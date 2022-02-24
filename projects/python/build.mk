# Copyright (c) Facebook, Inc. and its affiliates.

PYTHON_ANDROID_DEPS = ffi
$(eval $(call project-define,python))

PYTHON_EXTRA_CONFIG_OPTIONS = --build=x86_64 --disable-ipv6 --without-ensurepip --with-system-ffi
PYTHON_EXTRA_CONFIG_OPTIONS += ac_cv_file__dev_ptmx=no
PYTHON_EXTRA_CONFIG_OPTIONS += ac_cv_file__dev_ptc=no

$(PYTHON_ANDROID):
	cd $(PYTHON_ANDROID_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(PYTHON_ANDROID_BUILD_DIR): \
    export PKG_CONFIG_LIBDIR=$(abspath $(ANDROID_OUT_DIR)/lib/pkgconfig)
$(PYTHON_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	mkdir -p $@
	cd $@ && $(PYTHON_SRCS)/configure \
		$(ANDROID_EXTRA_CONFIGURE_FLAGS) \
		$(PYTHON_EXTRA_CONFIG_OPTIONS)

PYTHON_BRANCH_OR_TAG = v3.6.8
PYTHON_REPO = https://github.com/python/cpython.git
projects/python/sources:
	git clone $(PYTHON_REPO) $@ --depth=1 -b $(PYTHON_BRANCH_OR_TAG)
