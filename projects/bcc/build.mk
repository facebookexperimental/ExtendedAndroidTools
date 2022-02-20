# Copyright (c) Facebook, Inc. and its affiliates.

BCC_ANDROID_DEPS = llvm flex elfutils
BCC_HOST_DEPS = flex
$(eval $(call project-define,bcc))

# bionic and libbpf (built as part of bcc) both provide linux/compiler.h header.
# In case of bionic the header defines empty __user macro which is used in many
# other headers provided by bionic. Unfortunately libbpf's copy does not define
# that macro and we get many build errors when including not-overriden headers.
# Let's fix it by definiting __user on our own.
BCC_EXTRA_CFLAGS += "-D__user="

# Tests are built as part of regular bcc build and those tests depend on
# symbols that are not provided by bionic.
BCC_EXTRA_CFLAGS += "-include$(abspath projects/bcc/android_fixups/dl_fixups.h)"

# bits/reg.h header defining __WORDSIZE is missing, we need to provide our own
BCC_EXTRA_CFLAGS += "-I$(abspath projects/bcc/android_fixups)"

# stl we're building with provides std::make_unique, do not redefine it
BCC_EXTRA_CFLAGS += "-D__cpp_lib_make_unique"

$(BCC_ANDROID):
ifeq ($(BUILD_TYPE), Debug)
	cd $(ANDROID_BUILD_DIR)/bcc && $(MAKE) install -j $(THREADS)
else
	cd $(ANDROID_BUILD_DIR)/bcc && $(MAKE) install/strip -j $(THREADS)
endif
	touch $@

# generates bcc build files for Android
$(BCC_ANDROID_BUILD_DIR): $(HOST_OUT_DIR)/bin/flex
	-mkdir $@
	cd $@ && $(CMAKE) $(BCC_SRCS) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		-DCMAKE_C_FLAGS="$(BCC_EXTRA_CFLAGS)" \
		-DCMAKE_CXX_FLAGS="$(BCC_EXTRA_CFLAGS)" \
		-DFLEX_EXECUTABLE=$(abspath $(HOST_OUT_DIR)/bin/flex) \
		-DBPS_LINK_RT=OFF \
		-DPYTHON_CMD=python3.6

BCC_COMMIT = 4efe7fe3e81a65ca4d2cf6eec8055125ca3018f9
BCC_REPO = https://github.com/iovisor/bcc
projects/bcc/sources:
	git clone $(BCC_REPO) $@
	cd $@ && git checkout $(BCC_COMMIT)
