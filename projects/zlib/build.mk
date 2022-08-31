# Copyright (c) Meta Platforms, Inc. and affiliates.

$(ANDROID_OUT_DIR)/lib/pkgconfig/zlib.pc: | $(ANDROID_OUT_DIR)
	echo "Name: zlib" >> $@
	echo "Description:" >> $@
	echo "Version: 1.2.11" >> $@
	echo "Libs: -lz" >> $@
