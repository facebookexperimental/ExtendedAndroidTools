# Copyright (c) Meta Platforms, Inc. and affiliates.

"""JDWP Commands for ThreadReference Command Set."""

from projects.jdwp.defs.schema import Command, Field, Struct, Type, Array
from projects.jdwp.constants.errors import ErrorConstants

AllClasses = Command(
    name="AllClasses",
    id=3,
    out=None,
    reply=Struct(
        fields=[
            Field("classes", Type.INT, "Number of reference types that follow."),
            Field("referenceTypes", Array(Type.BYTE, Type.INT),
                  "Array of reference types."),
        ]
    ),
    error=Struct(
        [
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    )
)
