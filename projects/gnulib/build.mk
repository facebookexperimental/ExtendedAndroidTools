# Copyright (c) Meta Platforms, Inc. and affiliates.

$(eval $(call project-define,gnulib))

$(GNULIB_ANDROID):
	echo "gnulib build is not supported"
	false

GNULIB_COMMIT_HASH = 044bf893acee0a55b22b4be0ede0e3ce010c480a
GNULIB_REPO = https://github.com/simpleton/gnulib-mirror
projects/gnulib/sources:
	git clone $(GNULIB_REPO) $@
	cd $@ && git checkout $(GNULIB_COMMIT_HASH)
