# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Command Set: ReferenceType."""


from projects.jdwp.defs.schema import Command, Field, Struct, CommandSet, Type
from projects.jdwp.defs.constants import ErrorType


Signature = Command(
    name="Signature",
    id=1,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The Reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "signature", Type.STRING, "The JNI signature for the reference type."
            ),
        ]
    ),
    error={
        ErrorType.INVALID_CLASS,
        ErrorType.INVALID_OBJECT,
        ErrorType.VM_DEAD,
    },
)


ReferenceType = CommandSet(
    name="ReferenceType",
    id=2,
    commands=[
        Signature,
    ],
)
