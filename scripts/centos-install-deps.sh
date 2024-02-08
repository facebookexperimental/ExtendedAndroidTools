#! /bin/bash
# Copyright (c) Meta Platforms, Inc. and affiliates.

echo "installing deps..."

sudo dnf -y install \
     autoconf \
     automake \
     bison \
     curl \
     flex \
     gcc-c++ \
     gettext \
     gettext-devel \
     git \
     help2man \
     libtool \
     make \
     openssl-devel \
     pkg-config \
     po4a \
     texinfo \
     unzip \
     wget \
     zlib \
     zstd
