# Copyright (c) Facebook, Inc. and its affiliates.

argp: $(ANDROID_BUILD_DIR)/argp.done
fetch-sources: projects/argp/sources
remove-sources: remove-argp-sources

ifeq ($(ARGP_SOURCES),)
ARGP_SOURCES = $(abspath projects/argp/sources)
$(ANDROID_BUILD_DIR)/argp: projects/argp/sources
endif

$(ANDROID_BUILD_DIR)/argp.done: $(ANDROID_BUILD_DIR)/argp | $(ANDROID_OUT_DIR)
	cd $(ANDROID_BUILD_DIR)/argp && make -j $(THREADS)
	cp $(ANDROID_BUILD_DIR)/argp/gllib/libargp.a $(ANDROID_OUT_DIR)/lib/.
	cp projects/argp/headers/argp-wrapper.h $(ANDROID_OUT_DIR)/include/argp.h
	cp $(ARGP_SOURCES)/gllib/argp.h $(ANDROID_OUT_DIR)/include/argp-real.h
	touch $@

$(ANDROID_BUILD_DIR)/argp: $(ANDROID_CONFIG_SITE)
$(ANDROID_BUILD_DIR)/argp: | $(ANDROID_BUILD_DIR)
	-mkdir $@
	cd $@ && $(ARGP_SOURCES)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

GNULIB_COMMIT_HASH = cd46bf0ca5083162f3ac564ebbdeb6371085df45
GNULIB_REPO = https://git.savannah.gnu.org/git/gnulib.git
projects/argp/sources: | $(DOWNLOADS_DIR)
	-git clone $(GNULIB_REPO) $(DOWNLOADS_DIR)/gnulib
	cd $(DOWNLOADS_DIR)/gnulib && git checkout $(GNULIB_COMMIT_HASH)
	cd $(DOWNLOADS_DIR)/gnulib && ./gnulib-tool --create-testdir \
		--lib="libargp" --dir=$(abspath $@) argp

.PHONY: remove-argp-sources
remove-argp-sources:
	rm -rf projects/argp/sources
