# Copyright (c) Meta Platforms, Inc. and affiliates.

$(eval $(call project-define,flex))

$(FLEX_ANDROID):
	cd $(FLEX_ANDROID_BUILD_DIR) && make -j $(THREADS)
	cd $(FLEX_ANDROID_BUILD_DIR)/src && make install-libLTLIBRARIES install-binPROGRAMS install-includeHEADERS
	cp $(FLEX_SRCS)/COPYING $(ANDROID_OUT_DIR)/licenses/flex
	touch $@

$(FLEX_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	-mkdir $@
	cd $@ && $(FLEX_SRCS)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

$(HOST_OUT_DIR)/bin/flex: $(FLEX_HOST)

$(FLEX_HOST):
	cd $(FLEX_HOST_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(FLEX_HOST_BUILD_DIR):
	-mkdir $@
	cd $@ && $(FLEX_SRCS)/configure --prefix=$(abspath $(HOST_OUT_DIR))

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
