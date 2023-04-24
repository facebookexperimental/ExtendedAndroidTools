#!/system/bin/env sh
# Copyright (c) Meta Platforms, Inc. and affiliates.

SYSROOT=$(realpath $(dirname $0))

echo "setting up sysroot installed at $SYSROOT"

# links below are required by bcc python library which opens those libs with
# dlopen. Not the best solution but a solution
if [[ ! -e $SYSROOT/lib/libbcc.so.0 ]]; then
    ln $SYSROOT/lib/libbcc.so -s $SYSROOT/lib/libbcc.so.0
fi
if [[ ! -e $SYSROOT/lib/libc.so.6 ]]; then
    ln /system/lib64/libc.so -s $SYSROOT/lib/libc.so.6
fi
if [[ ! -e $SYSROOT/lib/librt.so.1 ]]; then
    ln /system/lib64/libc.so -s $SYSROOT/lib/librt.so.1
fi

export PATH=$SYSROOT/bin:$PATH
export LD_LIBRARY_PATH=$SYSROOT/lib:$SYSROOT/lib64:$LD_LIBRARY_PATH

# define environment variables bpftrace and bcc need to determine arch and
# kernel source path
export ARCH="<TARGET_ARCH_ENV_VAR>"

# bpftrace caches symbols per executable name. All java processes fork from
# zygote (and have the same executable name) which results in bad symbol names
# reported if libraries are loaded in different order.
export BPFTRACE_CACHE_USER_SYMBOLS=0

# tell python where to find bcc in case we built the package on ubuntu/debian
export PYTHONPATH=$SYSROOT/lib/python3.10/site-packages/bcc-0.27.0-py3.10.egg:$PYTHONPATH

export TMPDIR=/data/local/tmp

echo "done"
