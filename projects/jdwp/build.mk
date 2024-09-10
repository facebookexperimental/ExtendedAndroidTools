# Copyright (c) Meta Platforms, Inc. and affiliates.

jdwp-host-prepare: \
  black-host \
  buck2-host \
  python-host \
  pyre-host

jdwp-check: jdwp-host-prepare
	buck2 run //projects/jdwp:main
	buck2 test //projects/jdwp/...
	pyre check
	black projects/jdwp --check

jdwp-format: black-host
	black projects/jdwp
