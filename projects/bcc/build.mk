# Copyright (c) Meta Platforms, Inc. and affiliates.

BCC_ANDROID_DEPS = llvm libbpf flex elfutils python xz
BCC_HOST_DEPS = cmake flex python
$(eval $(call project-define,bcc))

BCC_EXTRA_CFLAGS += "-I$(abspath $(ANDROID_OUT_DIR))/include" -include strings.h
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
	cd $@ && CFLAGS="$(BCC_EXTRA_CFLAGS)" CXXFLAGS="$(BCC_EXTRA_CFLAGS)" LDFLAGS="$(BCC_EXTRA_LDFLAGS)" \
		$(CMAKE) $(BCC_SRCS) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		-DFLEX_EXECUTABLE=$(abspath $(HOST_OUT_DIR)/bin/flex) \
		-DBPS_LINK_RT=OFF \
		-DENABLE_TESTS=OFF \
		-DCMAKE_USE_LIBBPF_PACKAGE=ON \
		-DPYTHON_CMD=$(abspath $(HOST_OUT_DIR)/bin/python.xinstall)

BCC_COMMIT = eb8ede2d70b17350757f2570ef76ea4c2e1dbff8
BCC_REPO = https://github.com/iovisor/bcc
projects/bcc/sources:
	git clone $(BCC_REPO) $@
	cd $@ && git checkout $(BCC_COMMIT)
