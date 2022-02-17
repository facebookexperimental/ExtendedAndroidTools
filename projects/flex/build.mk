# Copyright (c) Facebook, Inc. and its affiliates.

flex: $(ANDROID_BUILD_DIR)/flex.done
flex-host: $(HOST_OUT_DIR)/bin/flex
fetch-sources: projects/flex/sources
remove-sources: remove-flex-sources

ifeq ($(FLEX_SOURCES),)
FLEX_SOURCES = $(abspath projects/flex/sources)
$(HOST_BUILD_DIR)/flex: projects/flex/sources
$(ANDROID_BUILD_DIR)/flex: projects/flex/sources
endif

$(ANDROID_BUILD_DIR)/flex.done: $(ANDROID_BUILD_DIR)/flex
	cd $(ANDROID_BUILD_DIR)/flex && make -j $(THREADS)
	cd $(ANDROID_BUILD_DIR)/flex/src && make install-libLTLIBRARIES install-binPROGRAMS install-includeHEADERS
	touch $@

$(ANDROID_BUILD_DIR)/flex: $(ANDROID_CONFIG_SITE) | $(ANDROID_BUILD_DIR)
	-mkdir $@
	cd $@ && $(FLEX_SOURCES)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

$(HOST_OUT_DIR)/bin/flex: $(HOST_BUILD_DIR)/flex.done

$(HOST_BUILD_DIR)/flex.done: $(HOST_BUILD_DIR)/flex
	cd $(HOST_BUILD_DIR)/flex && make install -j $(THREADS)
	touch $@

$(HOST_BUILD_DIR)/flex: | $(HOST_BUILD_DIR)
	-mkdir $@
	cd $@ && $(FLEX_SOURCES)/configure --prefix=$(abspath $(HOST_OUT_DIR))

FLEX_COMMIT_HASH = 98018e3f58d79e082216d406866942841d4bdf8a
FLEX_REPO = https://github.com/westes/flex.git
projects/flex/sources:
ifeq ($(shell whoami), vagrant)
	git clone $(FLEX_REPO) /tmp/flex_sources
	cd /tmp/flex_sources && git checkout $(FLEX_COMMIT_HASH)
	cd /tmp/flex_sources && ./autogen.sh
	mv /tmp/flex_sources $@
else
	git clone $(FLEX_REPO) $@
	cd $@ && git checkout $(FLEX_COMMIT_HASH)
	cd $@ && autoreconf -i -f
endif

.PHONY: remove-flex-sources
remove-flex-sources:
	rm -rf projects/flex/sources
