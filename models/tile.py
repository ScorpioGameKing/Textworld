from dataclasses import dataclass

@dataclass
class Tile:
    tile_char:str
    color:str
    
    def __getstate__(self):
        return (self.tile_char, self.color)
    
    def __setstate__(self, state):
        (self.tile_char, self.color) = state