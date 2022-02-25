#! /bin/bash
# Copyright (c) Meta Platforms, Inc. and affiliates.

pushd scripts
docker build -t extended-android-tools -f ../docker/Dockerfile .
popd
