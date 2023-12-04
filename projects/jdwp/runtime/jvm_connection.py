# Copyright (c) Meta Platforms, Inc. and affiliates.

import asyncio
import typing
import struct
from projects.jdwp.runtime.jdwp_streams import JDWPInputStream, JDWPOutputStream
from projects.jdwp.runtime.jdwpstruct import JDWPStruct


class JVMConnection:
    next_packet_id: int = 0

    def __init__(self, host: str, port: int):
        self.host: str = host
        self.port: int = port
        self.__reader: typing.Optional[asyncio.StreamReader] = None
        self.__writer: typing.Optional[asyncio.StreamWriter] = None
        self.__input_stream: typing.Optional[JDWPInputStream] = None
        self.__output_stream: typing.Optional[JDWPOutputStream] = None

    async def connect(self) -> None:
        try:
            self.__reader, self.__writer = await asyncio.open_connection(
                self.host, self.port
            )
            if self.__writer is None:
                raise Exception("Writer not initialized")
            self.__output_stream = JDWPOutputStream(self.__writer)
        except Exception as e:
            print(f"Error during connection: {e}")
            await self.close()

    async def close(self) -> None:
        for stream in (self.__reader, self.__writer):
            if stream is not None:
                if isinstance(stream, asyncio.streams.StreamWriter):
                    stream.close()
        self.__input_stream, self.__output_stream = None, None

    async def handshake(self) -> None:
        try:
            handshake_bytes = b"JDWP-Handshake"
            if self.__output_stream is not None:
                await self.__output_stream._write_bytes(handshake_bytes)

            if self.__input_stream is not None and hasattr(
                self.__input_stream, "read_packet_data"
            ):
                response_bytes = await self.__input_stream._read_bytes(
                    len(handshake_bytes)
                )

                if response_bytes != handshake_bytes:
                    raise Exception("Invalid handshake response")

                print(f"Handshake successful")
        except Exception as e:
            print(f"Error during handshake: {e}")
            await self.close()

    async def read_packet_header(self) -> typing.Tuple[int, int, bytes, int, int]:
        if self.__input_stream is None:
            raise Exception("Input stream not initialized")
        header_data = await self.__input_stream._read_bytes(10)
        return struct.unpack("!IIcBB", header_data)

    async def read_packet_data(self, length: int) -> bytes:
        if self.__input_stream is None:
            raise Exception("Input stream not initialized")
        return await self.__input_stream._read_bytes(length)

    async def write_packet_header(
        self, length: int, packet_id: int, flags: bytes, command_set: int, command: int
    ) -> None:
        header_data = struct.pack(
            "!IIcBB", length, packet_id, flags, command_set, command
        )
        if self.__output_stream is None:
            raise Exception("Output stream not initialized")
        await self.__output_stream._write_bytes(header_data)

    async def write_packet_data(self, data: bytes) -> None:
        if self.__output_stream is None:
            raise Exception("Output stream not initialized")
        await self.__output_stream._write_bytes(data)

    @staticmethod
    def get_next_packet_id() -> int:
        JVMConnection.next_packet_id += 1
        return JVMConnection.next_packet_id
