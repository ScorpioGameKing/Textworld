from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T', int, float)

@dataclass
class Size(Generic[T]):
    height: T
    width: T
    def to_tuple(self):
        return (self.height, self.width)
    
    def area(self):
        return self.height * self.width