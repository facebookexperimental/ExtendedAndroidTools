# Copyright (c) Meta Platforms, Inc. and affiliates.

from projects.jdwp.defs.schema import IdType
from projects.jdwp.codegen.types import python_type_for


def get_type_alias_definition(jdwp_type: IdType) -> str:
    """Return the type alias definition for a given IdType."""
    python_type = python_type_for(jdwp_type)
    return f"{python_type} = typing.NewType('{python_type}', int)"


def generate_new_types():
    print("import typing")
    for id_type in IdType:
        type_alias_definition = get_type_alias_definition(id_type)
        print(type_alias_definition)


if "__main__" == __name__:
    generate_new_types()
