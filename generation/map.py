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
    
    def __getitem__(self, __slice: tuple[int,int] | slice):
        if getattr(__slice, 'start', None):
            start = __slice.start
            stop = __slice.stop
            rows = []
            for y in range(start[1], stop[1]):
                row = []
                for x in range(start[0], stop[0]):
                    row.append(self.__tiles[Coords(x,y)])
                rows.append(row)
            return rows
                     
        else:
            return self.__tiles.get(Coords.from_tuple(__slice), None)
    
    def __setitem__(self, coords: tuple[int,int], tile: Tile):
        self.__tiles[Coords.from_tuple(coords)] = tile

    def __getstate__(self):
        return (self.columns, self.rows, self.__tiles)
    
    def __setstate__(self, state):
        (self.columns, self.rows, self.__tiles) = state