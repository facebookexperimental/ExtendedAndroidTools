#! /bin/bash

echo "downloading ndk..."

wget -q https://dl.google.com/android/repository/android-ndk-r17c-linux-x86_64.zip
unzip -q android-ndk-r17c-linux-x86_64.zip
rm android-ndk-r17c-linux-x86_64.zip

echo "done"
