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
ANDROID_TOOLCHAIN_PATH = $(abspath $(ANDROID_STANDALONE_TOOLCHAIN_DIR)/bin)
ANDROID_CONFIG_SITE = $(ANDROID_OUT_DIR)/share/config.site
ANDROID_EXTRA_CONFIGURE_FLAGS = --host=$(ANDROID_TRIPLE) --prefix=$(abspath $(ANDROID_OUT_DIR))

ANDROID_CMAKE_TOOLCHAIN_FILE = $(NDK_PATH)/build/cmake/android.toolchain.cmake
ANDROID_EXTRA_CMAKE_FLAGS = -DCMAKE_TOOLCHAIN_FILE=$(abspath $(ANDROID_CMAKE_TOOLCHAIN_FILE))
ANDROID_EXTRA_CMAKE_FLAGS += -DANDROID_ABI=$(CMAKE_ABI)
ANDROID_EXTRA_CMAKE_FLAGS += -DANDROID_PLATFORM=android-$(NDK_API)
ANDROID_EXTRA_CMAKE_FLAGS += -DANDROID_STL=c++_shared
ANDROID_EXTRA_CMAKE_FLAGS += -DANDROID_ALLOW_UNDEFINED_SYMBOLS=TRUE

ANDROID_EXTRA_CMAKE_FLAGS += -DCMAKE_INSTALL_PREFIX=$(abspath $(ANDROID_OUT_DIR))
ANDROID_EXTRA_CMAKE_FLAGS += -DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=BOTH
ANDROID_EXTRA_CMAKE_FLAGS += -DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=BOTH
ANDROID_EXTRA_CMAKE_FLAGS += -DCMAKE_FIND_ROOT_PATH_MODE_PACKAGE=BOTH
ANDROID_EXTRA_CMAKE_FLAGS += -DCMAKE_BUILD_TYPE=$(BUILD_TYPE)

ANDROID_CMAKE_LDFLAGS = -L$(abspath $(ANDROID_OUT_DIR))/lib
ANDROID_CMAKE_LDFLAGS += -Wl,-rpath-link -Wl,$(abspath $(ANDROID_OUT_DIR))/lib
ANDROID_EXTRA_CMAKE_FLAGS += -DANDROID_LINKER_FLAGS="$(ANDROID_CMAKE_LDFLAGS)"

$(ANDROID_STANDALONE_TOOLCHAIN_DIR):
	$(NDK_PATH)/build/tools/make_standalone_toolchain.py --arch $(NDK_ARCH) --api $(NDK_API) --install-dir $@

$(ANDROID_OUT_DIR)/lib/libc++_shared.so: | $(ANDROID_OUT_DIR)
	cp $(NDK_PATH)/sources/cxx-stl/llvm-libc++/libs/$(CMAKE_ABI)/libc++_shared.so $@

$(ANDROID_CONFIG_SITE): $(ANDROID_STANDALONE_TOOLCHAIN_DIR) | $(ANDROID_OUT_DIR)
	cp toolchain/config.site.template $@
	@sed -ibkp -e "s+<BIN_PATH>+$(abspath $(ANDROID_TOOLCHAIN_PATH))+g" $@
	@sed -ibkp -e "s+<TRIPLE>+$(ANDROID_TRIPLE)+g" $@
	@sed -ibkp -e "s+<SITE_PATH>+$(abspath $(ANDROID_OUT_DIR))+g" $@
