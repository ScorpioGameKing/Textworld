
from dataclasses import dataclass


@dataclass
class Coords:
    x: int
    y: int
    
    def to_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)
    
    @staticmethod
    def from_tuple(coords: tuple[int, int]) -> 'Coords':
        return Coords(*coords)
    
    def __hash__(self) -> int:
        return f"{self.x} {self.y}".__hash__()
    
    def __getstate__(self):
        return (self.x, self.y)
    
    def __setstate__(self, state):
        (self.x, self.y) = state