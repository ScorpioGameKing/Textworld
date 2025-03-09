from dataclasses import dataclass
from models.coords import Coords

@dataclass
class Tile:
    tile_char:str
    color:str
    name:str
    position: Coords

    def get_markdown(self):
        return f'[color=#{self.color}]{self.tile_char}[/color]'
    
    def __getstate__(self):
        return (self.tile_char, self.color, self.name, self.position)
    
    def __setstate__(self, state):
        (self.tile_char, self.color, self.name, self.position) = state