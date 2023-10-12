"""Threat status enum class."""
from enum import Enum


class ThreadStatus(Enum):
    """ThreadStatus constants for JDWP."""

    ZOMBIE = 0
    RUNNING = 1
    SLEEPING = 2
    MONITOR = 3
    WAIT = 4
