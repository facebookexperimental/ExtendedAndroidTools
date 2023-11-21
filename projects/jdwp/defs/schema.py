# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Basic types for JDWP messages."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar, Type as TypeAlias, Union
from collections.abc import Mapping
from enum import Enum
from collections.abc import Set, Sequence
from projects.jdwp.defs.constants import ErrorType


Type = Union[
    "PrimitiveType",
    "Array",
    "TaggedUnion",
    "IntegralType",
    "ArrayLength",
    "Struct",
    "UnionTag",
]


class PrimitiveType(Enum):
    """Primitive type class."""

    STRING = "string"
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


EnumT = TypeVar("EnumT", bound=Enum)


@dataclass(frozen=True)
class TaggedUnion(Generic[EnumT]):
    """Tagged Union class type"""

    tag: Field[UnionTag[EnumT]]
    cases: Mapping[EnumT, Struct]


@dataclass(frozen=True)
class UnionTag(Generic[EnumT]):
    """Union tag class type."""

    tag: IntegralType
    value: TypeAlias[EnumT]


TypeT = TypeVar("TypeT", bound=Type, covariant=True)


@dataclass(frozen=True)
class Field(Generic[TypeT]):
    """Field class."""

    name: str
    type: TypeT
    description: str


@dataclass(frozen=True)
class Struct:
    """Struct class."""

    fields: Sequence[Field[Type]]


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
