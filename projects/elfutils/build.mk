# Copyright (c) Facebook, Inc. and its affiliates.

elfutils: $(ANDROID_BUILD_DIR)/elfutils.done
fetch-sources: projects/elfutils/sources
remove-sources: remove-elfutils-sources

ifeq ($(ELFUTILS_SOURCES),)
ELFUTILS_SOURCES = $(abspath projects/elfutils/sources)
$(ANDROID_BUILD_DIR)/elfutils: projects/elfutils/sources
endif

ELFUTILS_EXTRA_CFLAGS = -I$(abspath $(ANDROID_OUT_DIR)/include)
ELFUTILS_EXTRA_CFLAGS += -I$(abspath projects/elfutils/android_fixups)
ELFUTILS_EXTRA_CFLAGS += -Dprogram_invocation_short_name=\\\"no-program_invocation_short_name\\\"

ELFUTILS_EXTRA_LDFLAGS = -L$(abspath $(ANDROID_OUT_DIR)/lib)
ELFUTILS_EXTRA_ENV_DEFS = CFLAGS="$(ELFUTILS_EXTRA_CFLAGS)" LDFLAGS="$(ELFUTILS_EXTRA_LDFLAGS)"

$(ANDROID_BUILD_DIR)/elfutils.done: $(ANDROID_BUILD_DIR)/elfutils
	cd $(ANDROID_BUILD_DIR)/elfutils/lib && make -j $(THREADS)
	cd $(ANDROID_BUILD_DIR)/elfutils/libelf && make install -j $(THREADS)
	touch $@

$(ANDROID_BUILD_DIR)/elfutils: $(ANDROID_CONFIG_SITE)
$(ANDROID_BUILD_DIR)/elfutils: argp
$(ANDROID_BUILD_DIR)/elfutils: | $(ANDROID_BUILD_DIR)
	-mkdir $@
	cd $@ && $(ELFUTILS_EXTRA_ENV_DEFS) $(ELFUTILS_SOURCES)/configure \
		$(ANDROID_EXTRA_CONFIGURE_FLAGS)

ELFUTILS_VERSION = 0.176
ELFUTILS_URL = http://sourceware.org/pub/elfutils/$(ELFUTILS_VERSION)/elfutils-$(ELFUTILS_VERSION).tar.bz2
projects/elfutils/sources: | $(DOWNLOADS_DIR)
	wget $(ELFUTILS_URL) -O $(DOWNLOADS_DIR)/elfutils-$(ELFUTILS_VERSION).tar.bz2
	-mkdir $@
	tar xf $(DOWNLOADS_DIR)/elfutils-$(ELFUTILS_VERSION).tar.bz2 -C $@ \
		--transform="s|^elfutils-$(ELFUTILS_VERSION)||"

remove-elfutils-sources:
	rm -rf projects/elfutils/sources
