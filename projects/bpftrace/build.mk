# Copyright (c) Facebook, Inc. and its affiliates.

BPFTRACE_ANDROID_DEPS = bcc elfutils flex llvm stdc++fs
BPFTRACE_HOST_DEPS = flex
$(eval $(call project-define,bpftrace))

$(BPFTRACE_ANDROID): $(ANDROID_OUT_DIR)/lib/libc++_shared.so
	cd $(BPFTRACE_ANDROID_BUILD_DIR) && $(MAKE) bpftrace -j $(THREADS)
	cp $(BPFTRACE_ANDROID_BUILD_DIR)/src/bpftrace $(ANDROID_OUT_DIR)/bin/.
	touch $@

$(BPFTRACE_ANDROID_BUILD_DIR): $(HOST_OUT_DIR)/bin/flex
	-mkdir $@
	cd $@ && $(CMAKE) $(BPFTRACE_SRCS) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		-DLIBBCC_INCLUDE_DIRS=$(abspath $(ANDROID_OUT_DIR)/include) \
		-DFLEX_EXECUTABLE=$(abspath $(HOST_OUT_DIR)/bin/flex) \
		-DALLOW_UNSAFE_PROBE=ON

$(ANDROID_OUT_DIR)/share/bpftrace/tools:
	mkdir -p $@
	cp $(BPFTRACE_SOURCES)/tools/*.bt $@

BPFTRACE_COMMIT = e6bbb9a925e405c1ec87790490d81227ac122032
BPFTRACE_REPO = https://github.com/iovisor/bpftrace.git/
projects/bpftrace/sources:
	git clone $(BPFTRACE_REPO) $@
	cd $@ && git checkout $(BPFTRACE_COMMIT)
