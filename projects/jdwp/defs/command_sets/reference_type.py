"""Command Set: ReferenceType."""

from jdwp.defs.schema import CommandSet
from jdwp.defs.commands.reference_type import (
    Signature,
    ClassLoader,
    Modifiers,
    Fields,
    Methods,
    GetValues,
    SourceFile,
    NestedTypes,
    Status,
    Interfaces,
    ClassObject,
    SourceDebugExtension,
    SignatureWithGeneric,
    FieldsWithGeneric,
    MethodsWithGeneric,
    Instances,
    ClassFileVersion,
    ConstantPool,
)

ReferenceType = CommandSet(
    name="VirtualMachine",
    id=2,
    commands=[
        Signature,
        ClassLoader,
        Modifiers,
        Fields,
        Methods,
        GetValues,
        SourceFile,
        NestedTypes,
        Status,
        Interfaces,
        ClassObject,
        SourceDebugExtension,
        SignatureWithGeneric,
        FieldsWithGeneric,
        MethodsWithGeneric,
        Instances,
        ClassFileVersion,
        ConstantPool,
    ],
)
