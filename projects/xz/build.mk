# Copyright (c) Meta Platforms, Inc. and affiliates.

$(eval $(call project-define,xz))

$(XZ_ANDROID):
	cd $(XZ_ANDROID_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(XZ_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	mkdir -p $@
	cd $@ && $(XZ_SRCS)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

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
