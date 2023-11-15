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
        case PrimitiveType.CLASS_LOADER:
            return f"out.writeClassLoader(self.{field.name})"
        case PrimitiveType.FIELD_ID:
            return f"out.writeFieldId(self.{field.name})"
        case PrimitiveType.METHOD_ID:
            return f"out.writeMethodId(self.{field.name})"
        case PrimitiveType.VALUE:
            return f"out.writeValue(self.{field.name})"
        case PrimitiveType.INTERFACE_ID:
            return f"out.writeInterfaceId(self.{field.name})"
        case PrimitiveType.CLASS_OBJECT_ID:
            return f"out.writeClassObjectId(self.{field.name})"
        case PrimitiveType.TAGGED_OBJECT_ID:
            return f"out.writeTaggedObjectId(self.{field.name})"
        case PrimitiveType.THREAD_ID:
            return f"out.writeThreadId(self.{field.name})"
        case PrimitiveType.THREAD_GROUP_ID:
            return f"out.writeThreadGroupId(self.{field.name})"
        case PrimitiveType.OBJECT_ID:
            return f"out.writeObjectId(self.{field.name})"
        case PrimitiveType.LOCATION:
            return f"out.writeLocation(self.{field.name})"
        case _:
            raise Exception(f"Unrecognized type: {field.type}")
