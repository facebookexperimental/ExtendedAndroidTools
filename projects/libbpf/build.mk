# Copyright (c) Meta Platforms, Inc. and affiliates.

LIBBPF_ANDROID_DEPS = elfutils
$(eval $(call project-define,libbpf))

LIBBPF_EXTRA_CFLAGS += "-D__user="
LIBBPF_EXTRA_CFLAGS += "-D__force="
LIBBPF_EXTRA_CFLAGS += "-D__poll_t=unsigned"
LIBBPF_EXTRA_CFLAGS += "-Wno-tautological-constant-out-of-range-compare"

$(LIBBPF_ANDROID): \
    export PKG_CONFIG_LIBDIR=$(abspath $(ANDROID_OUT_DIR)/lib/pkgconfig)
$(LIBBPF_ANDROID): $(ANDROID_OUT_DIR)/lib/pkgconfig/zlib.pc
	cd $(LIBBPF_SRCS)/src && make install install_uapi_headers \
		-j $(THREADS) \
		LIBSUBDIR=lib \
		PREFIX=$(abspath $(ANDROID_OUT_DIR)) \
		OBJDIR=$(abspath $(LIBBPF_ANDROID_BUILD_DIR)) \
		AR=$(abspath $(ANDROID_TOOLCHAIN_PATH)/llvm-ar) \
		CC=$(abspath $(ANDROID_TOOLCHAIN_PATH)/$(ANDROID_TRIPLE)$(NDK_API)-clang) \
		EXTRA_CFLAGS="$(LIBBPF_EXTRA_CFLAGS)"
	cp $(LIBBPF_SRCS)/LICENSE $(ANDROID_OUT_DIR)/licenses/libbpf
	touch $@

$(LIBBPF_ANDROID_BUILD_DIR):
	mkdir -p $@

LIBBPF_TAG = v1.5.0
LIBBPF_REPO = https://github.com/libbpf/libbpf
projects/libbpf/sources:
	git clone $(LIBBPF_REPO) $@ -b $(LIBBPF_TAG)
