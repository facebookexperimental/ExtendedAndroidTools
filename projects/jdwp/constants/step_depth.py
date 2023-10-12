"""Step depth enum class."""

from enum import Enum


class StepDepth(Enum):
    """StepDepth constants for JDWP."""

    INTO = 0
    OVER = 1
    OUT = 2
