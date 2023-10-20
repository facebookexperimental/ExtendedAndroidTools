""" JDWP serializer classes. """

class JDWPPacketHeaders:
    def __init__(self, length, id, flags, command_set, command):
        self.length = length
        self.id = id
        self.flags = flags
        self.command_set = command_set
        self.command = command

    def serialize(self):
        length_bytes = self.length.to_bytes(4, byteorder='big')
        id_bytes = self.id.to_bytes(4, byteorder='big')
        flags_bytes = self.flags.to_bytes(1, byteorder='big')
        command_set_bytes = self.command_set.to_bytes(1, byteorder='big')
        command_bytes = self.command.to_bytes(1, byteorder='big')
        return length_bytes + id_bytes + flags_bytes + command_set_bytes + command_bytes


class JDWPPacket:
    def __init__(self, header, payload):
        self.header = header
        self.payload = payload

    def serialize(self):
        header_bytes = self.header.serialize()
        return header_bytes + self.payload

