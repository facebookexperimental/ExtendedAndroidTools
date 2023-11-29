# Copyright (c) Meta Platforms, Inc. and affiliates.

from textwrap import dedent
from projects.jdwp.codegen.types import python_type_for

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


def get_python_type_for_field(field_type, parent_struct_name="", field_name=""):
    if isinstance(field_type, IdType):
        return python_type_for(field_type)
    elif isinstance(field_type, IntegralType):
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
    elif isinstance(field_type, (ArrayLength, UnionTag)):
        return None
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
    dataclass_definitions = []
    fields_def = []

    for field in struct.fields:
        if isinstance(field.type, Struct):
            nested_class_name = f"{class_name}{field.name.capitalize()}"
            nested_class_def = generate_dataclass_for_struct(
                field.type, nested_class_name
            )
            dataclass_definitions.append(nested_class_def)
            field_type = nested_class_name
        else:
            field_type = get_python_type_for_field(field.type, class_name, field.name)

        fields_def.append(f"    {field.name}: {field_type}")

    class_def = (
        "@dataclasses.dataclass(frozen=True)\n"
        + f"class {class_name}:\n"
        + "\n".join(fields_def)
    )

    dataclass_definitions.append(dedent(class_def))

    return "\n\n".join(dataclass_definitions)
