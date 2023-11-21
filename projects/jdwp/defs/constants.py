# Copyright (c) Meta Platforms, Inc. and affiliates.

from enum import Enum, Flag


class ErrorType(Enum):
    """Error constants for JDWP."""

    NONE = 0
    INVALID_THREAD = 10
    INVALID_THREAD_GROUP = 11
    INVALID_PRIORITY = 12
    THREAD_NOT_SUSPENDED = 13
    THREAD_SUSPENDED = 14
    THREAD_NOT_ALIVE = 15
    INVALID_OBJECT = 20
    INVALID_CLASS = 21
    CLASS_NOT_PREPARED = 22
    INVALID_METHODID = 23
    INVALID_LOCATION = 24
    INVALID_FIELDID = 25
    INVALID_FRAMEID = 30
    NO_MORE_FRAMES = 31
    OPAQUE_FRAME = 32
    NOT_CURRENT_FRAME = 33
    TYPE_MISMATCH = 34
    INVALID_SLOT = 35
    DUPLICATE = 40
    NOT_FOUND = 41
    INVALID_MONITOR = 50
    NOT_MONITOR_OWNER = 51
    INTERRUPT = 52
    INVALID_CLASS_FORMAT = 60
    CIRCULAR_CLASS_DEFINITION = 61
    FAILS_VERIFICATION = 62
    ADD_METHOD_NOT_IMPLEMENTED = 63
    SCHEMA_CHANGE_NOT_IMPLEMENTED = 64
    INVALID_TYPESTATE = 65
    HIERARCHY_CHANGE_NOT_IMPLEMENTED = 66
    DELETE_METHOD_NOT_IMPLEMENTED = 67
    UNSUPPORTED_VERSION = 68
    NAMES_DONT_MATCH = 69
    CLASS_MODIFIERS_CHANGE_NOT_IMPLEMENTED = 70
    METHOD_MODIFIERS_CHANGE_NOT_IMPLEMENTED = 71
    NOT_IMPLEMENTED = 99
    NULL_POINTER = 100
    ABSENT_INFORMATION = 101
    INVALID_EVENT_TYPE = 102
    ILLEGAL_ARGUMENT = 103
    OUT_OF_MEMORY = 110
    ACCESS_DENIED = 111
    VM_DEAD = 112
    INTERNAL = 113
    UNATTACHED_THREAD = 115
    INVALID_TAG = 500
    ALREADY_INVOKING = 502
    INVALID_INDEX = 503
    INVALID_LENGTH = 504
    INVALID_STRING = 506
    INVALID_CLASS_LOADER = 507
    INVALID_ARRAY = 508
    TRANSPORT_LOAD = 509
    TRANSPORT_INIT = 510
    NATIVE_METHOD = 511
    INVALID_COUNT = 512


class ClassStatus(Enum):
    """ClassStatus constants for JDWP."""

    VERIFIED = 1
    PREPARED = 2
    INITIALIZED = 4
    ERROR = 8


class EventKind(Enum):
    """EventKind constants for JDWP."""

    SINGLE_STEP = 1
    BREAKPOINT = 2
    FRAME_POP = 3
    EXCEPTION = 4
    USER_DEFINED = 5
    THREAD_START = 6
    THREAD_DEATH = 7
    THREAD_END = 7
    CLASS_PREPARE = 8
    CLASS_UNLOAD = 9
    CLASS_LOAD = 10
    FIELD_ACCESS = 20
    FIELD_MODIFICATION = 21
    EXCEPTION_CATCH = 30
    METHOD_ENTRY = 40
    METHOD_EXIT = 41
    METHOD_EXIT_WITH_RETURN_VALUE = 42
    MONITOR_CONTENDED_ENTER = 43
    MONITOR_CONTENDED_ENTERED = 44
    MONITOR_WAIT = 45
    MONITOR_WAITED = 46
    VM_START = 90
    VM_INIT = 90
    VM_DEATH = 99
    VM_DISCONNECTED = 100


class InvokeOptions(Flag):
    """Invoke options constants for JDWP."""

    INVOKE_SINGLE_THREADED = 0x01
    INVOKE_NONVIRTUAL = 0x02


class StepDepth(Enum):
    """StepDepth constants for JDWP."""

    INTO = 0
    OVER = 1
    OUT = 2


class StepSize(Enum):
    """StepSize constants for JDWP."""

    MIN = 0
    LINE = 1


class SuspendPolicy(Enum):
    """SuspendPolicy constants for JDWP."""

    NONE = 0
    EVENT_THREAD = 1
    ALL = 2


class SuspendStatus(Enum):
    """SuspendStatus constants for JDWP."""

    SUSPEND_STATUS_SUSPENDED = 0x1


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


class ThreadStatus(Enum):
    """ThreadStatus constants for JDWP."""

    ZOMBIE = 0
    RUNNING = 1
    SLEEPING = 2
    MONITOR = 3
    WAIT = 4


class TypeTag(Enum):
    """TypeTag constants for JDWP."""

    CLASS = 1
    INTERFACE = 2
    ARRAY = 3


class ModifierKind(Enum):
    COUNT = 1
    CONDITIONAL = 2
    THREAD_ONLY = 3
    CLASS_ONLY = 4
    CLASS_MATCH = 5
    CLASS_EXCLUDE = 6
    LOCATION_ONLY = 7
    EXCEPTION_ONLY = 8
    FIELD_ONLY = 9
    STEP = 10
    INSTANCE_ONLY = 11
    SOURCE_NAME_MATCH = 12
