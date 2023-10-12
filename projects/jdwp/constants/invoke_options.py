"""Invoke options enum class."""
from enum import IntEnum


class InvokeOptions(IntEnum):
    """Invoke options constants for JDWP."""

    INVOKE_SINGLE_THREADED = 0x01
    INVOKE_NON_VIRTUAL = 0x02
