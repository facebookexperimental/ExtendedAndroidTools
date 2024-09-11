# Copyright (c) Meta Platforms, Inc. and affiliates.

$(eval $(call project-define,ffi))

FFI_EXTRA_LDFLAGS = -Wl,--undefined-version

$(FFI_ANDROID):
	cd $(FFI_ANDROID_BUILD_DIR) && make install -j $(THREADS)
	cp $(FFI_SRCS)/LICENSE $(ANDROID_OUT_DIR)/licenses/ffi
	touch $@

$(FFI_HOST):
	cd $(FFI_HOST_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(FFI_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	mkdir -p $@
	cd $@ && EXTRA_LDFLAGS=$(FFI_EXTRA_LDFLAGS) $(FFI_SRCS)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

$(FFI_HOST_BUILD_DIR): $(HOST_CONFIG_SITE)
	mkdir -p $@
	cd $@ && $(FFI_SRCS)/configure $(HOST_EXTRA_CONFIGURE_FLAGS)

FFI_BRANCH_OR_TAG = v3.3-rc0
FFI_REPO = https://github.com/libffi/libffi
projects/ffi/sources:
	git clone $(FFI_REPO) $@ --depth=1 -b $(FFI_BRANCH_OR_TAG)
	cd $@ && autoreconf -i -f
