#! /bin/bash
# Copyright (c) Facebook, Inc. and its affiliates.

dest="${1:-$(cwd)}"
echo "downloading ndk to ${dest}..."

wget -q -P /tmp https://dl.google.com/android/repository/android-ndk-r17c-linux-x86_64.zip
unzip -q /tmp/android-ndk-r17c-linux-x86_64.zip -d "${dest}"
rm /tmp/android-ndk-r17c-linux-x86_64.zip

echo "done"
