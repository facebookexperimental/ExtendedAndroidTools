python: $(ANDROID_BUILD_DIR)/python.done
fetch-sources: projects/python/sources
remove-sources: remove-python-sources

ifeq ($(PYTHON_SOURCES),)
PYTHON_SOURCES = $(abspath projects/python/sources)
$(ANDROID_BUILD_DIR)/python: projects/python/sources
endif

PYTHON_CONFIG_SITE = $(abspath projects/python/config.site)
PYTHON_EXTRA_ENV_DEFS += CONFIG_SITE=$(PYTHON_CONFIG_SITE)
PYTHON_EXTRA_ENV_DEFS += PKG_CONFIG_LIBDIR=$(abspath out/android/lib/pkgconfig)
PYTHON_EXTRA_ENV_DEFS += LDFLAGS=-L$(abspath out/android/lib64)
PYTHON_EXTRA_CONFIG_OPTIONS = --build=x86_64 --disable-ipv6 --without-ensurepip --with-system-ffi

$(ANDROID_BUILD_DIR)/python.done: $(ANDROID_BUILD_DIR)/python
	cd $(ANDROID_BUILD_DIR)/python && make install -j $(THREADS)
	touch $@

$(ANDROID_BUILD_DIR)/python: $(ANDROID_TOOLCHAIN_DIR) ffi | $(ANDROID_BUILD_DIR)
	mkdir -p $@
	cd $@ && $(PYTHON_EXTRA_ENV_DEFS) $(PYTHON_SOURCES)/configure \
		$(ANDROID_EXTRA_CONFIGURE_FLAGS) \
		$(PYTHON_EXTRA_CONFIG_OPTIONS)

PYTHON_BRANCH_OR_TAG = v3.6.8
PYTHON_REPO = https://github.com/python/cpython.git
projects/python/sources:
	git clone $(PYTHON_REPO) $@ --depth=1 -b $(PYTHON_BRANCH_OR_TAG)

.PHONY: remove-python-sources
remove-python-sources:
	rm -rf projects/python/sources
