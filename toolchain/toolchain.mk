# Copyright (c) Facebook, Inc. and its affiliates.

NDK_API = 28
NDK_PATH = /opt/ndk/android-ndk-r17c
ANDROID_STANDALONE_TOOLCHAIN_DIR = ndk/$(NDK_ARCH)
ANDROID_TOOLCHAIN_PATH = $(abspath $(ANDROID_STANDALONE_TOOLCHAIN_DIR)/bin)

$(ANDROID_STANDALONE_TOOLCHAIN_DIR):
	$(NDK_PATH)/build/tools/make_standalone_toolchain.py --arch $(NDK_ARCH) --api $(NDK_API) --install-dir $@

include toolchain/autotools.mk
include toolchain/cmake.mk
