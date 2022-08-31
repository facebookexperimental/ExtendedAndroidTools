# Copyright (c) Meta Platforms, Inc. and affiliates.

FROM ubuntu:jammy

COPY jammy-install-deps.sh /
COPY download-ndk.sh /

RUN bash -c "/jammy-install-deps.sh" && \
    bash -c "/download-ndk.sh /opt/ndk"

WORKDIR /ExtendedAndroidTools

ENTRYPOINT ["/bin/bash"]
