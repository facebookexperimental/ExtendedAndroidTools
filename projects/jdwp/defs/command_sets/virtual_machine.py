# Copyright (c) Meta Platforms, Inc. and affiliates.

"""JDWP Commands for ThreadReference Command Set."""

from projects.jdwp.defs.schema import (
    Command,
    Field,
    Struct,
    Type,
    Array,
    CommandSet,
    ArrayLength,
    IntegralType,
)
from projects.jdwp.defs.constants import ErrorType


__AllClasses_reply_classes = Field(
    "classes",
    ArrayLength(IntegralType.INT),
    "Number of reference type that follow",
)


__AllClasses_reply_classesArray_element = Struct(
    [
        Field("refTypeTag", IntegralType.BYTE, "Kind of following reference type"),
        Field("typeID", Type.REFERENCE_TYPE_ID, "Loaded reference type"),
        Field(
            "signature", Type.STRING, "The JNI signature of the loaded reference type"
        ),
        Field("status", IntegralType.INT, "The current class status"),
    ]
)

__AllClasses_reply = Struct(
    [
        __AllClasses_reply_classes,
        Field(
            "classesArray",
            Array(__AllClasses_reply_classesArray_element, __AllClasses_reply_classes),
            "Array of reference type.",
        ),
    ]
)

AllClasses = Command(
    name="AllClasses",
    id=3,
    out=None,
    reply=__AllClasses_reply,
    error={
        ErrorType.VM_DEAD,
    },
)

Dispose = Command(
    name="Dispose",
    id=6,
    out=None,
    reply=None,
    error=set(),
)

__IDSizes_reply = Struct(
    [
        Field("fieldIDSize", IntegralType.INT, "fieldID size in bytes"),
        Field("methodIDSize", IntegralType.INT, "methodID size in bytes"),
        Field("objectIDSize", IntegralType.INT, "objectID size in bytes"),
        Field("referenceTypeIDSize", IntegralType.INT, "referenceTypeID size in bytes"),
        Field("frameIDSize", IntegralType.INT, "frameID size in bytes"),
    ]
)

IDSizes = Command(
    name="IDSizes",
    id=7,
    out=None,
    reply=__IDSizes_reply,
    error={ErrorType.VM_DEAD},
)

VirtualMachine = CommandSet(
    name="VirtualMachine",
    id=1,
    commands=[
        AllClasses,
        Dispose,
        IDSizes,
    ],
)
