# Copyright (c) Facebook, Inc. and its affiliates.

bpftrace: $(ANDROID_OUT_DIR)/bin/bpftrace
bpftrace: $(ANDROID_OUT_DIR)/share/bpftrace/tools
fetch-sources: projects/bpftrace/sources
remove-sources: remove-bpftrace-sources

ifeq ($(BPFTRACE_SOURCES),)
BPFTRACE_SOURCES = $(abspath projects/bpftrace/sources)
$(ANDROID_BUILD_DIR)/bpftrace: projects/bpftrace/sources
endif

$(ANDROID_OUT_DIR)/bin/bpftrace: $(ANDROID_BUILD_DIR)/bpftrace | $(ANDROID_OUT_DIR)
	cd $(ANDROID_BUILD_DIR)/bpftrace && $(MAKE) bpftrace -j $(THREADS)
	cp $(ANDROID_BUILD_DIR)/bpftrace/src/bpftrace $@

# generates bcc build files for Android
$(ANDROID_BUILD_DIR)/bpftrace: bcc elfutils flex flex-host llvm
$(ANDROID_BUILD_DIR)/bpftrace: $(ANDROID_OUT_DIR)/lib/libc++_shared.so
$(ANDROID_BUILD_DIR)/bpftrace: $(HOST_OUT_DIR)/bin/flex
$(ANDROID_BUILD_DIR)/bpftrace: $(ANDROID_CMAKE_DEPS)
$(ANDROID_BUILD_DIR)/bpftrace: | $(ANDROID_BUILD_DIR)
	-mkdir $@
	cd $@ && CXXFLAGS="$(ANDROID_CMAKE_CXXFLAGS)" LDFLAGS="$(ANDROID_CMAKE_LDFLAGS)" \
		$(CMAKE) $(BPFTRACE_SOURCES) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		-DLIBBCC_INCLUDE_DIRS=$(abspath $(ANDROID_OUT_DIR)/include) \
		-DFLEX_EXECUTABLE=$(abspath $(HOST_OUT_DIR)/bin/flex) \
		-DALLOW_UNSAFE_PROBE=ON

$(ANDROID_OUT_DIR)/share/bpftrace/tools:
	mkdir -p $@
	cp $(BPFTRACE_SOURCES)/tools/*.bt $@

BPFTRACE_COMMIT = 954049043568350af934275202d4414f0f800db7
BPFTRACE_REPO = https://github.com/iovisor/bpftrace.git/
projects/bpftrace/sources:
	git clone $(BPFTRACE_REPO) $@
	cd $@ && git checkout $(BPFTRACE_COMMIT)

.PHONY: remove-bpftrace-sources
remove-bpftrace-sources:
	rm -rf projects/bpftrace/sources
