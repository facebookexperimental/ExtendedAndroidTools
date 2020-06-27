#!/system/bin/env sh
# Copyright (c) Facebook, Inc. and its affiliates.

SYSROOT=$(realpath $(dirname $_))
source "${SYSROOT}/setup.sh" > /dev/null
exec "$@"
