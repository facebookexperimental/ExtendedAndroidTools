# Copyright (c) Meta Platforms, Inc. and affiliates.

BLACK_DONE := build/host/black.done

black-host: $(BLACK_DONE)

$(BLACK_DONE): python-host
	$(HOST_OUT_DIR)/bin/python3 -m pip install black
	mkdir -p build/host
	touch $@
