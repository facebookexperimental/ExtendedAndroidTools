# Copyright (c) Meta Platforms, Inc. and affiliates.

$(eval $(call project-define,argp))

$(ARGP_ANDROID):
	cd $(ARGP_ANDROID_BUILD_DIR) && make -j $(THREADS)
	cp $(ARGP_ANDROID_BUILD_DIR)/gllib/libargp.a $(ANDROID_OUT_DIR)/lib/.
	cp projects/argp/headers/argp-wrapper.h $(ANDROID_OUT_DIR)/include/argp.h
	cp $(ARGP_SRCS)/gllib/argp.h $(ANDROID_OUT_DIR)/include/argp-real.h
	$(call fetch-license,argp,LGPL)
	touch $@

$(ARGP_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	-mkdir $@
	cd $@ && $(ARGP_SRCS)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

projects/argp/sources: $(call project-optional-sources-target,gnulib)
	cd $(call project-sources,gnulib) && ./gnulib-tool --create-testdir \
		--lgpl --lib="libargp" --dir=$(abspath $@) argp
