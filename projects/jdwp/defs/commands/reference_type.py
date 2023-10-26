# Copyright (c) Meta Platforms, Inc. and affiliates.

"""JDWP Commands for Reference Type Command Set."""
from projects.jdwp.defs.schema import Command, Field, Struct, Type
from projects.jdwp.constants.errors import ErrorConstants


Signature = Command(
    name="Signature",
    id=1,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The Reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "signature", Type.STRING, "The JNI signature for the reference type."
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

ClassLoader = Command(
    name="Class loader",
    id=2,
    out=Struct(
        [
            Field(
                "refType",
                Type.REFERENCE_TYPE_ID,
                "The reference type ID.",
            ),
        ]
    ),
    reply=Struct(
        [
            Field(
                "classLoaderID",
                Type.CLASS_LOADER,
                "The class loader for the reference type.",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Modifiers = Command(
    name="Modifiers",
    id=3,
    out=Struct(
        [Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID.")]),
    reply=Struct(
        [
            Field(
                "modBits",
                Type.INT,
                "Modifier bits as defined in Chapter 4 of The Java™ Virtual Machine Specification. ",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Fields = Command(
    name="Fields",
    id=4,
    out=Struct(
        [Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID.")]),
    reply=Struct(
        [
            Field("declared", Type.INT, "Number of declared fields."),
            Field("fieldID", Type.FIELD_ID, "Field ID."),
            Field("name", Type.STRING, "Name of field."),
            Field("signature", Type.STRING, "JNI Signature of field."),
            Field(
                "modBits",
                Type.INT,
                "The modifier bit flags (also known as access flags).",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "CLASS_NOT_PREPARED",
                ErrorConstants.CLASS_NOT_PREPARED,
                "Class has been loaded but not yet prepared.",
            ),
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Methods = Command(
    name="Methods",
    id=5,
    out=Struct(
        [Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID.")]),
    reply=Struct(
        [
            Field("declared", Type.INT, "Number of declared methods."),
            Field("methodID", Type.METHOD_ID, "Method ID."),
            Field("name", Type.STRING, "Name of method."),
            Field("signature", Type.STRING, "JNI signature of method."),
            Field(
                "modBits",
                Type.INT,
                "The modifier bit flags (also known as access flags).",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "CLASS_NOT_PREPARED",
                ErrorConstants.CLASS_NOT_PREPARED,
                "Class has been loaded but not yet prepared.",
            ),
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

GetValues = Command(
    name="Get values",
    id=6,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
            Field("fields", Type.INT, "The number of values to get."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "values",
                Type.INT,
                "The number of values returned, always equal to fields.",
            ),
            Field("value", Type.VALUE, "The field value."),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "INVALID_FIELDID",
                ErrorConstants.INVALID_FIELDID,
                "One or more fieldIDs are invalid.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)


SourceFile = Command(
    name="Sourcefile",
    id=7,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "sourceFile",
                Type.STRING,
                "The source file name. No path information for the file is included",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "ABSENT_INFORMATION",
                ErrorConstants.ABSENT_INFORMATION,
                "The source file attribute is not present.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

NestedType = Command(
    name="Nested type",
    id=8,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("classes", Type.INT,
                  "The number of nested classes and interfaces"),
            Field("refTypeTag", Type.BYTE, "Kind of following reference type."),
            Field(
                "typeID", Type.REFERENCE_TYPE_ID, "The nested class or interface ID."
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Status = Command(
    name="Status",
    id=9,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("status", Type.INT, "Status bits: See JDWP.ClassStatus"),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Interfaces = Command(
    name="Interfaces",
    id=10,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("interfaces", Type.INT, "The number of implemented interfaces"),
            Field("interfaceType", Type.INTERFACE_ID, "Implemented interface."),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

ClassObject = Command(
    name="Class object",
    id=11,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [Field("classObject", Type.CLASS_OBJECT_ID, "Class object.")]),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

SourceDebugExtension = Command(
    name="Source debug extension",
    id=12,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct([Field("extension", Type.STRING, "Extension attribute.")]),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "ABSENT_INFORMATION",
                ErrorConstants.ABSENT_INFORMATION,
                "The source debug extension attribute is not present.",
            ),
            Field(
                "NOT_IMPLEMENTED",
                ErrorConstants.NOT_IMPLEMENTED,
                "The functionality is not implemented in this virtual machine.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

SignatureWithGeneric = Command(
    name="Signature with generic",
    id=13,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "signature", Type.STRING, "The JNI signature for the reference type."
            ),
            Field(
                "genericSignature",
                Type.STRING,
                "The generic signature for the reference type or an empty string if there is none.",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

FieldsWithGeneric = Command(
    name="Fields with generic",
    id=14,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("declared", Type.INT, "Number of declared fields."),
            Field("fieldID", Type.FIELD_ID, "Field ID."),
            Field("name", Type.STRING, "The name of the field."),
            Field("signature", Type.STRING, "The JNI signature of the field."),
            Field(
                "genericSignature",
                Type.STRING,
                "The generic signature of the field, or an empty string if there is none.",
            ),
            Field("modBits", Type.INT, "The modifier bit flags."),
        ]
    ),
    error=Struct(
        [
            Field(
                "CLASS_NOT_PREPARED",
                ErrorConstants.CLASS_NOT_PREPARED,
                "Class has been loaded but not yet prepared.",
            ),
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)


MethodsWithGeneric = Command(
    name="Methods with generic",
    id=15,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("declared", Type.INT, "Number of declared methods."),
            Field("methodID", Type.METHOD_ID, "Method ID."),
            Field("name", Type.STRING, "The name of the method."),
            Field("signature", Type.STRING, "The JNI signature of the method."),
            Field(
                "genericSignature",
                Type.STRING,
                "The generic signature of the method, or an empty string if there is none.",
            ),
            Field("modBits", Type.INT, "The modifier bit flags."),
        ]
    ),
    error=Struct(
        [
            Field(
                "CLASS_NOT_PREPARED",
                ErrorConstants.CLASS_NOT_PREPARED,
                "Class has been loaded but not yet prepared.",
            ),
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

Instances = Command(
    name="Instances",
    id=16,
    out=Struct(
        [
            Field("refType", Type.REFERENCE_TYPE_ID, "The reference type ID."),
            Field("maxInstances", Type.INT,
                  "Maximum number of instances to return."),
        ]
    ),
    reply=Struct(
        [
            Field("instances", Type.INT, "The number of instances that follow."),
            Field(
                "instance",
                Type.TAGGED_OBJECT_ID,
                "An instance of this reference type.",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "NOT_IMPLEMENTED",
                ErrorConstants.NOT_IMPLEMENTED,
                "The functionality is not implemented in this virtual machine.",
            ),
            Field(
                "Illegal Argument",
                ErrorConstants.ILLEGAL_ARGUMENT,
                "maxInstances is less than zero.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)


ClassFileVersion = Command(
    name="Class file version",
    id=17,
    out=Struct([Field("refType", Type.REFERENCE_TYPE_ID, "The class.")]),
    reply=Struct(
        [
            Field("majorVersion", Type.INT, "Major version number"),
            Field("minorVersion", Type.INT, "Minor version number"),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "ABSENT INFORMATION",
                ErrorConstants.ABSENT_INFORMATION,
                "The class file version information is absent for primitive and array type.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)

ConstantPool = Command(
    name="Constant pool",
    id=18,
    out=Struct([Field("refType", Type.REFERENCE_TYPE_ID, "The class.")]),
    reply=Struct(
        [
<<<<<<< HEAD
            Field("count", Type.INT, "Total number of constant pool entries plus one."),
=======
            Field(
                "count", Type.INT, "Total number of constant pool entries plus one."
            ),
>>>>>>> 7667236 (rename types)
            Field("bytes", Type.BYTE, "Raw bytes of constant pool"),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                ErrorConstants.INVALID_CLASS,
                "refType is not the ID of a reference type.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "refType is not a known ID.",
            ),
            Field(
                "ABSENT INFORMATION",
                ErrorConstants.ABSENT_INFORMATION,
                "The class file version information is absent for primitive and array type.",
            ),
            Field(
                "VM_DEAD", ErrorConstants.VM_DEAD, "The virtual machine is not running."
            ),
        ]
    ),
)
