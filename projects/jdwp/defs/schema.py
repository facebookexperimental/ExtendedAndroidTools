# Copyright (c) Meta Platforms, Inc. and affiliates.

"""Basic types for JDWP messages."""

from __future__ import annotations
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar, Type as TypeAlias
from collections.abc import Mapping
from enum import Enum
from collections.abc import Set, Sequence
from projects.jdwp.defs.constants import ErrorType


Type = Union[
    "Array",
    "ArrayLength",
    "IdType",
    "IntegralType",
    "OpaqueType",
    "Struct",
    "TaggedUnion",
    "UnionTag",
]


class OpaqueType(Enum):
    """Opaque types whose implementation is provided by debugger runtime library or language."""

    STRING = "string"
    BOOLEAN = "boolean"
    # TAGGED_OBJECT_ID = "tagged-objectID"
    LOCATION = "location"
    STRING = "string"
    # VALUE = "value"
    # UNTAGGED_VALUE = "untagged-value"
    # ARRAY_REGION = "arrayregion"


class IdType(Enum):
    """Types representing numeric IDs of internal VM objects."""

    OBJECT_ID = "objectID"
    THREAD_ID = "threadID"
    THREAD_GROUP_ID = "threadGroupID"
    STRING_ID = "stringId"
    CLASS_LOADER_ID = "classLoaderID"
    CLASS_OBJECT_ID = "classObjectID"
    ARRAY_ID = "arrayID"
    REFERENCE_TYPE_ID = "referenceTypeID"
    CLASS_ID = "classID"
    INTERFACE_ID = "interfaceID"
    ARRAY_TYPE_ID = "arrayTypeID"
    METHOD_ID = "methodID"
    FIELD_ID = "fieldID"
    FRAME_ID = "frameID"


class IntegralType(Enum):
    """Integer types of different precision."""

    BYTE = "byte"
    INT = "int"
    LONG = "long"


@dataclass(frozen=True)
class ArrayLength:
    """Array length class."""

    type: IntegralType


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


Type = (
    PrimitiveType | Array | TaggedUnion | IntegralType | ArrayLength | Struct | UnionTag
)

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
