# Copyright (c) Facebook, Inc. and its affiliates.

fetch-sources: projects/gnulib/sources
remoce-sources: remove-gnulib-sources

ifeq ($(GNULIB_SOURCES),)
GNULIB_SOURCES = $(abspath projects/gnulib/sources)
GNULIB = projects/gnulib/sources
endif

GNULIB_COMMIT_HASH = cd46bf0ca5083162f3ac564ebbdeb6371085df45
GNULIB_REPO = https://git.savannah.gnu.org/git/gnulib.git
projects/gnulib/sources:
	git clone $(GNULIB_REPO) $@
	cd $@ && git checkout $(GNULIB_COMMIT_HASH)

.PHONY: remove-gnulib-sources
remove-gnulib-sources:
	rm -rf projects/gnulib/sources
