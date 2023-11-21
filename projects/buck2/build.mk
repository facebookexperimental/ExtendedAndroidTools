# Copyright (c) Meta Platforms, Inc. and affiliates.

BUCK2_VERSION := 2023-10-01

ifeq ($(HOST_OS),GNU/Linux)
BUCK2_ARCHIVE_SUFFIX := unknown-linux-gnu
else
BUCK2_ARCHIVE_SUFFIX := apple-darwin
endif

ifeq ($(HOST_MACHINE),arm64)
BUCK2_ARCHIVE_INFIX := aarch64
else
BUCK2_ARCHIVE_INFIX := $(HOST_MACHINE)
endif

BUCK2_ARCHIVE := buck2-$(BUCK2_ARCHIVE_INFIX)-$(BUCK2_ARCHIVE_SUFFIX).zst
BUCK2_URL := https://github.com/facebook/buck2/releases/download/$(BUCK2_VERSION)/$(BUCK2_ARCHIVE)

$(HOST_OUT_DIR)/bin/buck2: $(DOWNLOADS_DIR)/$(BUCK2_ARCHIVE) | $(HOST_OUT_DIR)
# commands to unpack $(BUCK2_ARCHIVE) and set the executable flag
	zstd -d $(DOWNLOADS_DIR)/$(BUCK2_ARCHIVE) -o $@
	touch $@
	chmod +x $@

$(DOWNLOADS_DIR)/$(BUCK2_ARCHIVE): | $(DOWNLOADS_DIR)
# instructions to download the archive
	curl -L -s -o $@ $(BUCK2_URL)

# Phony target for host
.PHONY: buck2-host
buck2-host: $(HOST_OUT_DIR)/bin/buck2
