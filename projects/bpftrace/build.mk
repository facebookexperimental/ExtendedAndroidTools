# Copyright (c) Meta Platforms, Inc. and affiliates.

BPFTRACE_ANDROID_DEPS = bcc cereal elfutils flex libbpf llvm stdc++fs xz
BPFTRACE_HOST_DEPS = cmake flex
$(eval $(call project-define,bpftrace))

BPFTRACE_EXTRA_LDFLAGS = "-L$(abspath $(ANDROID_OUT_DIR))/lib"
BPFTRACE_EXTRA_CFLAGS = "-I$(abspath $(ANDROID_OUT_DIR))/include"

ifeq ($(STATIC_LINKING),true)
BPFTRACE_EXTRA_CMAKE_FLAGS = -DSTATIC_LINKING=ON

# XXX: As od 925127c5 ("Make bcc depend on liblzma") we're building libbcc
# with lzma support, but bpftrace currently doesn't have a way to detect this
# dependency, which causes undefined symbol errors when linking statically.
# This fixes it by adding liblzma to the link line.
BPFTRACE_EXTRA_LDFLAGS += "$(abspath $(ANDROID_OUT_DIR))/lib/liblzma.a"
endif

$(BPFTRACE_ANDROID): $(ANDROID_OUT_DIR)/lib/libc++_shared.so
	cd $(BPFTRACE_ANDROID_BUILD_DIR) && $(MAKE) install -j $(THREADS)
	cp $(BPFTRACE_SRCS)/LICENSE $(ANDROID_OUT_DIR)/licenses/bpftrace
	touch $@

$(BPFTRACE_ANDROID_BUILD_DIR): $(HOST_OUT_DIR)/bin/flex
	-mkdir $@
	cd $@ && LDFLAGS="$(BPFTRACE_EXTRA_LDFLAGS)" $(CMAKE) $(BPFTRACE_SRCS) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		$(BPFTRACE_EXTRA_CMAKE_FLAGS) \
		-DCMAKE_C_FLAGS="$(BPFTRACE_EXTRA_CFLAGS)" \
		-DBUILD_TESTING=OFF \
		-DENABLE_MAN=OFF \
		-DFLEX_EXECUTABLE=$(abspath $(HOST_OUT_DIR)/bin/flex) \
		-DALLOW_UNSAFE_PROBE=ON

BPFTRACE_COMMIT = 5d181c82acba400ec64e8d95c57cdb509f7cc57a
BPFTRACE_REPO = https://github.com/iovisor/bpftrace.git/
projects/bpftrace/sources:
	git clone $(BPFTRACE_REPO) $@
	cd $@ && git checkout $(BPFTRACE_COMMIT)
