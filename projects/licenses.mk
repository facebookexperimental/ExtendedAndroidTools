# Copyright (c) Meta Platforms, Inc. and affiliates.

# Definitions of licensing macros

LGPL_URL := https://www.gnu.org/licenses/lgpl-3.0.txt

fetch-license = curl -L $($(2)_URL) -o $(ANDROID_OUT_DIR)/licenses/$(1)
