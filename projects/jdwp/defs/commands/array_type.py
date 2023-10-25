"""JDWP Commands for Reference Type Command Set."""
from jdwp.defs.schema import Command, Field, Struct, Types
from jdwp.constants.errors import ErrorConstants

NewInstance = Command(
    name="NewInstance",
    id=1,
    out=Struct(
        [
            Field("arrayTypeID", Types.ARRAY_TYPE_ID, "The array type of the new instance."),
            Field("length", Types.INT, "The length of the array."),
        ]
    ),
    reply=Struct(
        [
            Field("newArray", Types.TAGGED_OBJECT_ID, "The newly created array object."),
        ]
    ),
    error=Struct(
        [
            Field(
                "INVALID_ARRAY",
                ErrorConstants.INVALID_ARRAY,
                "The array is invalid.",
            ),
            Field(
                "INVALID_OBJECT",
                ErrorConstants.INVALID_OBJECT,
                "If this reference type has been unloaded and garbage collected.",
            ),
            Field(
                "VM_DEAD",
                ErrorConstants.VM_DEAD,
                "The virtual machine is not running.",
            ),
        ]
    ),
)
