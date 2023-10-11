# Copyright (c) Meta Platforms, Inc. and affiliates.

BUCK2_VERSION := 2023-09-01
BUCK2_ARCHIVE := buck2.zst
BUCK2_URL := https://github.com/facebook/buck2/releases/download/$(BUCK2_VERSION)/buck2-x86_64-unknown-linux-gnu.zst

$(HOST_OUT_DIR)/bin/buck2: $(DOWNLOADS_DIR)/$(BUCK2_ARCHIVE) | $(HOST_OUT_DIR)
# commands to unpack $(BUCK2_ARCHIVE) and set the executable flag
	zstd -d $(DOWNLOADS_DIR)/$(BUCK2_ARCHIVE) -o $(HOST_OUT_DIR)/bin/buck2
	chmod +x $(HOST_OUT_DIR)/bin/buck2

$(DOWNLOADS_DIR)/$(BUCK2_ARCHIVE): | $(DOWNLOADS_DIR)
# instructions to download the archive
	wget -q -O $(DOWNLOADS_DIR)/$(BUCK2_ARCHIVE) $(BUCK2_URL)

# Phony target for host
.PHONY: buck2-host
buck2-host: $(HOST_OUT_DIR)/bin/buck2
