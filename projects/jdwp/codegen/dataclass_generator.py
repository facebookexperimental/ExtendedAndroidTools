# Copyright (c) Meta Platforms, Inc. and affiliates.

from textwrap import dedent
from projects.jdwp.codegen.types import python_type_for
import typing

from projects.jdwp.defs.schema import (
    Array,
    Field,
    Struct,
    TaggedUnion,
)


StructLink = typing.Tuple[Struct, Field, Struct]


class StructGenerator:
    def __init__(self, root: Struct, name: str):
        self.__root = root
        self.__struct_to_name = compute_struct_names(root, name)

    def __get_python_type_for(self, struct: Struct, field: Field) -> str:
        type = field.type
        match type:
            case Struct():
                return self.__struct_to_name[type]
            case Array():
                return f"typing.List[{self.__struct_to_name[typing.cast(Array, type).element_type]}]"
            case TaggedUnion():
                union_types = [
                    self.__struct_to_name[case_struct]
                    for case_struct in typing.cast(TaggedUnion, type).cases.values()
                ]
                union_types_str = ", ".join(union_types)
                return f"typing.Union[{union_types_str}]"
            case _:
                return python_type_for(type)

    def __generate_dataclass(self, struct: Struct) -> str:
        name = self.__struct_to_name[struct]
        fields_def = "\n".join(
            f"    {field.name}: {self.__get_python_type_for(struct, field)}"
            for field in struct.fields
        )
        class_def = f"@dataclasses.dataclass(frozen=True)\nclass {name}:\n{fields_def}"
        return dedent(class_def)

    def generate(self):
        return [
            self.__generate_dataclass(nested)
            for _, _, nested in reversed(list(nested_structs(self.__root)))
        ] + [self.__generate_dataclass(self.__root)]


def format_enum_name(enum_value):
    words = enum_value.name.split("_")
    formatted_name = "".join(word.capitalize() for word in words)
    return f"{formatted_name}Type"


def nested_structs(root: Struct) -> typing.Generator[StructLink, None, None]:
    for field in root.fields:
        type = field.type
        match type:
            case Array():
                yield root, field, type.element_type
                yield from nested_structs(typing.cast(Array, type).element_type)
            case TaggedUnion():
                for struct in typing.cast(TaggedUnion, type).cases.values():
                    yield root, field, struct
                    yield from nested_structs(struct)
            case Struct():
                yield root, field, type
                yield from nested_structs(type)


def compute_struct_names(root: Struct, name: str) -> typing.Mapping[Struct, str]:
    names = {root: name}
    for parent, field, nested in nested_structs(root):
        type = field.type
        match type:
            case Struct():
                names[nested] = f"{names[parent]}{field.name.capitalize()}"
            case Array():
                names[nested] = f"{names[parent]}{field.name.capitalize()}Element"
            case TaggedUnion():
                for case_value, case_struct in field.type.cases.items():
                    case_name = format_enum_name(case_value)
                    names[
                        case_struct
                    ] = f"{names[parent]}{field.name.capitalize()}Case{case_name}"
    return names
