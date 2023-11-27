# Copyright (c) Meta Platforms, Inc. and affiliates.

from argparse import ArgumentParser
from projects.jdwp.defs.schema import CommandSet
from projects.jdwp.defs.command_sets import ALL


def check_command_ids(command_set: CommandSet) -> None:
    try:
        sorted_command_ids = [command.id for command in command_set.commands]
        if sorted_command_ids != sorted(sorted_command_ids):
            print(f"Command IDs in {command_set.name} are NOT in ascending order.")
            exit(1)
    except Exception as e:
        print(f"Error checking command IDs in {command_set.name}: {e}")
        exit(1)


def main() -> None:
    parser = ArgumentParser(description="Check order of command IDs in command sets")
    parser.add_argument("--command-set", type=str, help="Specific command set to check")
    args = parser.parse_args()

    arg_command_set: str = args.command_set

    for command_set in ALL:
        if arg_command_set:
            if arg_command_set != command_set.name:
                continue
        check_command_ids(command_set)


if __name__ == "__main__":
    main()
