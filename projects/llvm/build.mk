# Copyright (c) Facebook, Inc. and its affiliates.

llvm: $(ANDROID_BUILD_DIR)/llvm.done
fetch-sources: projects/llvm/sources
remove-sources: remove-llvm-sources

ifeq ($(LLVM_SOURCES),)
LLVM_SOURCES = $(abspath projects/llvm/sources/llvm)
$(HOST_BUILD_DIR)/llvm: projects/llvm/sources
$(ANDROID_BUILD_DIR)/llvm: projects/llvm/sources
endif

ifeq ($(NDK_ARCH), arm64)
LLVM_HOST_TRIPLE = aarch64-none-linux-gnu
else ifeq ($(NDK_ARCH), x86_64)
LLVM_HOST_TRIPLE = x86_64-none-linux-gnu
else
$(error unknown abi $(NDK_ARCH))
endif

LLVM_EXTRA_CMAKE_FLAGS = -DLLVM_ENABLE_PROJECTS=clang
LLVM_EXTRA_HOST_FLAGS = -DLLVM_TEMPORARILY_ALLOW_OLD_TOOLCHAIN=1

$(ANDROID_BUILD_DIR)/llvm.done: $(ANDROID_BUILD_DIR)/llvm | $(ANDROID_OUT_DIR)
ifeq ($(BUILD_TYPE), Debug)
	cd $(ANDROID_BUILD_DIR)/llvm && $(MAKE) install -j $(THREADS)
else
	cd $(ANDROID_BUILD_DIR)/llvm && $(MAKE) install/strip -j $(THREADS)
endif
	touch $@

$(ANDROID_BUILD_DIR)/llvm: $(HOST_OUT_DIR)/bin/llvm-config
$(ANDROID_BUILD_DIR)/llvm: $(HOST_OUT_DIR)/bin/llvm-tblgen
$(ANDROID_BUILD_DIR)/llvm: $(HOST_OUT_DIR)/bin/clang-tblgen
$(ANDROID_BUILD_DIR)/llvm: $(ANDROID_CMAKE_DEPS)
$(ANDROID_BUILD_DIR)/llvm: | $(ANDROID_BUILD_DIR)
	-mkdir $@
	cd $@ && CXXFLAGS="$(ANDROID_CMAKE_CXXFLAGS)" LDFLAGS="$(ANDROID_CMAKE_LDFLAGS)" \
		$(CMAKE) $(LLVM_SOURCES) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		$(LLVM_EXTRA_CMAKE_FLAGS) \
		-DLLVM_CONFIG_PATH=$(abspath $(HOST_OUT_DIR)/bin/llvm-config) \
		-DLLVM_TABLEGEN=$(abspath $(HOST_OUT_DIR)/bin/llvm-tblgen) \
		-DCLANG_TABLEGEN=$(abspath $(HOST_OUT_DIR)/bin/clang-tblgen) \
		-DLLVM_HOST_TRIPLE=$(LLVM_HOST_TRIPLE) \
		-DLLVM_ENABLE_RTTI=yes

# rules building host llvm-tblgen and clang-tblgen binaries necessary to
# cross compile llvm and clang for Android
$(HOST_OUT_DIR)/bin/llvm-config: $(HOST_BUILD_DIR)/llvm | $(HOST_OUT_DIR)
$(HOST_OUT_DIR)/bin/llvm-tblgen: $(HOST_BUILD_DIR)/llvm | $(HOST_OUT_DIR)
$(HOST_OUT_DIR)/bin/clang-tblgen: $(HOST_BUILD_DIR)/llvm | $(HOST_OUT_DIR)
$(HOST_OUT_DIR)/bin/llvm-config $(HOST_OUT_DIR)/bin/llvm-tblgen $(HOST_OUT_DIR)/bin/clang-tblgen:
	cd $(HOST_BUILD_DIR)/llvm && $(MAKE) -j $(THREADS) $(notdir $@)
	cp $(HOST_BUILD_DIR)/llvm/bin/$(notdir $@) $@

# generates llvm build files for host
$(HOST_BUILD_DIR)/llvm: $(LLVM_SOURCE_DEPS) | $(HOST_BUILD_DIR)
	-mkdir $@
	cd $@ && $(CMAKE) $(LLVM_SOURCES) \
		$(LLVM_EXTRA_CMAKE_FLAGS) \
		$(LLVM_EXTRA_HOST_FLAGS)

LLVM_BRANCH_OR_TAG = llvmorg-10.0.0
LLVM_REPO = https://github.com/llvm/llvm-project
projects/llvm/sources:
	git clone $(LLVM_REPO) $@ --depth=1 -b $(LLVM_BRANCH_OR_TAG)

.PHONY: remove-llvm-sources
remove-llvm-sources:
	rm -rf projects/llvm/sources
