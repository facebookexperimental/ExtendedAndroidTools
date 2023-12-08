# Copyright (c) Meta Platforms, Inc. and affiliates.

import asyncio
import typing
import struct
from projects.jdwp.runtime.jdwp_streams import JDWPInputStream, JDWPOutputStream


class PacketHeader(typing.NamedTuple):
    length: int
    id: int
    flags: bytes
    command_set: int
    command: int

    def write(self) -> bytes:
        return struct.pack(
            "!IIcBB", self.length, self.id, self.flags, self.command_set, self.command
        )


class JVMConnection:
    def __init__(self, host: str, port: int):
        self.host: str = host
        self.port: int = port
        self.next_packet_id: int = 0
        self.__reader: typing.Optional[asyncio.StreamReader] = None
        self.__writer: typing.Optional[asyncio.StreamWriter] = None
        self.__input_stream: typing.Optional[JDWPInputStream] = None
        self.__output_stream: typing.Optional[JDWPOutputStream] = None

    async def connect(self) -> None:
        try:
            self.__reader, self.__writer = await asyncio.open_connection(
                self.host, self.port
            )

            self.__output_stream = JDWPOutputStream(self.__writer)

            if self.__reader is None:
                raise Exception("Reader not initialized")
            self.__input_stream = JDWPInputStream(self.__reader)

        except Exception as e:
            print(f"Error during connection: {e}")
            exit(1)

    def close(self) -> None:
        if self.__writer is not None:
            self.__writer.close()
        self.__input_stream, self.__output_stream = None, None

    async def handshake(self) -> None:
        try:
            handshake_bytes = b"JDWP-Handshake"
            if self.__output_stream is None:
                raise Exception("Output stream not initialized")
            await self.__output_stream._write_bytes(handshake_bytes)

            if self.__input_stream is None:
                raise Exception("Input stream not initialized")
            response_bytes = await self.__input_stream._read_bytes(len(handshake_bytes))

            if response_bytes != handshake_bytes:
                raise Exception("Invalid handshake response")

            print(f"Handshake successful")
        except Exception as e:
            print(f"Error during handshake: {e}")
            self.close()

    async def __read_packet_header(self) -> PacketHeader:
        if self.__input_stream is None:
            raise Exception("Input stream not initialized")

        header_data = await self.__input_stream._read_bytes(10)
        return PacketHeader(*struct.unpack("!IIcBB", header_data))

    async def __read_packet_data(self, length: int) -> bytes:
        if self.__input_stream is None:
            raise Exception("Input stream not initialized")
        return await self.__input_stream._read_bytes(length)

    async def __write_packet_header(
        self, length: int, flags: bytes, command_set: int, command: int
    ) -> None:
        try:
            packet_id = self.__get_next_packet_id()
            packet_header = PacketHeader(length, packet_id, flags, command_set, command)
            header_data = packet_header.write()
            if self.__output_stream is None:
                raise Exception("Output stream not initialized")
            await self.__output_stream._write_bytes(header_data)

        except Exception as e:
            print(f"Error writing packet header: {e}")
            self.close()

    async def __write_packet_data(self, data: bytes) -> None:
        if self.__output_stream is None:
            raise Exception("Output stream not initialized")
        await self.__output_stream._write_bytes(data)

    def __get_next_packet_id(self) -> int:
        self.next_packet_id += 1
        return self.next_packet_id
