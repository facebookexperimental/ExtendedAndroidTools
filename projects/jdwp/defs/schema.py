"""Basic types for JDWP messages."""

from dataclasses import dataclass
from typing import List, Union
from enum import Enum


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


Types = Union[PrimitiveType, Array, TaggedUnion]


@dataclass(frozen=True)
class Field:
    """Field class."""

    name: str
    type = Types
    description: str


@dataclass(frozen=True)
class Struct:
    """Struct class."""

    fields: List[Field]


@dataclass(frozen=True)
class Command:
    """Command class."""

    name: str
    id: int
    out: Struct
    reply: Struct
    error: Struct


@dataclass(frozen=True)
class CommandSet:
    """Command set class."""

    name: str
    id: int
    commands: List[Command]
