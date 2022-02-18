# Copyright (c) Facebook, Inc. and its affiliates.

ifeq ($(NDK_ARCH), arm64)
ANDROID_TRIPLE = aarch64-linux-android
else ifeq ($(NDK_ARCH), x86_64)
ANDROID_TRIPLE = x86_64-linux-android
else
$(error unknown abi $(NDK_ARCH))
endif

ANDROID_CONFIG_SITE = $(ANDROID_OUT_DIR)/share/config.site
ANDROID_EXTRA_CONFIGURE_FLAGS = --host=$(ANDROID_TRIPLE) --prefix=$(abspath $(ANDROID_OUT_DIR))

$(ANDROID_OUT_DIR)/lib/libc++_shared.so: | $(ANDROID_OUT_DIR)
	cp $(NDK_PATH)/sources/cxx-stl/llvm-libc++/libs/$(CMAKE_ABI)/libc++_shared.so $@

$(ANDROID_CONFIG_SITE): $(ANDROID_STANDALONE_TOOLCHAIN_DIR) | $(ANDROID_OUT_DIR)
	cp toolchain/config.site.template $@
	@sed -ibkp -e "s+<BIN_PATH>+$(abspath $(ANDROID_TOOLCHAIN_PATH))+g" $@
	@sed -ibkp -e "s+<TRIPLE>+$(ANDROID_TRIPLE)+g" $@
	@sed -ibkp -e "s+<SITE_PATH>+$(abspath $(ANDROID_OUT_DIR))+g" $@
