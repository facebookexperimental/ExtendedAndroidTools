#! /bin/bash
# Copyright (c) Meta Platforms, Inc. and affiliates.

pushd scripts
docker build --pull --no-cache -t extended-android-tools -f ../docker/Dockerfile .
popd
