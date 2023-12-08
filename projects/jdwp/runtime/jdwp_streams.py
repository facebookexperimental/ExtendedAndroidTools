# Copyright (c) Meta Platforms, Inc. and affiliates.

import struct
import typing
import asyncio
from projects.jdwp.runtime.type_aliases import *
from projects.jdwp.runtime.async_streams import (
    JDWPInputStreamBase,
    JDWPOutputStreamBase,
)


class JDWPInputStream(JDWPInputStreamBase):
    __tcp_connection: asyncio.StreamReader

    def __init__(self, stream_reader: asyncio.StreamReader):
        super().__init__()
        self.__tcp_connection = stream_reader

    async def read_boolean(self) -> bool:
        data = await self._read_bytes(1)
        return bool(data[0])

    async def read_location(self) -> typing.Any:
        pass

    async def read_string(self) -> str:
        length = await self.read_int()
        string_data = await self._read_bytes(length)
        return string_data.decode("utf-8")

    async def read_object_id(self) -> ObjectIDType:
        return ObjectIDType(0)

    async def read_thread_id(self) -> ThreadIDType:
        return ThreadIDType(0)

    async def read_thread_group_id(self) -> ThreadGroupIDType:
        return ThreadGroupIDType(0)

    async def read_string_id(self) -> StringIDType:
        return StringIDType(0)

    async def read_class_loader_id(self) -> ClassLoaderIDType:
        return ClassLoaderIDType(0)

    async def read_class_object_id(self) -> ClassObjectIDType:
        return ClassObjectIDType(0)

    async def read_array_id(self) -> ArrayIDType:
        return ArrayIDType(0)

    async def read_reference_type_id(self) -> ReferenceTypeIDType:
        return ReferenceTypeIDType(0)

    async def read_class_id(self) -> ClassIDType:
        return ClassIDType(0)

    async def read_interface_id(self) -> InterfaceIDType:
        return InterfaceIDType(0)

    async def read_array_type_id(self) -> ArrayTypeIDType:
        return ArrayTypeIDType(0)

    async def read_method_id(self) -> MethodIDType:
        return MethodIDType(0)

    async def read_field_id(self) -> FieldIDType:
        return FieldIDType(0)

    async def read_frame_id(self) -> FrameIDType:
        return FrameIDType(0)

    async def read_byte(self) -> int:
        data = await self._read_bytes(1)
        return int.from_bytes(data, byteorder="big")

    async def read_int(self) -> int:
        data = await self._read_bytes(4)
        return struct.unpack("!I", data)[0]

    async def read_long(self) -> int:
        data = await self._read_bytes(8)
        return struct.unpack("!Q", data)[0]

    async def _read_bytes(self, size: int) -> bytes:
        try:
            return await self.__tcp_connection.readexactly(size)
        except Exception as e:
            print(f"Error during data receiving: {e}")
            return b""


class JDWPOutputStream(JDWPOutputStreamBase):
    __tcp_connection: asyncio.StreamWriter

    def __init__(self, socket_connection: asyncio.StreamWriter):
        super().__init__()
        self.__tcp_connection = socket_connection
        self.__buffer = JDWPBufferOutputStream()

    def write_boolean(self, value: bool) -> None:
        self._write_bytes(struct.pack("!B", int(value)))

    def write_int(self, value: int) -> None:
        self._write_bytes(struct.pack("!I", value))

    def write_array_id(self, value: ArrayIDType) -> None:
        self._write_id(value)

    def write_array_type_id(self, value: ArrayTypeIDType) -> None:
        self._write_id(value)

    def write_byte(self, value: int) -> None:
        self._write_bytes(struct.pack("!B", value))

    def write_class_id(self, value: ClassIDType) -> None:
        self._write_id(value)

    def write_class_loader_id(self, value: ClassLoaderIDType) -> None:
        self._write_id(value)

    def write_class_object_id(self, value: ClassObjectIDType) -> None:
        self._write_id(value)

    def write_field_id(self, value: FieldIDType) -> None:
        self._write_id(value)

    def write_frame_id(self, value: FrameIDType) -> None:
        self._write_id(value)

    def write_interface_id(self, value: InterfaceIDType) -> None:
        self._write_id(value)

    def write_location(self, value: typing.Any) -> None:
        pass

    def write_method_id(self, value: MethodIDType) -> None:
        self._write_id(value)

    def write_string_id(self, value: StringIDType) -> None:
        self._write_id(value)

    def write_thread_group_id(self, value: ThreadGroupIDType) -> None:
        self._write_id(value)

    def write_long(self, value: int) -> None:
        self._write_bytes(struct.pack("!Q", value))

    def write_object_id(self, value: typing.Any) -> None:
        self._write_id(value)

    def write_thread_id(self, value: typing.Any) -> None:
        self._write_id(value)

    def write_string(self, value: str) -> None:
        value_bytes = value.encode("utf-8")
        length = len(value_bytes)

        self.write_int(length)

        self._write_bytes(value_bytes)

    def write_reference_type_id(self, value: ReferenceTypeIDType) -> None:
        self._write_id(value)

    def _write_bytes(self, data: bytes):
        self.__buffer.write(data)

    def buffered_data(self):
        message_size = self.__buffer.get_buffer_size()
        header_bytes = struct.pack("!I", message_size)
        return header_bytes + self.__buffer.get_buffer()

    def _write_id(self, value: typing.Any) -> None:
        self._write_bytes(struct.pack("B", value))
        self._write_bytes(value.to_bytes(value, byteorder="big"))


class JDWPBufferOutputStream:
    def __init__(self):
        self.__buffer = bytes()
        self.__size = 0

    def write(self, data: bytes) -> None:
        self.__buffer += data
        self.__size += len(data)

    def get_buffer(self) -> bytes:
        return self.__buffer

    def get_buffer_size(self) -> int:
        return self.__size

    def clear(self) -> None:
        self.__buffer = bytes()
        self.__size = 0
