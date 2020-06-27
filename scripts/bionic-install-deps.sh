#! /bin/bash
# Copyright (c) Facebook, Inc. and its affiliates.

echo "installing deps..."

apt-get update
apt-get install -y \
     autoconf \
     automake \
     autopoint \
     bison \
     cmake \
     flex \
     g++ \
     gettext \
     git \
     help2man \
     libtool \
     make \
     po4a \
     python \
     python3-distutils \
     texinfo \
     unzip \
     wget

echo "done"
