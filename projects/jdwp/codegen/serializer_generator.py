from projects.jdwp.defs.schema import Command, Field, PrimitiveType


def generate_serialization_function(command: Command) -> str:
    func_code = (
        f"def serialize_{command.name.lower()}_command(self, out: OutputStream):\n"
    )
    for field in command.out.fields:
        serialization_code = generate_field_serialization(field)
        func_code += f"    {serialization_code}\n"
    return func_code


def generate_field_serialization(field: Field):
    match field.type:
        case PrimitiveType.INT:
            return f"out.writeInt(self.{field.name})"
        case PrimitiveType.STRING:
            return f"out.writeString(self.{field.name})"
        case PrimitiveType.BOOLEAN:
            return f"out.writeBoolean(self.{field.name})"
        case PrimitiveType.BYTE:
            return f"out.writeByte(self.{field.name})"
        case PrimitiveType.REFERENCE_TYPE_ID:
            return f"out.writeReferenceTypeId(self.{field.name})"
        case _:
            raise Exception(f"Unrecognized type: {field.type}")
