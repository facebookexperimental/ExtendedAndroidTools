# Copyright (c) Meta Platforms, Inc. and affiliates.

$(eval $(call project-define,obstack))

$(OBSTACK_ANDROID):
	cd $(OBSTACK_ANDROID_BUILD_DIR) && make -j $(THREADS)
	cp $(OBSTACK_ANDROID_BUILD_DIR)/gllib/libobstack.a $(ANDROID_OUT_DIR)/lib/.
	cp $(OBSTACK_SRCS)/gllib/obstack.h $(ANDROID_OUT_DIR)/include/obstack.h
	touch $@

$(OBSTACK_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	-mkdir $@
	cd $@ && $(OBSTACK_SRCS)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

projects/obstack/sources: $(call project-optional-sources-target,gnulib)
	cd $(call project-sources,gnulib) && ./gnulib-tool --create-testdir \
		--lib="libobstack" --dir=$(abspath $@) obstack
