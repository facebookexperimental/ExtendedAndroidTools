from textwrap import dedent

from projects.jdwp.defs.schema import (
    Array,
    ArrayLength,
    Command,
    IdType,
    IntegralType,
    Struct,
    TaggedUnion,
    UnionTag,
)


def format_enum_name(enum_value):
    words = enum_value.name.split("_")
    formatted_name = "".join(word.capitalize() for word in words)
    return f"{formatted_name}Type"


def map_id_type(id_type: IdType):
    match id_type:
        case IdType.OBJECT_ID:
            return "ObjectIdType"
        case IdType.THREAD_ID:
            return "ThreadIdType"
        case IdType.THREAD_GROUP_ID:
            return "ThreadGroupIdType"
        case IdType.STRING_ID:
            return "StringIdType"
        case IdType.CLASS_LOADER_ID:
            return "ClassLoaderIdType"
        case IdType.CLASS_OBJECT_ID:
            return "ClassObjectIdType"
        case IdType.ARRAY_ID:
            return "ArrayIdType"
        case IdType.REFERENCE_TYPE_ID:
            return "ReferenceTypeIdType"
        case IdType.CLASS_ID:
            return "ClassIdType"
        case IdType.INTERFACE_ID:
            return "InterfaceIdType"
        case IdType.ARRAY_TYPE_ID:
            return "ArrayTypeIdType"
        case IdType.METHOD_ID:
            return "MethodIdType"
        case IdType.FIELD_ID:
            return "FieldIdType"
        case IdType.FRAME_ID:
            return "FrameIdType"
        case _:
            return f"Unrecognized type: {id_type}"


def get_python_type_for_field(field_type, parent_struct_name="", field_name=""):
    if isinstance(field_type, IdType):
        return map_id_type(field_type)
    elif (
        isinstance(field_type, IntegralType)
        or isinstance(field_type, ArrayLength)
        or isinstance(field_type, UnionTag)
    ):
        return "int"
    elif isinstance(field_type, Array):
        element_type = get_python_type_for_field(
            field_type.element_type, parent_struct_name, field_name + "Element"
        )
        return f"List[{element_type}]"
    elif isinstance(field_type, TaggedUnion):
        union_types = [
            f"{parent_struct_name}{field_name}Case{format_enum_name(case)}"
            for case in field_type.cases.keys()
        ]
        union_types_str = ", ".join(union_types)
        return f"typing.Union[{union_types_str}]"
    elif isinstance(field_type, Struct):
        nested_struct_name = (
            f"{parent_struct_name}{field_name}"
            if parent_struct_name and field_name
            else "NestedStruct"
        )
        return nested_struct_name
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
    fields_def = "\n".join(
        f"    {field.name}: {get_python_type_for_field(field.type, class_name, field.name)}"
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
