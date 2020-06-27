# Copyright (c) Facebook, Inc. and its affiliates.

ffi: $(ANDROID_BUILD_DIR)/ffi.done
fetch-sources: projects/ffi/sources
remove-sources: remove-ffi-sources

ifeq ($(FFI_SOURCES),)
FFI_SOURCES = $(abspath projects/ffi/sources)
$(ANDROID_BUILD_DIR)/ffi: projects/ffi/sources
endif

$(ANDROID_BUILD_DIR)/ffi.done: $(ANDROID_BUILD_DIR)/ffi
	cd $(ANDROID_BUILD_DIR)/ffi && make install -j $(THREADS)
	touch $@

$(ANDROID_BUILD_DIR)/ffi: $(ANDROID_STANDALONE_TOOLCHAIN_DIR) | $(ANDROID_BUILD_DIR)
	mkdir -p $@
	cd $@ && $(FFI_SOURCES)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

FFI_BRANCH_OR_TAG = v3.3-rc0
FFI_REPO = https://github.com/libffi/libffi
projects/ffi/sources:
	git clone $(FFI_REPO) $@ --depth=1 -b $(FFI_BRANCH_OR_TAG)
	cd $@ && autoreconf -i -f

.PHONY: remove-ffi-sources
remove-ffi-sources:
	rm -rf projects/ffi/sources
