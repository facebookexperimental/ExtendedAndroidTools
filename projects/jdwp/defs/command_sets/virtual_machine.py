# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Command Set: ThreadReference."""

from jdwp.defs.schema import CommandSet
from jdwp.defs.commands.virtual_machine import (
    AllClasses,
)


VirtualMachine = CommandSet(
    name="VirtualMachine",
    id=1,
    commands=[
        AllClasses,
    ],
)