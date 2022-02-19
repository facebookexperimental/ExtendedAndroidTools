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

projects/argp/sources: projects/gnulib/sources
	cd $(GNULIB_SOURCES) && ./gnulib-tool --create-testdir \
		--lib="libargp" --dir=$(abspath $@) argp

.PHONY: remove-argp-sources
remove-argp-sources:
	rm -rf projects/argp/sources
