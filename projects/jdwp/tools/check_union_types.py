# Copyright (c) Meta Platforms, Inc. and affiliates.

from argparse import ArgumentParser
from projects.jdwp.defs.command_sets import ALL
from projects.jdwp.defs.schema import (
    Command,
    CommandSet,
    Struct,
    TaggedUnion,
    Type,
    Array,
    UnionTag,
)


def check_command_set(command_set: CommandSet) -> None:
    for command in command_set.commands:
        check_command(command)


def check_command(command: Command) -> None:
    if command.out:
        check_struct(command.out)
    if command.reply:
        check_struct(command.reply)


def check_struct(struct: Struct) -> None:
    for field in struct.fields:
        check_type(field.type)


def check_type(type: Type) -> None:
    match type:
        case Struct():
            check_struct(type)
        case Array():
            check_struct(type.element_type)
        case TaggedUnion():
            check_tagged_union(type)


def check_tagged_union(union: TaggedUnion) -> None:
    tagged_union: UnionTag = union.tag.type
    for enum_value in tagged_union.value:
        try:
            union.cases[enum_value]
        except KeyError:
            print(
                f"Error in tagged union '{union.tag.type}': Missing case for enum value '{enum_value}'"
            )
            exit(1)

    for value in union.cases[1]:
        check_struct(value)


def main() -> None:
    parser = ArgumentParser(description="Check tagged union mappings in command sets")
    parser.add_argument("--command-set", type=str, help="Specific command set to check")
    args = parser.parse_args()

    arg_command_set: str = args.command_set

    for command_set in ALL:
        if arg_command_set:
            if arg_command_set != command_set.name:
                continue
        check_command_set(command_set)


if __name__ == "__main__":
    main()
