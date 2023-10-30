# Copyright (c) Meta Platforms, Inc. and affiliates.

"""JDWP Commands for ThreadReference Command Set."""

from projects.jdwp.defs.schema import Command, Field, Struct, Type, Array, CommandSet
from projects.jdwp.defs.constants import ErrorType

from projects.jdwp.defs.schema import Command, Field, Struct, Type, Array
from projects.jdwp.defs.constants import ErrorType

AllClasses = Command(
    name="AllClasses",
    id=3,
    out=Struct(
        fields=[
            Field("classes", Type.INT, "Number of reference types that follow."),
            Field(
                "referenceTypes",
                Array(Type.BYTE, Type.INT, Type.INT),
                "Array of reference types.",
            ),
        ]
    ),
    reply=None,
    error={
        ErrorType.INVALID_CLASS_LOADER,
        ErrorType.VM_DEAD,
    },
)


VirtualMachine = CommandSet(
    name="VirtualMachine",
    id=1,
    commands=[
        AllClasses,
    ],
)
