#! /bin/bash
# Copyright (c) Facebook, Inc. and its affiliates.

pushd scripts
docker build -t extended-android-tools -f ../docker/Dockerfile .
popd
