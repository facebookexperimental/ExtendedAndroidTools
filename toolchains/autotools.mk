# Copyright (c) Meta Platforms, Inc. and affiliates.

ifeq ($(NDK_ARCH), arm64)
ANDROID_TRIPLE = aarch64-linux-android
else ifeq ($(NDK_ARCH), x86_64)
ANDROID_TRIPLE = x86_64-linux-android
else ifeq ($(NDK_ARCH), armv7)
ANDROID_TRIPLE = armv7a-linux-androideabi
else
$(error unknown abi $(NDK_ARCH))
endif

ANDROID_CONFIG_SITE = $(ANDROID_OUT_DIR)/share/config.site
ANDROID_EXTRA_CONFIGURE_FLAGS = --host=$(ANDROID_TRIPLE) --prefix=$(abspath $(ANDROID_OUT_DIR))

HOST_CONFIG_SITE = $(HOST_OUT_DIR)/share/config.site
HOST_EXTRA_CONFIGURE_FLAGS = --prefix=$(abspath $(HOST_OUT_DIR))

$(ANDROID_CONFIG_SITE): | $(ANDROID_OUT_DIR)
	cp toolchains/config.site.template $@
	@sed -ibkp -e "s+<BIN_PATH>+$(abspath $(ANDROID_TOOLCHAIN_PATH))+g" $@
	@sed -ibkp -e "s+<TRIPLE>+$(ANDROID_TRIPLE)+g" $@
	@sed -ibkp -e "s+<SITE_PATH>+$(abspath $(ANDROID_OUT_DIR))+g" $@
	@sed -ibkp -e "s+<API>+$(NDK_API)+g" $@

$(HOST_CONFIG_SITE): | $(HOST_OUT_DIR)
	cp toolchains/config.site.host.template $@
	@sed -ibkp -e "s+<SITE_PATH>+$(abspath $(HOST_OUT_DIR))+g" $@
