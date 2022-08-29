#! /bin/bash
# Copyright (c) Meta Platforms, Inc. and affiliates.

echo "installing deps..."

apt-get update
apt-get install -y \
     autoconf \
     automake \
     autopoint \
     bison \
     flex \
     g++ \
     gettext \
     git \
     help2man \
     libssl-dev \
     libtool \
     make \
     pkg-config \
     po4a \
     texinfo \
     unzip \
     wget \
     zlib1g-dev

echo "done"
