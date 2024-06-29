
MPFR_ANDROID_DEPS = gmp

$(eval $(call project-define,mpfr))

$(MPFR_ANDROID):
	cd $(MPFR_ANDROID_BUILD_DIR) && make -j $(THREADS)
	cd $(MPFR_ANDROID_BUILD_DIR)/src && make install
	touch $@

$(MPFR_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	-mkdir $@
	cd $@ && $(MPFR_SRCS)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS) --with-gmp=$(abspath $(ANDROID_OUT_DIR))

$(HOST_OUT_DIR)/bin/mpfr: $(MPFR_HOST)

$(MPFR_HOST):
	cd $(MPFR_HOST_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(MPFR_HOST_BUILD_DIR):
	-mkdir $@
	echo "ANDROID_OUT_DIR:$(ANDROID_OUT_DIR)"
	cd $@ && $(MPFR_SRCS)/configure --prefix=$(abspath $(HOST_OUT_DIR)) \
		--with-gmp=$(ANDROID_OUT_DIR) \
				 --enable-maintainer-mode

MPFR_COMMIT_HASH = 5b3bdbf1ffe5ebbb9c2641cef250d9b1e016d951
MPFR_REPO =  https://gitlab.inria.fr/mpfr/mpfr.git
projects/mpfr/sources:
	git clone $(MPFR_REPO) $@
	cd $@ && git checkout $(MPFR_COMMIT_HASH)
	cd $@ && ./autogen.sh -i
