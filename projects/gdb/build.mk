GDB_ANDROID_DEPS = gmp mpfr

$(eval $(call project-define,gdb))

$(GDB_ANDROID):
	cd $(GDB_ANDROID_BUILD_DIR) && make -j $(THREADS)
	cd $(GDB_ANDROID_BUILD_DIR) && make install
	touch $@

$(GDB_ANDROID_BUILD_DIR): $(ANDROID_CONFIG_SITE)
	-mkdir $@
	cd $@ && $(GDB_SRCS)/configure $(ANDROID_EXTRA_CONFIGURE_FLAGS) \
		--with-gmp=$(abspath $(ANDROID_OUT_DIR)) \
		--with-mpfr=$(abspath $(ANDROID_OUT_DIR)) \
		--disable-gprofng

$(HOST_OUT_DIR)/bin/gdb: $(GDB_HOST)

$(GDB_HOST):
	cd $(GDB_HOST_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(GDB_HOST_BUILD_DIR):
	-mkdir $@
	cd $@ && $(GDB_SRCS)/configure --prefix=$(abspath $(HOST_OUT_DIR))

GDB_COMMIT_HASH = 17de5033a28cd04f9e16730b353ad7c08ec5d8c1
GDB_REPO = https://sourceware.org/git/binutils-gdb.git
projects/gdb/sources:
	git clone $(GDB_REPO) $@
	cd $@ && git checkout $(GDB_COMMIT_HASH)
	cd $@ && git am ../*patch
