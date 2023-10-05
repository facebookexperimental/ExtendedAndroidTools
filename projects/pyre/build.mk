# Copyright (c) Meta Platforms, Inc. and affiliates.

PYRE_CHECK_DONE := build/host/pyre-check.done

pyre-host: $(PYRE_CHECK_DONE)

$(PYRE_CHECK_DONE): python-host
	$(HOST_OUT_DIR)/bin/python3 -m pip install pyre-check
	mkdir -p build/host
	touch $@
