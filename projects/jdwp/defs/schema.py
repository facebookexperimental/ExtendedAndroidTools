# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Basic types for JDWP messages."""

from dataclasses import dataclass
from typing import NewType, Optional
from enum import Enum
from collections.abc import Set, Sequence

from projects.jdwp.defs.constants import ErrorType


class PrimitiveType(Enum):
    """Primitive type class."""

    STRING = "string"
    INT = "int"
    BYTE = "byte"
    BOOLEAN = "boolean"
    DICT = "dict"
    REFERENCE_TYPE_ID = "referenceTypeID"
    CLASS_LOADER = "classLoader"
    FIELD_ID = "fieldID"
    METHOD_ID = "methodID"
    VALUE = "value"
    INTERFACE_ID = "interfaceID"
    CLASS_OBJECT_ID = "classObjectID"
    TAGGED_OBJECT_ID = "taggedObjectID"
    THREAD_ID = "threadID"
    THREAD_GROUP_ID = "threadGroupID"
    OBJECT_ID = "objectID"
    LOCATION = "location"


class Array(Enum):
    """Array class type."""

    pass


class TaggedUnion(Enum):
    """Tagged Union class type"""

    pass


Type = PrimitiveType | Array | TaggedUnion

String = NewType("String", str)
Int = NewType("Int", int)
Byte = NewType("Byte", bytes)
Boolean = NewType("Boolean", bool)
ReferenceTypeID = NewType("ReferenceTypeID", str)
ClassLoader = NewType("ClassLoader", str)
FieldID = NewType("FieldID", str)
MethodID = NewType("MethodID", str)
Value = NewType("Value", str)
InterfaceID = NewType("InterfaceID", str)
ClassObjectID = NewType("ClassObjectID", str)
TaggedObjectID = NewType("TaggedObjectID", str)
ThreadId = NewType("ThreadId", str)
ThreadGroupID = NewType("ThreadGroupID", str)
ObjectID = NewType("ObjectID", str)
Location = NewType("location", str)


@dataclass(frozen=True)
class Field:
    """Field class."""

    name: str
    type: Type
    description: str


@dataclass(frozen=True)
class Struct:
    """Struct class."""

    fields: Sequence[Field]


@dataclass(frozen=True)
class Command:
    """Command class."""

    name: str
    id: int
    out: Optional[Struct]
    reply: Optional[Struct]
    error: Set[ErrorType]


@dataclass(frozen=True)
class CommandSet:
    """Command set class."""

    name: str
    id: int
    commands: Sequence[Command]
