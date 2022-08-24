# Copyright (c) Meta Platforms, Inc. and affiliates.

# number of threads to use. This value is passed to recursive make calls as -j
# option.
THREADS = 4

# arch: arm64 or x86_64
NDK_ARCH = arm64

# Release or Debug
BUILD_TYPE = Release

BUILD_DIR = build
ANDROID_BUILD_DIR = $(BUILD_DIR)/android/$(NDK_ARCH)
HOST_BUILD_DIR = $(BUILD_DIR)/host
DOWNLOADS_DIR = $(BUILD_DIR)/downloads

OUT_DIR = out
ANDROID_OUT_DIR = $(OUT_DIR)/android/$(NDK_ARCH)
ANDROID_SYSROOTS_OUT_DIR = $(OUT_DIR)/sysroots/$(NDK_ARCH)
HOST_OUT_DIR = $(OUT_DIR)/host

all:
	@echo "Choose a project to build"

include toolchain/toolchain.mk

$(ANDROID_BUILD_DIR) $(HOST_BUILD_DIR) $(DOWNLOADS_DIR) $(ANDROID_SYSROOTS_OUT_DIR):
	mkdir -p $@

$(ANDROID_OUT_DIR) $(HOST_OUT_DIR):
	mkdir -p $@
	mkdir $@/bin
	mkdir $@/include
	mkdir $@/lib
	mkdir $@/share
	mkdir $@/licenses

clean:
	-rm -fr $(BUILD_DIR)
	-rm -fr $(OUT_DIR)

.PHONY: clean fetch-sources remove-sources install uninstall
.DELETE_ON_ERROR:

include projects/project.mk
include projects/licenses.mk
include projects/*/build.mk
include sysroot/*.mk
