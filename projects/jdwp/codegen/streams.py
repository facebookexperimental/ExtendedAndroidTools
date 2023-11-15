class OutputStream:
    def __init__(self):
        self.buffer = bytearray()

    def writeInt(self, value: int):
        self.buffer.extend(value.to_bytes(4, byteorder="big"))

    def writeString(self, value: str):
        encoded_string = value.encode("utf-8")
        self.writeInt(len(encoded_string))  # Write string length first
        self.buffer.extend(encoded_string)

    def writeBoolean(self, value: bool):
        self.buffer.append(1 if value else 0)

    def writeByte(self, value: int):
        self.buffer.append(value)


class InputStream:
    def __init__(self, data: bytes):
        self.buffer = data
        self.position = 0

    def readInt(self) -> int:
        value = int.from_bytes(
            self.buffer[self.position : self.position + 4], byteorder="big"
        )
        self.position += 4
        return value

    def readString(self) -> str:
        length = self.readInt()
        start = self.position
        end = self.position + length
        self.position += length
        return self.buffer[start:end].decode("utf-8")

    def readBoolean(self) -> bool:
        value = self.buffer[self.position] != 0
        self.position += 1
        return value

    def readByte(self) -> int:
        value = self.buffer[self.position]
        self.position += 1
        return value
