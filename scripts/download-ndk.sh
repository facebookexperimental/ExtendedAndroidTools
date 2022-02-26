#! /bin/bash
# Copyright (c) Meta Platforms, Inc. and affiliates.

dest="${1:-$(cwd)}"
echo "downloading ndk to ${dest}..."

wget -q -P /tmp https://dl.google.com/android/repository/android-ndk-r23b-linux.zip
unzip -q /tmp/android-ndk-r23b-linux.zip -d "${dest}"
rm /tmp/android-ndk-r23b-linux.zip

echo "done"
