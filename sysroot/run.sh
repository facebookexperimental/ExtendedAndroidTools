#!/system/bin/env sh
# Copyright (c) Meta Platforms, Inc. and affiliates.

SYSROOT=$(realpath $(dirname $0))
source "${SYSROOT}/setup.sh" > /dev/null
exec "$@"
