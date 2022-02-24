# Copyright (c) Facebook, Inc. and its affiliates.

NDK_API = 28
NDK_PATH = /opt/ndk/android-ndk-r23b
ANDROID_TOOLCHAIN_PATH = \
    $(abspath $(NDK_PATH)/toolchains/llvm/prebuilt/linux-x86_64/bin)

include toolchain/autotools.mk
include toolchain/cmake.mk

ifeq ($(NDK_ARCH), arm64)
LIBCPP_ABI = arm64-v8a
else ifeq ($(NDK_ARCH), x86_64)
LIBCPP_ABI = x86_64
else
$(error unknown abi $(NDK_ARCH))
endif

$(ANDROID_OUT_DIR)/lib/libc++_shared.so: | $(ANDROID_OUT_DIR)
	cp $(NDK_PATH)/sources/cxx-stl/llvm-libc++/libs/$(LIBCPP_ABI)/libc++_shared.so $@
