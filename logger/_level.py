
from enum import Enum


class Level(Enum):
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

    def __str__(self):
        return self.name
    
    def __gt__(self, other):
        if isinstance(other, Level):
            return self.value > other.value
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Level):
            return self.value < other.value
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Level):
            return self.value >= other.value
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Level):
            return self.value <= other.value
        return NotImplemented

    @property
    def value(self):
        return self._value_