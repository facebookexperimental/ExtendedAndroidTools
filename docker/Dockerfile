# Copyright (c) Facebook, Inc. and its affiliates.

FROM ubuntu:bionic

COPY bionic-install-deps.sh /
COPY download-ndk.sh /

RUN bash -c "/bionic-install-deps.sh" && \
    bash -c "/download-ndk.sh /opt/ndk"

WORKDIR /ExtendedAndroidTools

ENTRYPOINT ["/bin/bash"]