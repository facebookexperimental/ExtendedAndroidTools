$(eval $(call project-define,gmp))

$(GMP_ANDROID):
	cd $(GMP_ANDROID_BUILD_DIR) && make -j $(THREADS)
	cd $(GMP_ANDROID_BUILD_DIR) && make install
	cp $(GMP_SRCS)/COPYING $(ANDROID_OUT_DIR)/licenses/gmp
	touch $@

$(GMP_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	-mkdir $@
	cd $@ && $(GMP_SRCS)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS)

$(HOST_OUT_DIR)/bin/gmp: $(GMP_HOST)

$(GMP_HOST):
	cd $(GMP_HOST_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(GMP_HOST_BUILD_DIR):
	-mkdir $@
	cd $@ && $(GMP_SRCS)/configure --prefix=$(abspath $(HOST_OUT_DIR)) \
				 --enable-maintainer-mode

GMP_COMMIT_HASH = 14fe69d7f56e00917e9fd9ab616afc798a1af6c1
GMP_REPO = https://github.com/gmp-mirror/gmp.git
projects/gmp/sources:
	git clone $(GMP_REPO) $@
	cd $@ && git checkout $(GMP_COMMIT_HASH)
	cd $@ && autoreconf -v -f -i
	cp $@/../version.texi $@/doc/
