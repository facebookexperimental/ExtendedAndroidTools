# Copyright (c) Meta Platforms, Inc. and affiliates.

ELFUTILS_ANDROID_DEPS = argp obstack
$(eval $(call project-define,elfutils))

ELFUTILS_EXTRA_CFLAGS += -I$(abspath projects/elfutils/android_fixups)
ELFUTILS_EXTRA_CFLAGS += -Dprogram_invocation_short_name=\\\"no-program_invocation_short_name\\\"

$(ELFUTILS_ANDROID):
	cd $(ELFUTILS_ANDROID_BUILD_DIR)/lib && make -j $(THREADS)
	cd $(ELFUTILS_ANDROID_BUILD_DIR)/libelf && make install -j $(THREADS)
	cd $(ELFUTILS_ANDROID_BUILD_DIR)/config && make
	cp $(ELFUTILS_ANDROID_BUILD_DIR)/config/libelf.pc $(ANDROID_OUT_DIR)/lib/pkgconfig
	cp $(ELFUTILS_SRCS)/COPYING-LGPLV3 $(ANDROID_OUT_DIR)/licenses/elfutils-libs
	touch $@

$(ANDROID_BUILD_DIR)/elfutils: $(ANDROID_CONFIG_SITE)
$(ANDROID_BUILD_DIR)/elfutils: $(ANDROID_OUT_DIR)/lib/pkgconfig/zlib.pc
	-mkdir $@
	cd $@ && EXTRA_CFLAGS="$(ELFUTILS_EXTRA_CFLAGS)" $(ELFUTILS_SRCS)/configure \
		$(ANDROID_EXTRA_CONFIGURE_FLAGS) \
		--disable-debuginfod \
		--disable-libdebuginfod \
		--enable-install-elfh

ELFUTILS_VERSION = 0.191
ELFUTILS_URL = http://sourceware.org/pub/elfutils/$(ELFUTILS_VERSION)/elfutils-$(ELFUTILS_VERSION).tar.bz2
projects/elfutils/sources: | $(DOWNLOADS_DIR)
	curl -L $(ELFUTILS_URL) -o $(DOWNLOADS_DIR)/elfutils-$(ELFUTILS_VERSION).tar.bz2
	-mkdir $@
	tar xf $(DOWNLOADS_DIR)/elfutils-$(ELFUTILS_VERSION).tar.bz2 -C $@ \
		--transform="s|^elfutils-$(ELFUTILS_VERSION)||"
