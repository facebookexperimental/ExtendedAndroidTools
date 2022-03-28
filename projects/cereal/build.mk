# Copyright (c) Meta Platforms, Inc. and affiliates.

CEREAL_HOST_DEPS = cmake
$(eval $(call project-define,cereal))

$(CEREAL_ANDROID):
	cd $(CEREAL_ANDROID_BUILD_DIR) && make install -j $(THREADS)
	cp $(CEREAL_SRCS)/LICENSE $(ANDROID_OUT_DIR)/licenses/cereal
	touch $@

$(CEREAL_ANDROID_BUILD_DIR):
	-mkdir $@
	cd $@ && $(CMAKE) $(CEREAL_SRCS) \
		$(ANDROID_EXTRA_CMAKE_FLAGS) \
		-DBUILD_TESTS=OFF \
		-DBUILD_DOC=OFF \
		-DBUILD_SANDBOX=OFF \
		-DSKIP_PERFORMANCE_COMPARISON=ON

CEREAL_TAG = v1.3.2
CEREAL_REPO = https://github.com/USCiLab/cereal
projects/cereal/sources:
	git clone $(CEREAL_REPO) -b $(CEREAL_TAG) $@
