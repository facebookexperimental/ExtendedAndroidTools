"""Suspend status enum class."""

from enum import Enum


class SuspendStatus(Enum):
    """SuspendStatus constants for JDWP."""

    SUSPEND_STATUS_SUSPENDED = 0x1
