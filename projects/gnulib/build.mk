# Copyright (c) Facebook, Inc. and its affiliates.

$(eval $(call project-define,gnulib))

$(GNULIB_ANDROID):
	echo "gnulib build is not supported"
	false

GNULIB_COMMIT_HASH = cd46bf0ca5083162f3ac564ebbdeb6371085df45
GNULIB_REPO = https://git.savannah.gnu.org/git/gnulib.git
projects/gnulib/sources:
	git clone $(GNULIB_REPO) $@
	cd $@ && git checkout $(GNULIB_COMMIT_HASH)
