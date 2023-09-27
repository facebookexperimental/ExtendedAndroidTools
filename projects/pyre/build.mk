PYRE_HOST_DEPS = python
$(eval $(call project-define,pyre))


projects/pyre/sources:
	$(HOST_OUT_DIR)/bin/python3 -m pip install pyre-check
