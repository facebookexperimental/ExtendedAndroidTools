# Copyright (c) Meta Platforms, Inc. and affiliates.

from projects.jdwp.defs.schema import (
    Command,
    Field,
    Struct,
    CommandSet,
    IntegralType,
    ArrayLength,
    Array,
    TaggedUnion,
    UnionTag,
    Type,
)
from projects.jdwp.defs.constants import ErrorType, ModifierKind


CountModifier = Struct(
    [Field("count", IntegralType.INT, "Count before event. One for one-off.")]
)

ConditionalModifier = Struct([Field("exprID", IntegralType.INT, "For the future")])

ThreadOnlyModifier = Struct([Field("thread", Type.THREAD_ID, "Required thread")])

ClassOnlyModifier = Struct([Field("clazz", Type.REFERENCE_TYPE_ID, "Required class")])

ClassMatchModifier = Struct(
    [Field("classPattern", Type.STRING, "Restricted class pattern")]
)

StepModifier = Struct(
    [
        Field("thread", Type.THREAD_ID, "Required thread"),
        Field("size", IntegralType.INT, "Size of each step"),
        Field("depth", IntegralType.INT, "Relative call stack limit"),
    ]
)

ClassExcludeModifier = Struct(
    [Field("classPattern", Type.STRING, "Disallowed class pattern")]
)

LocationOnlyModifier = Struct([Field("loc", Type.LOCATION, "Required location")])

ExceptionOnlyModifier = Struct(
    [
        Field(
            "exceptionOrNull",
            Type.REFERENCE_TYPE_ID,
            "Exception to report. Null (0) means report exceptions of all types.",
        ),
        Field("caught", Type.BOOLEAN, "True if exception was caught"),
        Field("uncaught", Type.BOOLEAN, "True if exception was uncaught"),
    ]
)

FieldOnlyModifier = Struct(
    [
        Field("declaring", Type.REFERENCE_TYPE_ID, "Type in which field is declared."),
        Field("fieldID", IntegralType.INT, "Required field"),
    ]
)

InstanceOnlyModifier = Struct(
    [Field("instance", Type.OBJECT_ID, "Required 'this' object")]
)

SourceNameMatchModifier = Struct(
    [Field("sourceNamePattern", Type.STRING, "	Required source name pattern")]
)

__SetCommand_out_modKind = Field(
    "modKind", UnionTag(IntegralType.BYTE, ModifierKind), "Modifier kind"
)

__SetCommand_outArray_element_modifier = Field(
    "Modifier cases",
    TaggedUnion(
        __SetCommand_out_modKind,
        {
            ModifierKind.COUNT: CountModifier,
            ModifierKind.CONDITIONAL: ConditionalModifier,
            ModifierKind.THREAD_ONLY: ThreadOnlyModifier,
            ModifierKind.CLASS_ONLY: ClassOnlyModifier,
            ModifierKind.CLASS_MATCH: ClassMatchModifier,
            ModifierKind.CLASS_EXCLUDE: ClassExcludeModifier,
            ModifierKind.STEP: StepModifier,
            ModifierKind.LOCATION_ONLY: LocationOnlyModifier,
            ModifierKind.EXCEPTION_ONLY: ExceptionOnlyModifier,
            ModifierKind.FIELD_ONLY: FieldOnlyModifier,
            ModifierKind.INSTANCE_ONLY: InstanceOnlyModifier,
            ModifierKind.SOURCE_NAME_MATCH: SourceNameMatchModifier,
        },
    ),
    "Modifier cases.",
)

__SetCommand_outModifierArray_length = Field(
    "modifiers",
    ArrayLength(IntegralType.INT),
    "Constraints used to control the number of generated events.",
)
__SetCommand_out = Struct(
    [
        Field("eventKind", IntegralType.BYTE, "The kind of event to request."),
        Field("suspendPolicy", IntegralType.BYTE, "The suspend policy to use."),
        __SetCommand_outModifierArray_length,
        Field(
            "outModifiers",
            Array(
                Struct(
                    [
                        __SetCommand_out_modKind,
                        __SetCommand_outArray_element_modifier,
                    ]
                ),
                __SetCommand_outModifierArray_length,
            ),
            "Modifier Array",
        ),
    ]
)

SetCommand = Command(
    name="SetCommand",
    id=1,
    out=__SetCommand_out,
    reply=Struct([Field("requestID", IntegralType.INT, "ID of the request created.")]),
    error={
        ErrorType.INVALID_EVENT_TYPE,
        ErrorType.INVALID_CLASS,
        ErrorType.INVALID_STRING,
        ErrorType.INVALID_OBJECT,
        ErrorType.INVALID_COUNT,
        ErrorType.INVALID_FIELDID,
        ErrorType.INVALID_METHODID,
        ErrorType.INVALID_LOCATION,
        ErrorType.INVALID_EVENT_TYPE,
        ErrorType.NOT_IMPLEMENTED,
        ErrorType.VM_DEAD,
    },
)

EventRequest = CommandSet(
    name="EventRequest",
    id=1,
    commands=[
        SetCommand,
    ],
)
