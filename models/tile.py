from dataclasses import dataclass

@dataclass
class Tile:
    tile_char:str
    color:str
    name:str

    def get_markdown(self):
        return f'[color=#{self.color}]{self.tile_char}[/color]'
    
    def __getstate__(self):
        return (self.tile_char, self.color, self.name)
    
    def __setstate__(self, state):
        (self.tile_char, self.color, self.name) = state