# Definitions of licensing macros

LGPL_URL := https://www.gnu.org/licenses/lgpl-3.0.txt

fetch-license = wget $($(2)_URL) -O $(ANDROID_OUT_DIR)/licenses/$(1)
