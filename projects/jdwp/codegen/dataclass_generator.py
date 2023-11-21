from textwrap import dedent

from projects.jdwp.defs.schema import (
    Array,
    ArrayLength,
    Command,
    IntegralType,
    PrimitiveType,
    Struct,
    TaggedUnion,
)


def map_primitive_type(primitive_type):
    match primitive_type:
        case PrimitiveType.STRING:
            return "str"
        case PrimitiveType.BOOLEAN:
            return "bool"
        case PrimitiveType.REFERENCE_TYPE_ID:
            return "ReferenceTypeId"
        case PrimitiveType.CLASS_LOADER:
            return "ClassLoaderId"
        case PrimitiveType.FIELD_ID:
            return "FieldId"
        case PrimitiveType.METHOD_ID:
            return "MethodId"
        case PrimitiveType.VALUE:
            return "Value"
        case PrimitiveType.INTERFACE_ID:
            return "InterfaceId"
        case PrimitiveType.CLASS_OBJECT_ID:
            return "ClassObjectId"
        case PrimitiveType.TAGGED_OBJECT_ID:
            return "TaggedObjectId"
        case PrimitiveType.THREAD_ID:
            return "ThreadId"
        case PrimitiveType.THREAD_GROUP_ID:
            return "ThreadGroupId"
        case PrimitiveType.OBJECT_ID:
            return "ObjectId"
        case PrimitiveType.LOCATION:
            return "Location"
        case _:
            return f"Unrecognized type: {primitive_type}"


def get_python_type_for_field(field_type):
    if isinstance(field_type, PrimitiveType):
        return map_primitive_type(field_type)
    elif isinstance(field_type, IntegralType) or isinstance(field_type, ArrayLength):
        return "int"
    elif isinstance(field_type, Array):
        element_type = get_python_type_for_field(field_type.element_type)
        return f"List[{element_type}]"
    elif isinstance(field_type, TaggedUnion):
        pass
    elif isinstance(field_type, Struct):
        return "NestedStruct"
    else:
        raise Exception(f"Unrecognized type: {field_type}")


def generate_dataclass_for_command(command: Command) -> str:
    """Generates a dataclass definition for a given command."""
    out_class = (
        generate_dataclass_for_struct(command.out, f"{command.name}Command")
        if command.out
        else ""
    )

    reply_class = (
        generate_dataclass_for_struct(command.reply, f"{command.name}Response")
        if command.reply
        else ""
    )

    return out_class + "\n" + reply_class


def generate_dataclass_for_struct(struct: Struct, class_name: str) -> str:
    """Generates a dataclass definition for a given struct."""
    fields_def = "\n".join(
        f"    {field.name}: {get_python_type_for_field(field.type)}"
        for field in struct.fields
    )
    class_def = dedent(
        f"""
    @dataclasses.dataclass(frozen=True)
    class {class_name}:
{fields_def}
    """
    )
    return class_def
