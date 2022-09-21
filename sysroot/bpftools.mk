# Copyright (c) Meta Platforms, Inc. and affiliates.

ifeq ($(NDK_ARCH), arm64)
TARGET_ARCH_ENV_VAR = arm64
else ifeq ($(NDK_ARCH), x86_64)
TARGET_ARCH_ENV_VAR = x86
else ifeq ($(NDK_ARCH), armv7)
TARGET_ARCH_ENV_VAR = arm
else
$(error unknown abi $(NDK_ARCH))
endif

GEN_SETUP_SCRIPT = sed -e "s+<TARGET_ARCH_ENV_VAR>+$(TARGET_ARCH_ENV_VAR)+" sysroot/setup.sh > $@/setup.sh
gen-wrapper = sed -e "s+<BIN>+$(1)+" sysroot/wrapper.sh.template > $@/$(1) && chmod +x $@/$(1)

BPFTOOLS = $(ANDROID_SYSROOTS_OUT_DIR)/bpftools
BPFTOOLS_TAR = bpftools-$(NDK_ARCH).tar.gz
bpftools: $(BPFTOOLS_TAR)

BPFTOOLS_MIN = $(ANDROID_SYSROOTS_OUT_DIR)/bpftools-min
BPFTOOLS_MIN_TAR = bpftools-min-$(NDK_ARCH).tar.gz
bpftools-min: $(BPFTOOLS_MIN_TAR)

$(BPFTOOLS_TAR): $(BPFTOOLS)
$(BPFTOOLS_MIN_TAR): $(BPFTOOLS_MIN)
$(BPFTOOLS_TAR) $(BPFTOOLS_MIN_TAR):
	tar -zcf $@ $^ --owner=0 --group=0 \
		--transform="s|^$(ANDROID_SYSROOTS_OUT_DIR)/||"

$(BPFTOOLS) $(BPFTOOLS_MIN): $(ANDROID_SYSROOTS_OUT_DIR)
$(BPFTOOLS) $(BPFTOOLS_MIN): sysroot/setup.sh
$(BPFTOOLS) $(BPFTOOLS_MIN): sysroot/run.sh
$(BPFTOOLS) $(BPFTOOLS_MIN): sysroot/wrapper.sh.template
$(BPFTOOLS) $(BPFTOOLS_MIN): $(call project-android-target,bcc)
$(BPFTOOLS) $(BPFTOOLS_MIN): $(call project-android-target,bpftrace)
$(BPFTOOLS) $(BPFTOOLS_MIN): $(call project-android-target,xz)
$(BPFTOOLS) $(BPFTOOLS_MIN): $(ANDROID_OUT_DIR)/lib/libc++_shared.so
$(BPFTOOLS): $(call project-android-target,python)

$(BPFTOOLS):
	mkdir -p $@/bin
	cp $(ANDROID_OUT_DIR)/bin/bpftrace $@/bin/
	cp $(ANDROID_OUT_DIR)/bin/bpftrace-aotrt $@/bin/
	cp -P $(ANDROID_OUT_DIR)/bin/python* $@/bin/
	cp $(ANDROID_OUT_DIR)/bin/xzcat $@/bin/

	mkdir -p $@/lib
	cp $(ANDROID_OUT_DIR)/lib/libbcc.so $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libbcc_bpf.so $@/lib/
	cp -a $(ANDROID_OUT_DIR)/lib/libbpf.so* $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libclang.so $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libc++_shared.so $@/lib/
	cp -a $(ANDROID_OUT_DIR)/lib/libelf*.so* $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libfl.so $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/liblzma.so $@/lib/
	cp -a $(ANDROID_OUT_DIR)/lib/python3* $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libffi.so $@/lib/

	mkdir -p $@/share
	cp -a $(ANDROID_OUT_DIR)/share/bcc $@/share/
	cp -a $(ANDROID_OUT_DIR)/share/bpftrace $@/share/

	cp -r sysroot/run.sh $@/
	$(GEN_SETUP_SCRIPT)
	$(call gen-wrapper,bpftrace)
	$(call gen-wrapper,bpftrace-aotrt)
	$(call gen-wrapper,python3.10)
	cp $@/python3.10 $@/python3
	$(call gen-wrapper,xzcat)

	cp -r $(ANDROID_OUT_DIR)/licenses $@/licenses

$(BPFTOOLS_MIN):
	mkdir -p $@/bin
	cp $(ANDROID_OUT_DIR)/bin/bpftrace $@/bin/
	cp $(ANDROID_OUT_DIR)/bin/xzcat $@/bin/

	mkdir -p $@/lib
	cp $(ANDROID_OUT_DIR)/lib/libbcc_bpf.so $@/lib/
	cp -a $(ANDROID_OUT_DIR)/lib/libbpf.so* $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libclang.so $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libc++_shared.so $@/lib/
	cp -a $(ANDROID_OUT_DIR)/lib/libelf*.so* $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/liblzma.so $@/lib/

	mkdir -p $@/share
	cp -a $(ANDROID_OUT_DIR)/share/bpftrace $@/share/

	cp -r sysroot/run.sh $@/
	$(GEN_SETUP_SCRIPT)
	$(call gen-wrapper,bpftrace)
	$(call gen-wrapper,xzcat)

	cp -r $(ANDROID_OUT_DIR)/licenses $@/licenses
