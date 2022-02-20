# Copyright (c) Facebook, Inc. and its affiliates.

NDK_API = 28
NDK_PATH = /opt/ndk/android-ndk-r23b
ANDROID_TOOLCHAIN_PATH = \
    $(abspath $(NDK_PATH)/toolchains/llvm/prebuilt/linux-x86_64/bin)

include toolchain/autotools.mk
include toolchain/cmake.mk
