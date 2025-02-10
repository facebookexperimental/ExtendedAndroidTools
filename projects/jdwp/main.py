# Copyright (c) Meta Platforms, Inc. and affiliates.

import asyncio
from projects.jdwp.runtime.jvm_connection import JVMConnection


async def main():
    host = "localhost"
    port = 8880

    # connection = JVMConnection(host, port)

    # await connection.connect()

    # await connection.handshake()

    # await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
