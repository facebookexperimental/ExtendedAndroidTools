# Copyright (c) Meta Platforms, Inc. and affiliates.

NDK_API = 28
NDK_PATH = /opt/ndk/android-ndk-r23b
ANDROID_TOOLCHAIN_PATH = \
    $(abspath $(NDK_PATH)/toolchains/llvm/prebuilt/linux-x86_64/bin)
ANDROID_TOOLCHAIN_STRIP_PATH = $(ANDROID_TOOLCHAIN_PATH)/llvm-strip

include toolchain/autotools.mk
include toolchain/cmake.mk

ifeq ($(NDK_ARCH), arm64)
ANDROID_SYSROOT_LIB_SUBDIR = aarch64-linux-android
LIBCPP_ABI = arm64-v8a
else ifeq ($(NDK_ARCH), x86_64)
ANDROID_SYSROOT_LIB_SUBDIR = x86_64-linux-android
LIBCPP_ABI = x86_64
else ifeq ($(NDK_ARCH), armv7)
ANDROID_SYSROOT_LIB_SUBDIR = arm-linux-androideabi
LIBCPP_ABI = armeabi-v7a
else
$(error unknown abi $(NDK_ARCH))
endif

ANDROID_SYSROOT_PATH = \
    $(abspath $(NDK_PATH)/toolchains/llvm/prebuilt/linux-x86_64/sysroot)
ANDROID_SYSROOT_INCLUDE_PATH = \
    $(ANDROID_SYSROOT_PATH)/usr/include/
ANDROID_SYSROOT_LIB_PATH = \
    $(ANDROID_SYSROOT_PATH)/usr/lib/$(ANDROID_SYSROOT_LIB_SUBDIR)/$(NDK_API)/

$(ANDROID_OUT_DIR)/lib/libc++_shared.so: | $(ANDROID_OUT_DIR)
	cp $(NDK_PATH)/sources/cxx-stl/llvm-libc++/libs/$(LIBCPP_ABI)/libc++_shared.so $@
