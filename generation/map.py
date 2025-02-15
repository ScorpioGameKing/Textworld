
from models import Size, Coords, Tile
import numpy as np


class TextworldMap():
    columns: int
    rows: int
    __tiles: dict[Coords, Tile]
    noise: np.typing.NDArray
    
    
    def __init__(self,chunk_size: Size[int]):
        self.rows = chunk_size.height
        self.columns = chunk_size.width
        self.__tiles = {}
        self.noise = np.zeros(shape=(self.rows, self.columns))
    
    def __getitem__(self, coords: tuple[int,int]) -> Tile:
        return self.__tiles.get(Coords.from_tuple(coords), None)
    
    def __setitem__(self, coords: tuple[int,int], tile: Tile):
        self.__tiles[Coords.from_tuple(coords)] = tile