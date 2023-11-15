# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Basic types for JDWP messages."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar
from enum import Enum
from collections.abc import Set, Sequence

from projects.jdwp.defs.constants import ErrorType


class PrimitiveType(Enum):
    """Primitive type class."""

    STRING = "string"
    BOOLEAN = "boolean"
    INT = "int"
    BYTE = "int"
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


class IntegralType(Enum):
    """Integral type class."""

    INT = "int"
    BYTE = "byte"


@dataclass(frozen=True)
class ArrayLength:
    """Array length class."""

    type: IntegralType


@dataclass(frozen=True)
class Array:
    """Array class type."""

    element_type: Struct
    length: Field[ArrayLength]


class TaggedUnion(Enum):
    """Tagged Union class type"""

    pass


Type = PrimitiveType | Array | TaggedUnion | IntegralType | ArrayLength

T = TypeVar("T", bound=Type)


@dataclass(frozen=True)
class Field(Generic[T]):
    """Field class."""

    name: str
    type: T
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
