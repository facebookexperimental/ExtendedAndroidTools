from projects.jdwp.defs.schema import Command, Field, PrimitiveType


def generate_deserialization_function(command: Command) -> str:
    func_code = (
        f"def deserialize_{command.name.lower()}_response(self, inp: InputStream):\n"
    )
    constructor_args = []

    for field in command.reply.fields:
        deserialization_code = generate_field_deserialization(field)
        func_code += f"    {deserialization_code}\n"
        constructor_args.append(f"{field.name}={field.name}")

    constructor_call = (
        f"    return {command.name}Response({', '.join(constructor_args)})\n"
    )
    func_code += constructor_call
    return func_code


def generate_field_deserialization(field: Field):
    match field.type:
        case PrimitiveType.INT:
            return f"{field.name} = inp.readInt()"
        case PrimitiveType.STRING:
            return f"{field.name} = inp.readString()"
        case PrimitiveType.BOOLEAN:
            return f"{field.name} = inp.readBoolean()"
        case PrimitiveType.BYTE:
            return f"{field.name} = inp.readByte()"
        case PrimitiveType.REFERENCE_TYPE_ID:
            return f"{field.name} = inp.readReferenceTypeId()"
        case _:
            raise Exception(f"Unrecognized type: {field.type}")
