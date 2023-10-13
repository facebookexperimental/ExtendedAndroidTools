# Copyright (c) Meta Platforms, Inc. and affiliates.

# number of threads to use. This value is passed to recursive make calls as -j
# option.
THREADS = 4

# arch: arm64, armv7, or x86_64
NDK_ARCH = arm64

# Release or Debug
BUILD_TYPE = Release

# For tools that support it, statically link against non-NDK dependencies to
# produce a self-contained binary.
STATIC_LINKING = false

# Only enable support for the BPF target in LLVM. This reduces the code size,
# but note that not all tools may work (in particular, bcc's rwengine also
# requires support for the $NDK_ARCH target)
LLVM_BPF_ONLY = false

BUILD_DIR = build
ANDROID_BUILD_DIR = $(BUILD_DIR)/android/$(NDK_ARCH)
HOST_BUILD_DIR = $(BUILD_DIR)/host
DOWNLOADS_DIR = $(BUILD_DIR)/downloads

OUT_DIR = out
ANDROID_OUT_DIR = $(OUT_DIR)/android/$(NDK_ARCH)
ANDROID_SYSROOTS_OUT_DIR = $(OUT_DIR)/sysroots/$(NDK_ARCH)
HOST_OUT_DIR = $(OUT_DIR)/host

HOST_OS = $(shell uname -o)
HOST_MACHINE = $(shell uname -m)

export PATH:=$(abspath $(HOST_OUT_DIR)/bin):$(PATH)

all:
	@echo "Choose a project to build"

include toolchains/toolchains.mk

$(ANDROID_BUILD_DIR) $(HOST_BUILD_DIR) $(DOWNLOADS_DIR) $(ANDROID_SYSROOTS_OUT_DIR):
	mkdir -p $@

$(ANDROID_OUT_DIR) $(HOST_OUT_DIR):
	mkdir -p $@
	mkdir $@/bin
	mkdir $@/include
	mkdir $@/lib
	mkdir $@/lib/pkgconfig
	mkdir $@/share
	mkdir $@/licenses

clean:
	-rm -fr $(BUILD_DIR)
	-rm -fr $(OUT_DIR)

setup-env:
	@echo "export PATH=\"$(PATH)\""

.PHONY: clean fetch-sources remove-sources install uninstall setup-env
.DELETE_ON_ERROR:

include projects/project.mk
include projects/licenses.mk
include projects/*/build.mk
include sysroot/*.mk
