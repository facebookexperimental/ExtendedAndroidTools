# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Command Set: ArrayType."""

from projects.jdwp.defs.schema import CommandSet
from projects.jdwp.defs.commands.array_type import (

    NewInstance,
)

ArrayType = CommandSet(
    name="ArrayType",
    id=4,
    commands=[
        NewInstance,
    ],
)
