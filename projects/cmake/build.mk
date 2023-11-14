# Copyright (c) Meta Platforms, Inc. and affiliates.

$(eval $(call project-define,cmake))

$(CMAKE_HOST):
	cd $(CMAKE_HOST_BUILD_DIR) && make install -j $(THREADS)
	touch $@

$(CMAKE_HOST_BUILD_DIR):
	-mkdir $@
	cd $@ && $(CMAKE_SRCS)/bootstrap --prefix=$(abspath $(HOST_OUT_DIR))

CMAKE_VERSION = 3.22.2
CMAKE_URL = https://github.com/Kitware/CMake/releases/download/v$(CMAKE_VERSION)/cmake-$(CMAKE_VERSION).tar.gz
$(DOWNLOADS_DIR)/cmake-$(CMAKE_VERSION).tar.gz: | $(DOWNLOADS_DIR)
	cd $(DOWNLOADS_DIR) && curl -L -O $(CMAKE_URL)

projects/cmake/sources: $(DOWNLOADS_DIR)/cmake-$(CMAKE_VERSION).tar.gz
	-mkdir $@
	tar xf $(DOWNLOADS_DIR)/cmake-$(CMAKE_VERSION).tar.gz -C $@ \
		--transform="s|^cmake-$(CMAKE_VERSION)/||"
