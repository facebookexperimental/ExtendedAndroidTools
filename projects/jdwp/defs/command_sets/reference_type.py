# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Command Set: ReferenceType."""

from jdwp.defs.schema import CommandSet, Type
from jdwp.defs.schema import Command, Field, Struct
from projects.jdwp.defs.constants import ErrorType
from collections.abc import Sequence


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
    error=Sequence[
        ErrorType.INVALID_CLASS,
        ErrorType.INVALID_OBJECT,
        ErrorType.VM_DEAD,
    ],
)


ReferenceType = CommandSet(
    name="ReferenceType",
    id=2,
    commands=[
        Signature,
    ],
)
