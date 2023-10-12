"""Suspend policy enum class."""

from enum import Enum


class SuspendPolicy(Enum):
    """SuspendPolicy constants for JDWP."""

    NONE = 0
    EVENT_THREAD = 1
    ALL = 2
