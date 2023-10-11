"""Tag enum class."""
from enum import Enum


class Tag(Enum):
    """Tag constants for JDWP."""

    ARRAY = 91
    BYTE = 66
    CHAR = 67
    OBJECT = 76
    FLOAT = 70
    DOUBLE = 68
    INT = 73
    LONG = 74
    SHORT = 83
    VOID = 86
    BOOLEAN = 90
    STRING = 115
    THREAD = 116
    THREAD_GROUP = 103
    CLASS_LOADER = 108
    CLASS_OBJECT = 99
