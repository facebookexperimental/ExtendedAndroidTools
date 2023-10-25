"""Command Set: ArrayType."""

from jdwp.defs.schema import CommandSet
from jdwp.defs.commands.array_type import (
    NewInstance,
)

ArrayType = CommandSet(
    name="ArrayType",
    id=4,
    commands=[
        NewInstance,
    ],
)