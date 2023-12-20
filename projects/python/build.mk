# Copyright (c) Meta Platforms, Inc. and affiliates.

PYTHON_ANDROID_DEPS = ffi
PYTHON_HOST_DEPS = ffi
$(eval $(call project-define,python))

PYTHON_ANDROID_EXTRA_CONFIG_OPTIONS = --build=x86_64 --disable-ipv6 --without-ensurepip --with-system-ffi
PYTHON_ANDROID_EXTRA_CONFIG_OPTIONS += "EXTRA_CPPFLAGS=-I$(ANDROID_SYSROOT_INCLUDE_PATH)"
PYTHON_ANDROID_EXTRA_CONFIG_OPTIONS += "EXTRA_LDFLAGS=-L$(ANDROID_SYSROOT_LIB_PATH)"
PYTHON_ANDROID_EXTRA_CONFIG_OPTIONS += ac_cv_file__dev_ptmx=no
PYTHON_ANDROID_EXTRA_CONFIG_OPTIONS += ac_cv_file__dev_ptc=no

$(PYTHON_ANDROID):
	cd $(PYTHON_ANDROID_BUILD_DIR) && make install -j $(THREADS)
	cp $(PYTHON_SRCS)/LICENSE $(ANDROID_OUT_DIR)/licenses/python
	touch $@

$(PYTHON_HOST): $(HOST_OUT_DIR)/bin/python.xinstall
	cd $(PYTHON_HOST_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(HOST_OUT_DIR)/bin/python.xinstall: projects/python/python.xinstall.template
$(HOST_OUT_DIR)/bin/python.xinstall: | $(HOST_OUT_DIR)
	cp $^ $@
	sed -ibkp -e "s+<HOST_OUT_DIR>+$(abspath $(HOST_OUT_DIR))+g" $@
	sed -ibkp -e "s+<ANDROID_OUT_DIR>+$(abspath $(ANDROID_OUT_DIR))+g" $@
	chmod +x $@

$(PYTHON_ANDROID_BUILD_DIR): \
    export PKG_CONFIG_LIBDIR=$(abspath $(ANDROID_OUT_DIR)/lib/pkgconfig)
$(PYTHON_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
$(PYTHON_ANDROID_BUILD_DIR): $(PYTHON_HOST)
	mkdir -p $@
	cd $@ && $(PYTHON_SRCS)/configure \
		$(ANDROID_EXTRA_CONFIGURE_FLAGS) \
		$(PYTHON_ANDROID_EXTRA_CONFIG_OPTIONS)

$(PYTHON_HOST_BUILD_DIR): \
    export PKG_CONFIG_LIBDIR=$(abspath $(HOST_OUT_DIR)/lib/pkgconfig)
$(PYTHON_HOST_BUILD_DIR): $(HOST_CONFIG_SITE)
	mkdir -p $@
	cd $@ && $(PYTHON_SRCS)/configure \
		$(HOST_EXTRA_CONFIGURE_FLAGS) \
		--with-system-ffi

PYTHON_BRANCH_OR_TAG = v3.10.6
PYTHON_REPO = https://github.com/python/cpython.git
projects/python/sources:
	git clone $(PYTHON_REPO) $@ --depth=1 -b $(PYTHON_BRANCH_OR_TAG)
