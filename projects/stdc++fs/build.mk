# Copyright (c) Facebook, Inc. and its affiliates.

stdc++fs: $(ANDROID_BUILD_DIR)/stdc++fs.done

$(ANDROID_BUILD_DIR)/stdc++fs.done: $(ANDROID_STANDALONE_TOOLCHAIN_DIR) | $(ANDROID_BUILD_DIR) $(ANDROID_BUILD_DIR)/stdc++fs
	clang++ -c -std=c++17 projects/stdc++fs/thunks.cpp -o $(ANDROID_BUILD_DIR)/thunks.o
	llvm-ar rc $(ANDROID_OUT_DIR)/lib/libstdc++fs.a $(ANDROID_BUILD_DIR)/thunks.o
	touch $@

$(ANDROID_BUILD_DIR)/stdc++fs:
	mkdir -p $@
