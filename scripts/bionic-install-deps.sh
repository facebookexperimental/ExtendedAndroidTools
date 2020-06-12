#! /bin/bash

echo "installing deps..."

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y \
     autoconf \
     automake \
     autopoint \
     bison \
     cmake \
     flex \
     gettext \
     git \
     help2man \
     libtool \
     make \
     python \
     python3-distutils \
     texinfo \
     unzip \
     wget

echo "done"
