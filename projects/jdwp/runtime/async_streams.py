# Copyright (c) Meta Platforms, Inc. and affiliates.

import abc
import typing

from projects.jdwp.defs.schema import IdType


class JDWPInputStreamBase(abc.ABC):
    # Methods for OpaqueType
    @abc.abstractmethod
    async def read_boolean(self) -> bool:
        pass

    @abc.abstractmethod
    async def read_location(self) -> typing.Any:
        pass

    @abc.abstractmethod
    async def read_string(self) -> str:
        pass

    # Methods for IdType
    @abc.abstractmethod
    async def read_object_id(self) -> IdType.OBJECT_ID:
        pass

    @abc.abstractmethod
    async def read_thread_id(self) -> IdType.THREAD_ID:
        pass

    @abc.abstractmethod
    async def read_thread_group_id(self) -> IdType.THREAD_GROUP_ID:
        pass

    @abc.abstractmethod
    async def read_string_id(self) -> IdType.STRING_ID:
        pass

    @abc.abstractmethod
    async def read_class_loader_id(self) -> IdType.CLASS_LOADER_ID:
        pass

    @abc.abstractmethod
    async def read_class_object_id(self) -> IdType.CLASS_OBJECT_ID:
        pass

    @abc.abstractmethod
    async def read_array_id(self) -> IdType.ARRAY_ID:
        pass

    @abc.abstractmethod
    async def read_reference_type_id(self) -> IdType.REFERENCE_TYPE_ID:
        pass

    @abc.abstractmethod
    async def read_class_id(self) -> IdType.CLASS_ID:
        pass

    @abc.abstractmethod
    async def read_interface_id(self) -> IdType.INTERFACE_ID:
        pass

    @abc.abstractmethod
    async def read_array_type_id(self) -> IdType.ARRAY_TYPE_ID:
        pass

    @abc.abstractmethod
    async def read_method_id(self) -> IdType.METHOD_ID:
        pass

    @abc.abstractmethod
    async def read_field_id(self) -> IdType.FIELD_ID:
        pass

    @abc.abstractmethod
    async def read_frame_id(self) -> IdType.FRAME_ID:
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
    # Methods for OpaqueType
    @abc.abstractmethod
    def write_boolean(self, value: bool) -> None:
        pass

    @abc.abstractmethod
    def write_location(self, value: typing.Any) -> None:
        pass

    @abc.abstractmethod
    def write_string(self, value: str) -> None:
        pass

    # Methods for IdType
    @abc.abstractmethod
    def write_object_id(self, value: IdType.OBJECT_ID) -> None:
        pass

    @abc.abstractmethod
    def write_thread_id(self, value: IdType.THREAD_ID) -> None:
        pass

    @abc.abstractmethod
    def write_thread_group_id(self, value: IdType.THREAD_GROUP_ID) -> None:
        pass

    @abc.abstractmethod
    def write_string_id(self, value: IdType.STRING_ID) -> None:
        pass

    @abc.abstractmethod
    def write_class_loader_id(self, value: IdType.CLASS_LOADER_ID) -> None:
        pass

    @abc.abstractmethod
    def write_class_object_id(self, value: IdType.CLASS_OBJECT_ID) -> None:
        pass

    @abc.abstractmethod
    def write_array_id(self, value: IdType.ARRAY_ID) -> None:
        pass

    @abc.abstractmethod
    def write_reference_type_id(self, value: IdType.REFERENCE_TYPE_ID) -> None:
        pass

    @abc.abstractmethod
    def write_class_id(self, value: IdType.CLASS_ID) -> None:
        pass

    @abc.abstractmethod
    def write_interface_id(self, value: IdType.INTERFACE_ID) -> None:
        pass

    @abc.abstractmethod
    def write_array_type_id(self, value: IdType.ARRAY_TYPE_ID) -> None:
        pass

    @abc.abstractmethod
    def write_method_id(self, value: IdType.METHOD_ID) -> None:
        pass

    @abc.abstractmethod
    def write_field_id(self, value: IdType.FIELD_ID) -> None:
        pass

    @abc.abstractmethod
    def write_frame_id(self, value: IdType.FRAME_ID) -> None:
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
