"""Class Status  enum class."""

from enum import Enum


class ClassStatus(Enum):
    """ClassStatus constants for JDWP."""

    VERIFIED = 1
    PREPARED = 2
    INITIALIZED = 4
    ERROR = 8
