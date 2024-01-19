"""Command Set: ReferenceType """
        
from projects.jdwp.defs.command_sets.reference_type import Signature


class SignatureCommand:
    @staticmethod
    def serialize(command):
        serialized_data = bytearray()
        serialized_data += command.refType.to_bytes(8, 'big')
        return serialized_data



    @staticmethod
    def deserialize(data):
        command = Signature()
        command.refType = int.from_bytes(data[:8], 'big')
        data = data[8:]
        return command, data

