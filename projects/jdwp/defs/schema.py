# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Basic types for JDWP messages."""

from dataclasses import dataclass
from typing import Optional, Dict
from typing_extensions import Literal
from enum import Enum
from collections.abc import Set, Sequence
from projects.jdwp.constants.errors import ErrorConstants
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
    ARRAY_TYPE_ID = "arrayTypeID"


@dataclass(frozen=True)
class Array(Enum):
    """Array class type."""

    base_type: PrimitiveType
    dimensions: int


class TaggedUnion(Enum):
    """Tagged Union class type"""

    pass


Type = PrimitiveType | Array | TaggedUnion | ErrorConstants


@dataclass(frozen=True)
class Field:
    """Field class."""

    name: str
    type: Type
    description: str


@dataclass(frozen=True)
class Struct:
    """Struct class."""

    fields: Sequence[Field | Array]


@dataclass(frozen=True)
class Command:
    """Command class."""

    name: str
    id: int
    out: Optional[Struct]
    reply: Optional[Struct]
    error: Dict[ErrorType, str] | Struct | Set[ErrorType]


@dataclass(frozen=True)
class CommandSet:
    """Command set class."""

    name: str
    id: int
    commands: Sequence[Command]
