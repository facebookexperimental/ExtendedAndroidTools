"""JDWP Commands for Reference Type Command Set."""
from jdwp.common import Command, CommandSet, Field, Struct, Types


Signature = Command(
    name="Signature",
    id=1,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The Reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "signature", Types.STRING, "The JNI signature for the reference type."
            ),
        ]
    ),
    error=Struct([]),
)

ClassLoader = Command(
    name="Class loader",
    id=2,
    out=Struct(
        [
            Field(
                "refType",
                Types.REFERENCE_TYPE_ID,
                "The reference type ID.",
            ),
        ]
    ),
    reply=Struct(
        [
            Field(
                "classLoaderID",
                Types.CLASS_LOADER,
                "The class loader for the reference type.",
            ),
        ]
    ),
    error=Struct([]),
)

Modifiers = Command(
    name="Modifiers",
    id=3,
    out=Struct([Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID.")]),
    reply=Struct(
        [
            Field(
                "modBits",
                Types.INT,
                "Modifier bits as defined in Chapter 4 of The Java™ Virtual Machine Specification. ",
            ),
        ]
    ),
    error=Struct([]),
)

Fields = Command(
    name="Fields",
    id=4,
    out=Struct([Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID.")]),
    reply=Struct(
        [
            Field("declared", Types.INT, "Number of declared fields."),
            Field("fieldID", Types.FIELD_ID, "Field ID."),
            Field("name", Types.STRING, "Name of field."),
            Field("signature", Types.STRING, "JNI Signature of field."),
            Field(
                "modBits",
                Types.INT,
                "The modifier bit flags (also known as access flags).",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "CLASS_NOT_PREPARED",
                Types.STRING,
                "Class has been loaded but not yet prepared.",
            ),
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

Methods = Command(
    name="Methods",
    id=5,
    out=Struct([Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID.")]),
    reply=Struct(
        [
            Field("declared", Types.INT, "Number of declared methods."),
            Field("methodID", Types.METHOD_ID, "Method ID."),
            Field("name", Types.STRING, "Name of method."),
            Field("signature", Types.STRING, "JNI signature of method."),
            Field(
                "modBits",
                Types.INT,
                "The modifier bit flags (also known as access flags).",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "CLASS_NOT_PREPARED",
                Types.STRING,
                "Class has been loaded but not yet prepared.",
            ),
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

GetValues = Command(
    name="Get values",
    id=6,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
            Field("fields", Types.INT, "The number of values to get."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "values",
                Types.INT,
                "The number of values returned, always equal to fields.",
            ),
            Field("value", Types.VALUE, "The field value."),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("INVALID_FIELDID", Types.STRING, "Invalid field."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)


SourceFile = Command(
    name="Sourcefile",
    id=7,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "sourceFile",
                Types.STRING,
                "The source file name. No path information for the file is included",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field(
                "ABSENT_INFORMATION",
                Types.STRING,
                "The source file attribute is absent.",
            ),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

NestedTypes = Command(
    name="Nested types",
    id=8,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("classes", Types.INT, "The number of nested classes and interfaces"),
            Field("refTypeTag", Types.BYTE, "Kind of following reference type."),
            Field(
                "typeID", Types.REFERENCE_TYPE_ID, "The nested class or interface ID."
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

Status = Command(
    name="Status",
    id=9,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("status", Types.INT, "Status bits: See JDWP.ClassStatus"),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

Interfaces = Command(
    name="Interfaces",
    id=10,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("interfaces", Types.INT, "The number of implemented interfaces"),
            Field("interfaceType", Types.INTERFACE_ID, "Implemented interface."),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

ClassObject = Command(
    name="Class object",
    id=11,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct([Field("classObject", Types.CLASS_OBJECT_ID, "Class object.")]),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

SourceDebugExtension = Command(
    name="Source debug extension",
    id=12,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct([Field("extension", Types.STRING, "Extension attribute.")]),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field(
                "ABSENT_INFORMATION", Types.STRING, "If the extension is not specified."
            ),
            Field(
                "NOT_IMPLEMENTED",
                Types.STRING,
                "The functionality is not implemented in this virtual machine.",
            ),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

SignatureWithGeneric = Command(
    name="Signature with generic",
    id=13,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field(
                "signature", Types.STRING, "The JNI signature for the reference type."
            ),
            Field(
                "genericSignature",
                Types.STRING,
                "The generic signature for the reference type or an empty string if there is none.",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

FieldsWithGeneric = Command(
    name="Fields with generic",
    id=14,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("declared", Types.INT, "Number of declared fields."),
            Field("fieldID", Types.FIELD_ID, "Field ID."),
            Field("name", Types.STRING, "The name of the field."),
            Field("signature", Types.STRING, "The JNI signature of the field."),
            Field(
                "genericSignature",
                Types.STRING,
                "The generic signature of the field, or an empty string if there is none.",
            ),
            Field("modBits", Types.INT, "The modifier bit flags."),
        ]
    ),
    error=Struct(
        [
            Field(
                "CLASS_NOT_PREPARED",
                Types.STRING,
                "Class has been loaded but not yet prepared.",
            ),
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)


MethodsWithGeneric = Command(
    name="Methods with generic",
    id=15,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
        ]
    ),
    reply=Struct(
        [
            Field("declared", Types.INT, "Number of declared methods."),
            Field("methodID", Types.METHOD_ID, "Method ID."),
            Field("name", Types.STRING, "The name of the method."),
            Field("signature", Types.STRING, "The JNI signature of the method."),
            Field(
                "genericSignature",
                Types.STRING,
                "The generic signature of the method, or an empty string if there is none.",
            ),
            Field("modBits", Types.INT, "The modifier bit flags."),
        ]
    ),
    error=Struct(
        [
            Field(
                "CLASS_NOT_PREPARED",
                Types.STRING,
                "Class has been loaded but not yet prepared.",
            ),
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

Instances = Command(
    name="Instances",
    id=16,
    out=Struct(
        [
            Field("refType", Types.REFERENCE_TYPE_ID, "The reference type ID."),
            Field("maxInstances", Types.INT, "Maximum number of instances to return."),
        ]
    ),
    reply=Struct(
        [
            Field("instances", Types.INT, "The number of instances that follow."),
            Field(
                "instance",
                Types.TAGGED_OBJECT_ID,
                "An instance of this reference type.",
            ),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field("ILLEGAL_ARGUMENT", Types.STRING, "maxInstances is less than zero."),
            Field(
                "NOT_IMPLEMENTED",
                Types.STRING,
                "The functionality is not implemented in this virtual machine.",
            ),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)


ClassFileVersion = Command(
    name="Class file version",
    id=17,
    out=Struct([Field("refType", Types.REFERENCE_TYPE_ID, "The class.")]),
    reply=Struct(
        [
            Field("majorVersion", Types.INT, "Major version number"),
            Field("minorVersion", Types.INT, "Minor version number"),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field(
                "ABSENT_INFORMATION",
                Types.STRING,
                "The class file version information is absent for primitive and array types.",
            ),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
)

ConstantPool = Command(
    name="Constant pool",
    id=18,
    out=Struct([Field("refType", Types.REFERENCE_TYPE_ID, "The class.")]),
    reply=Struct(
        [
            Field(
                "count", Types.INT, "Total number of constant pool entries plus one."
            ),
            Field("bytes", Types.BYTE, "Raw bytes of constant pool"),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_CLASS",
                Types.STRING,
                "refType is not the ID of a reference type.",
            ),
            Field("INVALID_OBJECT", Types.STRING, "refType is not a known ID."),
            Field(
                "NOT_IMPLEMENTED",
                Types.STRING,
                "If the target virtual machine does not support the retrieval of constant pool information.",
            ),
            Field(
                "ABSENT_INFORMATION",
                Types.STRING,
                "The Constant Pool information is absent for primitive and array types.",
            ),
            Field("VM_DEAD", Types.STRING, "The virtual machine is not running."),
        ]
    ),
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
