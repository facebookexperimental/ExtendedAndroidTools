# Copyright (c) Meta Platforms, Inc. and affiliates.

import asyncio
import abc


class JDWPInputStreamBase(abc.ABC):
    def __init__(self, reader: asyncio.StreamReader) -> None:
        self.reader = reader

    # Methods for OpaqueType
    @abc.abstractmethod
    async def read_boolean(self) -> bool:
        pass

    @abc.abstractmethod
    async def read_location(self) -> str:
        pass

    @abc.abstractmethod
    async def read_string(self) -> str:
        pass

    # Methods for IdType
    @abc.abstractmethod
    async def read_object_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_thread_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_thread_group_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_string_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_class_loader_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_class_object_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_array_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_reference_type_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_class_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_interface_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_array_type_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_method_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_field_id(self) -> str:
        pass

    @abc.abstractmethod
    async def read_frame_id(self) -> str:
        pass

    # Methods for IntegralType
    @abc.abstractmethod
    async def read_byte(self) -> int:
        pass

    @abc.abstractmethod
    async def read_int(self) -> int:
        pass

    @abc.abstractmethod
    async def read_long(
        self,
    ) -> int:
        pass


class JDWPOutputStreamBase(abc.ABC):
    def __init__(self, writer: asyncio.StreamWriter) -> None:
        self.writer = writer

    # Methods for OpaqueType
    @abc.abstractmethod
    def write_boolean(self, value: bool) -> None:
        pass

    @abc.abstractmethod
    def write_location(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_string(self, value: str) -> None:
        pass

    # Methods for IdType
    @abc.abstractmethod
    def write_object_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_thread_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_thread_group_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_string_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_class_loader_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_class_object_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_array_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_reference_type_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_class_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_interface_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_array_type_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_method_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_field_id(self, value: str) -> None:
        pass

    @abc.abstractmethod
    def write_frame_id(self, value: str) -> None:
        pass

    # Methods for IntegralType
    @abc.abstractmethod
    def write_byte(self, value: int) -> None:
        pass

    @abc.abstractmethod
    def write_int(self, value: int) -> None:
        pass

    @abc.abstractmethod
    def write_long(
        self,
        value: int,
    ) -> None:
        pass
