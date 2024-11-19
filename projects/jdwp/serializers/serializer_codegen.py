import re
import os
from projects.jdwp.defs.schema import Type, Struct, CommandSet, Command, Field
from projects.jdwp.defs.command_sets.reference_type import ReferenceType


class CommandSerializerGenerator:
    def __init__(self):
        self.serializer_code: str = ""

    def generate_field_serializer(self, field: Field) -> str:
        serializer_code: str = ""
        if isinstance(field, Struct):
            for subfield in field.fields:
                serializer_code += self.generate_field_serializer(subfield)
        elif field.type == Type.INT:
            serializer_code = (
                f"        serialized_data += command.{field.name}.to_bytes(4, 'big')"
            )
        elif field.type == Type.STRING:
            serializer_code = (
                f"        serialized_data += command.{field.name}.encode('utf-8')"
            )
        elif field.type == Type.OBJECT_ID:
            serializer_code = (
                f"        serialized_data += command.{field.name}.to_bytes(8, 'big')"
            )
        elif field.type == Type.REFERENCE_TYPE_ID:
            serializer_code = (
                f"        serialized_data += command.{field.name}.to_bytes(8, 'big')"
            )
        return serializer_code

    def generate_field_deserializer(self, field: Field) -> str:
        deserializer_code: str = ""
        if isinstance(field, Struct):
            for subfield in field.fields:
                deserializer_code += self.generate_field_deserializer(subfield)
        elif field.type == Type.INT:
            deserializer_code = f"        command.{field.name} = int.from_bytes(data[:4], 'big')\n        data = data[4:]"
        elif field.type == Type.STRING:
            deserializer_code = f"        null_terminator = data.index(0)\n        command.{field.name} = data[:null_terminator].decode('utf-8')\n\t\tdata = data[null_terminator + 1:]"
        elif field.type == Type.OBJECT_ID:
            deserializer_code = f"        command.{field.name} = int.from_bytes(data[:8], 'big')\n        data = data[8:]"
        elif field.type == Type.REFERENCE_TYPE_ID:
            deserializer_code = f"        command.{field.name} = int.from_bytes(data[:8], 'big')\n        data = data[8:]"
        return deserializer_code

    def generate_command_serializer(self, command: Command) -> str:
        serializer_code: str = f"""
class {command.name}Command:
    @staticmethod
    def serialize(command):
        serialized_data = bytearray()
{self.generate_field_serializer(command.out)}
        return serialized_data
"""
        return serializer_code

    def generate_command_deserializer(self, command: Command) -> str:
        deserializer_code: str = f"""
    @staticmethod
    def deserialize(data):
        command = {command.name}()
{"".join(self.generate_field_deserializer(field) for field in command.out.fields)}
        return command, data
"""
        return deserializer_code

    def _convert_to_snake_case(self, name: str) -> str:
        name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()
        return name

    def generate_command_set_file(self, command_set: CommandSet) -> str:
        self.serializer_code = f"""\"\"\"Command Set: {command_set.name} \"\"\"
        
from projects.jdwp.defs.command_sets.{self._convert_to_snake_case(command_set.name)} import {", ".join([command.name for command in command_set.commands])}

{"".join(self.generate_command_serializer(command) for command in command_set.commands)}

{"".join(self.generate_command_deserializer(command) for command in command_set.commands)}
"""
        return self.serializer_code

    def generate_serializer_file(self, command_set: CommandSet) -> None:
        command_set_name = command_set.name
        serializer_file_name: str = (
            f"{self._convert_to_snake_case(command_set_name)}_serializer.py"
        )
        command_set_code: str = self.generate_command_set_file(command_set)
        output_dir: str = os.path.dirname(os.path.realpath(__file__))
        file_path: str = os.path.join(output_dir, serializer_file_name)
        with open(file_path, "w") as output_file:
            output_file.write(command_set_code)
        print(f"Generated serializer code saved to {serializer_file_name}")


serializer_generator = CommandSerializerGenerator()
gen_file = serializer_generator.generate_serializer_file(ReferenceType)
