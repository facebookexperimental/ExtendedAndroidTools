# Copyright (c) Meta Platforms, Inc. and affiliates.

import enum
from textwrap import dedent
from projects.jdwp.codegen.types import python_type_for
import typing

from projects.jdwp.defs.schema import (
    Array,
    ArrayLength,
    Command,
    CommandSet,
    Field,
    Struct,
    TaggedUnion,
    UnionTag,
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
                array_type = typing.cast(Array, type)
                if isinstance(array_type.element_type, Struct):
                    return (
                        f"typing.List[{self.__struct_to_name[array_type.element_type]}]"
                    )
                else:
                    return f"typing.List[{python_type_for(array_type.element_type)}]"
            case TaggedUnion():
                tagged_union_type = typing.cast(TaggedUnion, type)
                union_types = [
                    self.__struct_to_name[case_struct]
                    for (_, case_struct) in tagged_union_type.cases
                ]
                union_types_str = ", ".join(union_types)
                return f"typing.Union[{union_types_str}]"
            case _:
                return python_type_for(type)

    def __get_element_struct_name(self, field: Field) -> str:
        element_type = field.type.element_type
        return self.__struct_to_name[element_type]

    def __is_explicit_field(self, field: Field) -> bool:
        return not isinstance(field.type, (ArrayLength, UnionTag))

    def __get_field_name(self, field: Field) -> str:
        words = field.name.split(" ")
        words = [words[0]] + [word.capitalize() for word in words[1:]]
        return "".join(words)

    def __generate_dataclass(self, struct: Struct) -> str:
        name = self.__struct_to_name[struct]
        fields_def = "\n".join(
            f"    {self.__get_field_name(field)}: {self.__get_python_type_for(struct, field)}"
            for field in struct.fields
            if self.__is_explicit_field(field)
        )

        class_def = f"@dataclasses.dataclass(frozen=True)\nclass {name}:\n{fields_def}"
        class_def += "\n\n" + self.__generate_serialize_method(struct)
        class_def += "\n\n" + self.__generate_parse_method(struct)

        return dedent(class_def)

    def __generate_serialize_method(self, struct: Struct) -> str:
        serialize_code = "def serialize(self, output: JDWPOutputStreamBase):\n"
        for field in struct.fields:
            serialize_code += f"    {self.__generate_serialize_field_code(field)}\n"
        return dedent(serialize_code)

    def __generate_serialize_array_code(self, field: Field) -> str:
        array_length_field_type = field.type.length
        array_code = (
            f"output.write_{array_length_field_type.lower()}(len(self.{field.name}))\n"
            f"for element in self.{field.name}:\n"
            f"    element.serialize(output)\n"
        )
        return dedent(array_code)

    def __generate_serialize_tagged_union_code(
        self, field: Field, union: TaggedUnion
    ) -> str:
        union_code = "match self.{0}:\n".format(field.name)
        for enum_val, struct_type in union.cases:
            union_code += f"    case {struct_type.__name__}():\n"
            union_code += f"        output.write_{union.tag.type.name.lower()}({enum_val.value})\n"
            union_code += f"        self.{field.name}.serialize(output)\n"
        return dedent(union_code)

    def __generate_serialize_field_code(self, field: Field) -> str:
        match field.type:
            case Array():
                return self.__generate_serialize_array_code(field)
            case TaggedUnion():
                return self.__generate_serialize_tagged_union_code(field)
            case _:
                return f"output.write_{field.type.name.lower()}(self.{field.name})"

    def __generate_parse_method(self, struct: Struct) -> str:
        struct_name = self.__struct_to_name[struct]
        parse_code = f"@staticmethod\nasync def parse(input: JDWPInputStreamBase) -> {struct_name}:\n"

        for field in struct.fields:
            parse_code += (
                f"    {field.name} = {self.__generate_parse_field_code(field)}\n"
            )

        parse_code += f"    return {struct_name}(\n"
        for field in struct.fields:
            parse_code += f"        {field.name}={field.name},\n"
        parse_code += "    )"
        return dedent(parse_code)

    def __generate_parse_array_code(self, field: Field) -> str:
        element_struct_name = self.__get_element_struct_name(field)
        array_length_field = field.type.length
        array_code = (
            f"{field.name}: typing.List[{element_struct_name}] = []\n"
            f"for _ in range({array_length_field.name}):\n"
            f"    {field.name}.append(await {element_struct_name}.parse(input))\n"
        )
        return dedent(array_code)

    def __generate_parse_tagged_union_code(
        self, field: Field, union: TaggedUnion
    ) -> str:
        tag_field_name = self.__struct_to_name[union.tag.type]
        union_code = (
            f"tag = await input.read_{tag_field_name}()  # Read tag\n" f"match tag:\n"
        )
        for enum_val, struct_type in union.cases:
            struct_name = self.__struct_to_name[struct_type]
            union_code += f"    case {enum_val.value}:\n"
            union_code += f"        {field.name} = await {struct_name}.parse(input)\n"
        union_code += "    default:\n"
        union_code += "        raise ValueError('Unexpected tag value: {{tag}}')\n"
        return dedent(union_code)

    def __generate_parse_field_code(self, field: Field) -> str:
        match field.type:
            case Array():
                return self.__generate_parse_array_code(field)
            case TaggedUnion():
                return self.__generate_parse_tagged_union_code(field)
            case _:
                return f"await input.read_{field.type.name.lower()}()"

    def generate(self) -> typing.Generator[str, None, None]:
        for _, _, nested in reversed(list(nested_structs(self.__root))):
            yield self.__generate_dataclass(nested)
        yield self.__generate_dataclass(self.__root)


def format_enum_name(enum_value: enum.Enum) -> str:
    words = enum_value.name.split("_")
    formatted_name = "".join(word.capitalize() for word in words)
    return f"{formatted_name}Type"


def nested_structs(root: Struct) -> typing.Generator[StructLink, None, None]:
    for field in root.fields:
        field_type = field.type
        match field_type:
            case Array():
                array_type = typing.cast(Array, field_type)
                if isinstance(array_type.element_type, Struct):
                    yield root, field, array_type.element_type
                    yield from nested_structs(array_type.element_type)
            case TaggedUnion():
                tagged_union_type = typing.cast(TaggedUnion, field_type)
                for _, struct in tagged_union_type.cases:
                    yield root, field, struct
                    yield from nested_structs(struct)
            case Struct():
                yield root, field, field_type
                yield from nested_structs(field_type)


def compute_struct_names(root: Struct, name: str) -> typing.Mapping[Struct, str]:
    names = {root: name}
    for parent, field, nested in nested_structs(root):
        sanitized_field_name = "".join(
            word.capitalize() for word in field.name.split(" ")
        )
        type = field.type
        match type:
            case Struct():
                names[nested] = f"{names[parent]}{sanitized_field_name}"
            case Array():
                names[nested] = f"{names[parent]}{sanitized_field_name}Element"
            case TaggedUnion():
                tagged_union_type = typing.cast(TaggedUnion, type)
                for case_value, case_struct in tagged_union_type.cases:
                    case_name = format_enum_name(case_value)
                    names[
                        case_struct
                    ] = f"{names[parent]}{sanitized_field_name}Case{case_name}"
    return names


def generate_for_command(command: Command) -> typing.Generator[str, None, None]:
    if command.out:
        yield from StructGenerator(command.out, f"{command.name}Out").generate()
    if command.reply:
        yield from StructGenerator(command.reply, f"{command.name}Reply").generate()


def generate_for_command_set(
    command_set: CommandSet,
) -> typing.Generator[str, None, None]:
    for command in command_set.commands:
        yield from generate_for_command(command)


def generate_for_all_command_sets() -> typing.Generator[str, None, None]:
    # TODO: refactor this once PR90 is merged
    from projects.jdwp.defs.command_sets.virtual_machine import VirtualMachine
    from projects.jdwp.defs.command_sets.reference_type import ReferenceType
    from projects.jdwp.defs.command_sets.event_request import EventRequest

    yield from generate_for_command_set(VirtualMachine)
    yield from generate_for_command_set(ReferenceType)
    yield from generate_for_command_set(EventRequest)


def main():
    print("import dataclasses")
    print("import typing")
    print("from projects.jdwp.runtime.type_aliases import *")

    for struct_definition in generate_for_all_command_sets():
        print()
        print(struct_definition)


if __name__ == "__main__":
    main()
