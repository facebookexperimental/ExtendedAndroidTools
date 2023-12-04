# Copyright (c) Meta Platforms, Inc. and affiliates.

import struct
import typing
import asyncio
from projects.jdwp.defs.schema import IdType
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
        return await self._read_id(IdType.OBJECT_ID)

    async def read_thread_id(self) -> ThreadIDType:
        return await self._read_id(IdType.THREAD_ID)

    async def read_thread_group_id(self) -> ThreadGroupIDType:
        return await self._read_id(IdType.THREAD_GROUP_ID)

    async def read_string_id(self) -> StringIDType:
        return await self._read_id(IdType.STRING_ID)

    async def read_class_loader_id(self) -> ClassLoaderIDType:
        return await self._read_id(IdType.CLASS_LOADER_ID)

    async def read_class_object_id(self) -> ClassObjectIDType:
        return await self._read_id(IdType.CLASS_OBJECT_ID)

    async def read_array_id(self) -> ArrayIDType:
        return await self._read_id(IdType.ARRAY_ID)

    async def read_reference_type_id(self) -> ReferenceTypeIDType:
        return await self._read_id(IdType.REFERENCE_TYPE_ID)

    async def read_class_id(self) -> ClassIDType:
        return await self._read_id(IdType.CLASS_ID)

    async def read_interface_id(self) -> InterfaceIDType:
        return await self._read_id(IdType.INTERFACE_ID)

    async def read_array_type_id(self) -> ArrayTypeIDType:
        return await self._read_id(IdType.ARRAY_TYPE_ID)

    async def read_method_id(self) -> MethodIDType:
        return await self._read_id(IdType.METHOD_ID)

    async def read_field_id(self) -> FieldIDType:
        return await self._read_id(IdType.FIELD_ID)

    async def read_frame_id(self) -> FrameIDType:
        return await self._read_id(IdType.FRAME_ID)

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

    async def _read_id(self, id_type: IdType) -> typing.Any:
        pass


class JDWPOutputStream(JDWPOutputStreamBase):
    __tcp_connection: asyncio.StreamWriter

    def __init__(self, socket_connection: asyncio.StreamWriter):
        super().__init__()
        self.__tcp_connection = socket_connection

    async def write_boolean(self, value: bool) -> None:
        await self._write_bytes(struct.pack("!B", int(value)))

    async def write_int(self, value: int) -> None:
        await self._write_bytes(struct.pack("!I", value))

    async def write_array_id(self, value: ArrayIDType) -> None:
        await self._write_id(value)

    async def write_array_type_id(self, value: ArrayTypeIDType) -> None:
        await self._write_id(value)

    async def write_byte(self, value: int) -> None:
        await self._write_bytes(struct.pack("!B", value))

    async def write_class_id(self, value: ClassIDType) -> None:
        await self._write_id(value)

    async def write_class_loader_id(self, value: ClassLoaderIDType) -> None:
        await self._write_id(value)

    async def write_class_object_id(self, value: ClassObjectIDType) -> None:
        await self._write_id(value)

    async def write_field_id(self, value: FieldIDType) -> None:
        await self._write_id(value)

    async def write_frame_id(self, value: FrameIDType) -> None:
        await self._write_id(value)

    async def write_interface_id(self, value: InterfaceIDType) -> None:
        await self._write_id(value)

    async def write_location(self, value: typing.Any) -> None:
        pass

    async def write_method_id(self, value: MethodIDType) -> None:
        await self._write_id(value)

    async def write_string_id(self, value: StringIDType) -> None:
        await self._write_id(value)

    async def write_thread_group_id(self, value: ThreadGroupIDType) -> None:
        await self._write_id(value)

    async def write_long(self, value: int) -> None:
        await self._write_bytes(struct.pack("!Q", value))

    async def write_object_id(self, value: typing.Any) -> None:
        await self._write_id(value)

    async def write_thread_id(self, value: typing.Any) -> None:
        await self._write_id(value)

    async def write_string(self, value: str) -> None:
        value_bytes = value.encode("utf-8")
        length = len(value_bytes)

        await self.write_int(length)

        await self._write_bytes(value_bytes)

    async def write_reference_type_id(self, value: ReferenceTypeIDType) -> None:
        await self._write_id(value)

    async def _write_bytes(self, data: bytes) -> None:
        try:
            self.__tcp_connection.write(data)
            await self.__tcp_connection.drain()
        except Exception as e:
            print(f"Error during data sending: {e}")
            await self.__tcp_connection.drain()

    async def _write_id(self, value: typing.Any) -> None:
        size = min(value.bit_length() // 8 + 1, 8)
        await self._write_bytes(struct.pack("B", size))
        await self._write_bytes(value.to_bytes(size, byteorder="big"))
