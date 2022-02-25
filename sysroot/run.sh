#!/system/bin/env sh
# Copyright (c) Meta Platforms, Inc. and affiliates.

SYSROOT=$(realpath $(dirname $_))
source "${SYSROOT}/setup.sh" > /dev/null
exec "$@"
