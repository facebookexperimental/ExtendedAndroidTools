# Copyright (c) Facebook, Inc. and its affiliates.

NDK_API = 28
NDK_PATH = /opt/ndk/android-ndk-r17c

ifeq ($(NDK_ARCH), arm64)
ANDROID_TRIPLE = aarch64-linux-android
CMAKE_ABI = arm64-v8a
else ifeq ($(NDK_ARCH), x86_64)
ANDROID_TRIPLE = x86_64-linux-android
CMAKE_ABI = x86_64
else
$(error unknown abi $(NDK_ARCH))
endif

CMAKE = cmake

ANDROID_STANDALONE_TOOLCHAIN_DIR = ndk/$(NDK_ARCH)
ANDROID_CMAKE_TOOLCHAIN_FILE = $(ANDROID_BUILD_DIR)/toolchain-$(NDK_ARCH).cmake
ANDROID_EXTRA_CMAKE_FLAGS = -DCMAKE_TOOLCHAIN_FILE=$(abspath $(ANDROID_CMAKE_TOOLCHAIN_FILE))
ANDROID_EXTRA_CMAKE_FLAGS += -DCMAKE_INSTALL_PREFIX=$(abspath $(ANDROID_OUT_DIR))
ANDROID_EXTRA_CMAKE_FLAGS += -DCMAKE_BUILD_TYPE=$(BUILD_TYPE)
ANDROID_CMAKE_DEPS = $(ANDROID_STANDALONE_TOOLCHAIN_DIR) $(ANDROID_CMAKE_TOOLCHAIN_FILE)
ANDROID_EXTRA_CONFIGURE_FLAGS = --host=$(ANDROID_TRIPLE) --prefix=$(abspath $(ANDROID_OUT_DIR))

ANDROID_CMAKE_CXXFLAGS = -I $(abspath $(ANDROID_OUT_DIR))/include
ANDROID_CMAKE_LDFLAGS = -L $(abspath $(ANDROID_OUT_DIR))/lib
ANDROID_CMAKE_LDFLAGS += -Wl,-rpath-link -Wl,$(abspath $(ANDROID_OUT_DIR))/lib
ANDROID_CMAKE_LDFLAGS += "-pie"

export PATH := $(abspath $(ANDROID_STANDALONE_TOOLCHAIN_DIR))/bin:$(PATH)

$(ANDROID_STANDALONE_TOOLCHAIN_DIR):
	$(NDK_PATH)/build/tools/make_standalone_toolchain.py --arch $(NDK_ARCH) --api $(NDK_API) --install-dir $@

$(ANDROID_CMAKE_TOOLCHAIN_FILE): toolchain/toolchain.cmake
	mkdir -p $(ANDROID_BUILD_DIR)
	cp $< $@
	@sed -ibkp -e "s+<ABI>+$(CMAKE_ABI)+" $@
	@sed -ibkp -e "s+<TOOLCHAIN_PATH>+$(abspath $(ANDROID_STANDALONE_TOOLCHAIN_DIR))+" $@
	@sed -ibkp -e "s+<FIND_ROOT_PATH>+$(abspath $(ANDROID_OUT_DIR))+" $@
