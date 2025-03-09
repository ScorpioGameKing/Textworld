
from enum import StrEnum


class Direction(StrEnum):
    """Direction enum."""

    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"

    @classmethod
    def from_string(cls, direction: str) -> 'Direction':
        """Convert a string to a Direction enum."""
        return cls[direction.upper()]