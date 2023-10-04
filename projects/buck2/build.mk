# --------------------------------------------------------------------------------
# Project: Buck2 Build Script
# Description: This script is used for building and managing the Buck2 project.
# Author: Christian Abrokwa
# --------------------------------------------------------------------------------

# Copyright (c) Meta Platforms, Inc. and affiliates.

$(eval $(call project-define,buck2))

PROJECT_NAME := buck2
PROJECT_VERSION := 2023-09-01

HOST_OUT_DIR := out/host/bin
BUILD_HOST_DIR :=build/host

BUCK2_HOST_OUT_TARGET := $(HOST_OUT_DIR)/buck2
BUCK2_HOST_BUILD_TARGET := $(BUILD_HOST_DIR)
BUCK2_ZIP_TARGET := $(BUCK2_OUT_TARGET).zip

BUCK2_URL := https://github.com/facebook/$(PROJECT_NAME)/archive/refs/tags/$(PROJECT_VERSION).zip

# ZSTD := $(shell command -v zstd 2> /dev/null)
# ifeq ($(ZSTD),)
# 	ZSTD := $(shell apt-get -qy install zstd && command -v zstd)
# 	ifeq ($(ZSTD),)
# 		$(error "Failed to install zstd. Please install it manually and try again.")
# 	endif
# endif


# Define the target for the host build
$(BUCK2_HOST): $(BUCK2_HOST_BUILD_DIR)
	@echo "Buck2 host build complete"

$(BUCK2_HOST_BUILD_DIR):
	mkdir -p $(BUCK2_HOST_OUT_TARGET) $(BUCK2_HOST_BUILD_TARGET)
	wget -q -O  $(BUCK2_ZIP_TARGET) $(BUCK2_URL)
	unzip $(BUCK2_ZIP_TARGET) -d $(BUCK2_HOST_OUT_TARGET)
	cp -r $(BUCK2_HOST_OUT_TARGET)/* $(BUCK2_HOST_BUILD_TARGET)
	chmod +x $(BUCK2_HOST_OUT_TARGET)/*
	rm $(BUCK2_ZIP_TARGET)
	touch $@

# Phony target for host
.PHONY: buck2-host
buck2-host: $(BUCK2_HOST)

projects/buck2/sources: $(BUCK2_HOST)
#	git clone $(BUCK2_REPO) $@ --depth=1 -b $(BUCK2_BRANCH_OR_TAG)