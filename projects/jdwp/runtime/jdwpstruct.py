# Copyright (c) Meta Platforms, Inc. and affiliates.

from __future__ import annotations

import abc
from projects.jdwp.runtime.async_streams import (
    JDWPInputStreamBase,
    JDWPOutputStreamBase,
)


class JDWPStruct(abc.ABC):
    @abc.abstractmethod
    def serialize(self, output: JDWPOutputStreamBase):
        pass

    @staticmethod
    @abc.abstractmethod
    async def parse(input: JDWPInputStreamBase) -> JDWPStruct:
        pass
