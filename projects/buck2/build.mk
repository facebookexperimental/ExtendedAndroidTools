# Makefile for downloading and installing the Buck2 binary
$(eval $(call project-define,buck2))

# Project-specific variables
PROJECT_NAME := buck2
PROJECT_VERSION := 2023-09-01

# Installation directories
INSTALL_DIR := out/host/bin

# Binary name and paths
BINARY_NAME := buck2
BINARY_PATH := $(INSTALL_DIR)/$(BINARY_NAME)
COMPRESSED_BINARY := $(BINARY_PATH).zst

# URL for the release asset
RELEASE_URL := https://github.com/facebook/$(PROJECT_NAME)/releases/download/$(PROJECT_VERSION)/$(BINARY_NAME)-x86_64-unknown-linux-gnu.zst

# Check if wget is available and install it if missing
WGET := $(shell command -v wget 2> /dev/null)
ifeq ($(WGET),)
    WGET := $(shell apt-get -qy install wget && command -v wget)
    ifeq ($(WGET),)
        $(error "Failed to install wget. Please install it manually and try again.")
    endif
endif

# Check if zstd is available and install it if missing
ZSTD := $(shell command -v zstd 2> /dev/null)
ifeq ($(ZSTD),)
    ZSTD := $(shell apt-get -qy install zstd && command -v zstd)
    ifeq ($(ZSTD),)
        $(error "Failed to install zstd. Please install it manually and try again.")
    endif
endif

# Target to download and install the binary
$(BINARY_PATH): | $(INSTALL_DIR)
	$(WGET) -q -O $(COMPRESSED_BINARY) $(RELEASE_URL)
	$(ZSTD) -d -o $(BINARY_PATH) $(COMPRESSED_BINARY)
	chmod +x $(BINARY_PATH)
	rm $(COMPRESSED_BINARY)

# Target to create the installation directory if it doesn't exist
$(INSTALL_DIR):
	mkdir -p $@


# Default target to fetch and install the binary
projects/buck2/sources: $(BINARY_PATH)