# Copyright (c) Meta Platforms, Inc. and affiliates.

stdc++fs: $(ANDROID_BUILD_DIR)/stdc++fs.done

$(ANDROID_BUILD_DIR)/stdc++fs.done: $(ANDROID_BUILD_DIR) $(ANDROID_BUILD_DIR)/stdc++fs
	$(ANDROID_TOOLCHAIN_PATH)/clang++ -target $(ANDROID_TRIPLE) -c -std=c++17 projects/stdc++fs/thunks.cpp -o $(ANDROID_BUILD_DIR)/thunks.o
	$(ANDROID_TOOLCHAIN_PATH)/llvm-ar rc $(ANDROID_OUT_DIR)/lib/libstdc++fs.a $(ANDROID_BUILD_DIR)/thunks.o
	touch $@

$(ANDROID_BUILD_DIR)/stdc++fs:
	mkdir -p $@
