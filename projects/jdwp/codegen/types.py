# Copyright (c) Meta Platforms, Inc. and affiliates.

from projects.jdwp.defs.schema import (
    ArrayLength,
    OpaqueType,
    IdType,
    IntegralType,
    Type,
    UnionTag,
)
import typing


__OPAQUE_TYPE_MAPPING = {
    OpaqueType.BOOLEAN: "bool",
    OpaqueType.LOCATION: "typing.Any",
    OpaqueType.STRING: "str",
}


def python_type_for(jdwp_type: Type) -> str:
    match jdwp_type:
        case OpaqueType():
            return __OPAQUE_TYPE_MAPPING[jdwp_type]
        case IdType():
            return jdwp_type.value[0].upper() + jdwp_type.value[1:] + "Type"
        case IntegralType() | ArrayLength() | UnionTag():
            return "int"
        case _:
            raise Exception("not implemented")
