# Copyright (c) Meta Platforms, Inc. and affiliates.

import abc
import typing

from projects.jdwp.runtime.type_aliases import *


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
    async def read_object_id(self) -> ObjectIDType:
        pass

    @abc.abstractmethod
    async def read_thread_id(self) -> ThreadIDType:
        pass

    @abc.abstractmethod
    async def read_thread_group_id(self) -> ThreadGroupIDType:
        pass

    @abc.abstractmethod
    async def read_string_id(self) -> StringIDType:
        pass

    @abc.abstractmethod
    async def read_class_loader_id(self) -> ClassLoaderIDType:
        pass

    @abc.abstractmethod
    async def read_class_object_id(self) -> ClassObjectIDType:
        pass

    @abc.abstractmethod
    async def read_array_id(self) -> ArrayIDType:
        pass

    @abc.abstractmethod
    async def read_reference_type_id(self) -> ReferenceTypeIDType:
        pass

    @abc.abstractmethod
    async def read_class_id(self) -> ClassIDType:
        pass

    @abc.abstractmethod
    async def read_interface_id(self) -> InterfaceIDType:
        pass

    @abc.abstractmethod
    async def read_array_type_id(self) -> ArrayTypeIDType:
        pass

    @abc.abstractmethod
    async def read_method_id(self) -> MethodIDType:
        pass

    @abc.abstractmethod
    async def read_field_id(self) -> FieldIDType:
        pass

    @abc.abstractmethod
    async def read_frame_id(self) -> FrameIDType:
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
    def write_object_id(self, value: ObjectIDType) -> None:
        pass

    @abc.abstractmethod
    def write_thread_id(self, value: ThreadIDType) -> None:
        pass

    @abc.abstractmethod
    def write_thread_group_id(self, value: ThreadGroupIDType) -> None:
        pass

    @abc.abstractmethod
    def write_string_id(self, value: StringIDType) -> None:
        pass

    @abc.abstractmethod
    def write_class_loader_id(self, value: ClassLoaderIDType) -> None:
        pass

    @abc.abstractmethod
    def write_class_object_id(self, value: ClassObjectIDType) -> None:
        pass

    @abc.abstractmethod
    def write_array_id(self, value: ArrayIDType) -> None:
        pass

    @abc.abstractmethod
    def write_reference_type_id(self, value: ReferenceTypeIDType) -> None:
        pass

    @abc.abstractmethod
    def write_class_id(self, value: ClassIDType) -> None:
        pass

    @abc.abstractmethod
    def write_interface_id(self, value: InterfaceIDType) -> None:
        pass

    @abc.abstractmethod
    def write_array_type_id(self, value: ArrayTypeIDType) -> None:
        pass

    @abc.abstractmethod
    def write_method_id(self, value: MethodIDType) -> None:
        pass

    @abc.abstractmethod
    def write_field_id(self, value: FieldIDType) -> None:
        pass

    @abc.abstractmethod
    def write_frame_id(self, value: FrameIDType) -> None:
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
