# Copyright (c) Meta Platforms, Inc. and affiliates.

ifeq ($(NDK_ARCH), arm64)
TARGET_ARCH_ENV_VAR = arm64
else ifeq ($(NDK_ARCH), x86_64)
TARGET_ARCH_ENV_VAR = x86
else
$(error unknown abi $(NDK_ARCH))
endif

bpftools: bpftools-$(NDK_ARCH).tar.gz

bpftools-$(NDK_ARCH).tar.gz: $(ANDROID_SYSROOTS_OUT_DIR)/bpftools
	tar -zcf $@ $^ --owner=0 --group=0 \
		--transform="s|^$(ANDROID_SYSROOTS_OUT_DIR)/||"

$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: $(ANDROID_SYSROOTS_OUT_DIR)
$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: sysroot/setup.sh
$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: sysroot/run.sh
$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: sysroot/wrapper.sh.template
$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: $(call project-android-target,bcc)
$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: $(call project-android-target,bpftrace)
$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: $(call project-android-target,python)
$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: $(call project-android-target,xz)
$(ANDROID_SYSROOTS_OUT_DIR)/bpftools: $(ANDROID_OUT_DIR)/lib/libc++_shared.so
	mkdir -p $@/bin
	cp $(ANDROID_OUT_DIR)/bin/bpftrace $@/bin/
	cp -P $(ANDROID_OUT_DIR)/bin/python* $@/bin/
	cp $(ANDROID_OUT_DIR)/bin/xzcat $@/bin/

	mkdir -p $@/lib
	cp $(ANDROID_OUT_DIR)/lib/libbcc.so $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libbcc_bpf.so $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libclang.so $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libc++_shared.so $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libelf* $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libfl* $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/liblzma.so $@/lib/
	cp -a $(ANDROID_OUT_DIR)/lib/python3* $@/lib/
	cp $(ANDROID_OUT_DIR)/lib/libffi* $@/lib/

	mkdir -p $@/share
	cp -a $(ANDROID_OUT_DIR)/share/bcc $@/share/

	cp -r sysroot/run.sh $@/
	sed -e "s+<TARGET_ARCH_ENV_VAR>+$(TARGET_ARCH_ENV_VAR)+" sysroot/setup.sh > $@/setup.sh
	sed -e "s+<BIN>+bpftrace+" sysroot/wrapper.sh.template > $@/bpftrace
	chmod +x $@/bpftrace
	sed -e "s+<BIN>+python3.6m+" sysroot/wrapper.sh.template > $@/python3
	chmod +x $@/python3
	sed -e "s+<BIN>+xzcat+" sysroot/wrapper.sh.template > $@/xzcat
	chmod +x $@/xzcat
