"""Type tag enum class."""

from enum import Enum


class TypeTag(Enum):
    """TypeTag constants for JDWP."""

    CLASS = 1
    INTERFACE = 2
    ARRAY = 3
