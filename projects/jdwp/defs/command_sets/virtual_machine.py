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

__Version_reply = Struct(
    [
        Field("description", Type.STRING, "Text information on the VM version"),
        Field("jdwpMajor", IntegralType.INT, "JDWP major version number"),
        Field("jdwpMinor", IntegralType.INT, "JDWP minor version number"),
        Field(
            "vmVersion",
            Type.STRING,
            "Target VM JRE version, as in the java.version property",
        ),
        Field("vmName", Type.STRING, "Target VM name, as in the java.vm.name property"),
    ]
)

Version = Command(
    name="Version",
    id=1,
    out=None,
    reply=__Version_reply,
    error={ErrorType.VM_DEAD},
)

VirtualMachine = CommandSet(
    name="VirtualMachine",
    id=1,
    commands=[
        Version,
        AllClasses,
    ],
)
