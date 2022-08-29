# Copyright (c) Meta Platforms, Inc. and affiliates.

BCC_ANDROID_DEPS = llvm flex elfutils
BCC_HOST_DEPS = cmake flex
$(eval $(call project-define,bcc))

# bionic and libbpf (built as part of bcc) both provide linux/compiler.h header.
# In case of bionic the header defines empty __user macro which is used in many
# other headers provided by bionic. Unfortunately libbpf's copy does not define
# that macro and we get many build errors when including not-overriden headers.
# Let's fix it by definiting __user on our own.
BCC_EXTRA_CFLAGS += "-D__user="
BCC_EXTRA_CFLAGS += "-D__force="
BCC_EXTRA_CFLAGS += "-D__poll_t=unsigned"

BCC_EXTRA_LDFLAGS = "-L$(abspath $(ANDROID_OUT_DIR))/lib"

$(BCC_ANDROID):
ifeq ($(BUILD_TYPE), Debug)
	cd $(ANDROID_BUILD_DIR)/bcc && $(MAKE) install -j $(THREADS)
else
	cd $(ANDROID_BUILD_DIR)/bcc && $(MAKE) install/strip -j $(THREADS)
endif
	cp $(BCC_SRCS)/LICENSE.txt $(ANDROID_OUT_DIR)/licenses/bcc
	touch $@

# generates bcc build files for Android
$(BCC_ANDROID_BUILD_DIR): $(HOST_OUT_DIR)/bin/flex
	-mkdir $@
	cd $@ && LDFLAGS="$(BCC_EXTRA_LDFLAGS)" $(CMAKE) $(BCC_SRCS) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		-DCMAKE_C_FLAGS="$(BCC_EXTRA_CFLAGS)" \
		-DCMAKE_CXX_FLAGS="$(BCC_EXTRA_CFLAGS)" \
		-DFLEX_EXECUTABLE=$(abspath $(HOST_OUT_DIR)/bin/flex) \
		-DBPS_LINK_RT=OFF \
		-DENABLE_TESTS=OFF \
		-DPYTHON_CMD=python3.10

BCC_COMMIT = v0.24.0
BCC_REPO = https://github.com/iovisor/bcc
projects/bcc/sources:
	git clone $(BCC_REPO) $@
	cd $@ && git checkout $(BCC_COMMIT)
