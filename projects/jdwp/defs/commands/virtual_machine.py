"""JDWP Commands for ThreadReference Command Set."""

from jdwp.defs.schema import Command, Field, Struct, Type, Array
from jdwp.constants.errors import ErrorConstants

AllClasses = Command(
    name="AllClasses",
    id=3,
    out=None,
    reply=Struct(
        fields=[
            Field("classes", Type.INT, "Number of reference types that follow."),
            Field("referenceTypes", Array(Type.BYTE), "Array of reference types."),
        ]
    ),
    error={
        ErrorConstants.VM_DEAD: "The virtual machine is not running."
    }
)