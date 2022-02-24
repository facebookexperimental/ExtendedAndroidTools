# Copyright (c) Facebook, Inc. and its affiliates.

$(eval $(call project-define,llvm))

ifeq ($(NDK_ARCH), arm64)
LLVM_HOST_TRIPLE = aarch64-none-linux-gnu
else ifeq ($(NDK_ARCH), x86_64)
LLVM_HOST_TRIPLE = x86_64-none-linux-gnu
else
$(error unknown abi $(NDK_ARCH))
endif

LLVM_EXTRA_CMAKE_FLAGS = -DLLVM_ENABLE_PROJECTS=clang
LLVM_EXTRA_HOST_FLAGS = -DLLVM_TEMPORARILY_ALLOW_OLD_TOOLCHAIN=1

$(LLVM_ANDROID):
ifeq ($(BUILD_TYPE), Debug)
	cd $(LLVM_ANDROID_BUILD_DIR) && $(MAKE) install -j $(THREADS)
else
	cd $(LLVM_ANDROID_BUILD_DIR) && $(MAKE) install/strip -j $(THREADS)
endif
	touch $@

$(LLVM_ANDROID_BUILD_DIR): $(HOST_OUT_DIR)/bin/llvm-config
$(LLVM_ANDROID_BUILD_DIR): $(HOST_OUT_DIR)/bin/llvm-tblgen
$(LLVM_ANDROID_BUILD_DIR): $(HOST_OUT_DIR)/bin/clang-tblgen
	-mkdir $@
	cd $@ && $(CMAKE) $(LLVM_SRCS)/llvm \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		$(LLVM_EXTRA_CMAKE_FLAGS) \
		-DLLVM_CONFIG_PATH=$(abspath $(HOST_OUT_DIR)/bin/llvm-config) \
		-DLLVM_TABLEGEN=$(abspath $(HOST_OUT_DIR)/bin/llvm-tblgen) \
		-DCLANG_TABLEGEN=$(abspath $(HOST_OUT_DIR)/bin/clang-tblgen) \
		-DLLVM_HOST_TRIPLE=$(LLVM_HOST_TRIPLE) \
		-DLLVM_ENABLE_RTTI=yes

# rules building host llvm-tblgen and clang-tblgen binaries necessary to
# cross compile llvm and clang for Android
$(HOST_OUT_DIR)/bin/llvm-config: $(LLVM_HOST_BUILD_DIR) | $(HOST_OUT_DIR)
$(HOST_OUT_DIR)/bin/llvm-tblgen: $(LLVM_HOST_BUILD_DIR) | $(HOST_OUT_DIR)
$(HOST_OUT_DIR)/bin/clang-tblgen: $(LLVM_HOST_BUILD_DIR) | $(HOST_OUT_DIR)
$(HOST_OUT_DIR)/bin/llvm-config $(HOST_OUT_DIR)/bin/llvm-tblgen $(HOST_OUT_DIR)/bin/clang-tblgen:
	cd $(LLVM_HOST_BUILD_DIR) && $(MAKE) -j $(THREADS) $(notdir $@)
	cp $(LLVM_HOST_BUILD_DIR)/bin/$(notdir $@) $@

# generates llvm build files for host
$(LLVM_HOST_BUILD_DIR):
	-mkdir $@
	cd $@ && $(CMAKE) $(LLVM_SRCS)/llvm \
		$(LLVM_EXTRA_CMAKE_FLAGS) \
		$(LLVM_EXTRA_HOST_FLAGS)

LLVM_BRANCH_OR_TAG = llvmorg-10.0.0
LLVM_REPO = https://github.com/llvm/llvm-project
projects/llvm/sources:
	git clone $(LLVM_REPO) $@ --depth=1 -b $(LLVM_BRANCH_OR_TAG)
