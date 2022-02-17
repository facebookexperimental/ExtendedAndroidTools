# Copyright (c) Facebook, Inc. and its affiliates.

xz: $(ANDROID_BUILD_DIR)/xz.done
fetch-sources: projects/xz/sources
remove-sources: remove-xz-sources

ifeq ($(XZ_SOURCES),)
XZ_SOURCES = $(abspath projects/xz/sources)
$(ANDROID_BUILD_DIR)/xz: projects/xz/sources
endif

$(ANDROID_BUILD_DIR)/xz.done: $(ANDROID_BUILD_DIR)/xz
	cd $(ANDROID_BUILD_DIR)/xz && make install -j $(THREADS)
	touch $@

$(ANDROID_BUILD_DIR)/xz: $(ANDROID_CONFIG_SITE) | $(ANDROID_BUILD_DIR)
	mkdir -p $@
	cd $@ && $(XZ_SOURCES)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

XZ_BRANCH_OR_TAG = v5.2.5
XZ_REPO = https://git.tukaani.org/xz.git
projects/xz/sources:
ifeq ($(shell whoami), vagrant)
	git clone $(XZ_REPO) /tmp/xz_sources -b $(XZ_BRANCH_OR_TAG)
	cd /tmp/xz_sources && ./autogen.sh
	mv /tmp/xz_sources $@
else
	git clone $(XZ_REPO) $@ -b $(XZ_BRANCH_OR_TAG)
	cd $@ && ./autogen.sh
endif

.PHONY: remove-xz-sources
remove-xz-sources:
	rm -rf projects/xz/sources
