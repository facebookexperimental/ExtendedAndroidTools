# Copyright (c) Meta Platforms, Inc. and affiliates.

BPFTRACE_ANDROID_DEPS = bcc cereal elfutils flex libbpf llvm stdc++fs xz
BPFTRACE_HOST_DEPS = cmake flex
$(eval $(call project-define,bpftrace))

BPFTRACE_EXTRA_LDFLAGS = "-L$(abspath $(ANDROID_OUT_DIR))/lib"

ifeq ($(STATIC_LINKING),true)
BPFTRACE_EXTRA_CMAKE_FLAGS = -DSTATIC_LINKING=ON

# XXX: As od 925127c5 ("Make bcc depend on liblzma") we're building libbcc
# with lzma support, but bpftrace currently doesn't have a way to detect this
# dependency, which causes undefined symbol errors when linking statically.
# This fixes it by adding liblzma to the link line.
BPFTRACE_EXTRA_LDFLAGS += "$(abspath $(ANDROID_OUT_DIR))/lib/liblzma.a"
endif

STRIP_THUNK = $(HOST_OUT_DIR)/bpftrace-strip-thunk

$(BPFTRACE_ANDROID): $(ANDROID_OUT_DIR)/lib/libc++_shared.so
ifeq ($(BUILD_TYPE), Debug)
	cd $(BPFTRACE_ANDROID_BUILD_DIR) && $(MAKE) install -j $(THREADS)
else
	cd $(BPFTRACE_ANDROID_BUILD_DIR) && $(MAKE) install/strip -j $(THREADS)
endif
	cp $(BPFTRACE_SRCS)/LICENSE $(ANDROID_OUT_DIR)/licenses/bpftrace
	touch $@

$(BPFTRACE_ANDROID_BUILD_DIR): $(HOST_OUT_DIR)/bin/flex $(STRIP_THUNK)
	-mkdir $@
	cd $@ && LDFLAGS="$(BPFTRACE_EXTRA_LDFLAGS)" $(CMAKE) $(BPFTRACE_SRCS) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		$(BPFTRACE_EXTRA_CMAKE_FLAGS) \
		-DBUILD_TESTING=OFF \
		-DENABLE_MAN=OFF \
		-DFLEX_EXECUTABLE=$(abspath $(HOST_OUT_DIR)/bin/flex) \
		-DUSE_SYSTEM_BPF_BCC=ON \
		-DALLOW_UNSAFE_PROBE=ON \
		-DCMAKE_STRIP=$(abspath $(STRIP_THUNK))

$(STRIP_THUNK): projects/bpftrace/strip-thunk | $(HOST_OUT_DIR)
	@sed -e "s+<STRIP_PATH>+$(ANDROID_TOOLCHAIN_STRIP_PATH)+g" $< > $@
	chmod +x $@

BPFTRACE_COMMIT = v0.21.2
BPFTRACE_REPO = https://github.com/iovisor/bpftrace.git/
projects/bpftrace/sources:
	git clone $(BPFTRACE_REPO) $@
	cd $@ && git checkout $(BPFTRACE_COMMIT) && git cherry-pick a77b8061f9291793e15c54a19a2202643d900387 --no-commit
