import asyncio


class AsyncInputStream:
    def __init__(self, reader: asyncio.StreamReader):
        self.reader = reader

    async def read(self, n: int = -1) -> bytes:
        """
        Asynchronously read n bytes from the stream.
        If n is -1 (default), read until EOF.
        """
        return await self.reader.read(n)

    async def readexactly(self, n: int) -> bytes:
        """
        Asynchronously read exactly n bytes from the stream.
        """
        return await self.reader.readexactly(n)

    async def readline(self) -> bytes:
        """
        Asynchronously read one line, where “line” is a sequence of bytes ending with \n.
        """
        return await self.reader.readline()


class AsyncOutputStream:
    def __init__(self, writer: asyncio.StreamWriter):
        self.writer = writer

    async def write(self, data: bytes) -> None:
        """
        Asynchronously write data to the stream.
        """
        self.writer.write(data)
        await self.writer.drain()

    async def close(self):
        """
        Close the stream.
        """
        self.writer.close()
        await self.writer.wait_closed()
