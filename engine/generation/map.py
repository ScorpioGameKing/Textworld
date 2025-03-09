from models import Size, Coords, Tile
from engine.entities import Entity
import numpy as np

class TextworldMap():
    columns: int
    rows: int
    __tiles: dict[Coords, Tile]
    entities: dict[Coords, Entity]
    noise: np.typing.NDArray
    chunk_position: Coords
    
    def __init__(self,chunk_size: Size[int], position: Coords):
        self.rows = chunk_size.height
        self.columns = chunk_size.width
        self.__tiles = {}
        self.entities = {}
        self.noise = np.zeros(shape=(self.rows, self.columns))
        self.chunk_position = position
    
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
        return (self.columns, self.rows, self.__tiles, self.entities, self.chunk_position)
    
    def __setstate__(self, state):
        (self.columns, self.rows, self.__tiles, self.entities, self.chunk_position) = state
        
    def get_entity_coords(self, entity: Entity) -> Coords:
        try:
            return self.entities[Coords(*coords)]
        except:
            return None

    def set_entity_coords(self, coords: Coords, entity: Entity):
        self.entities[Coords(*coords)] = entity

    def update_entity_coords(self, old_coords: Coords, coords: Coords, entity: Entity):
        if self.entities.__contains__(Coords(*old_coords)):
            self.entities.pop(Coords(*old_coords))
        self.entities[Coords(*coords)] = entity

    def delete_entity_coords(self, old_coords: Coords):
        self.entities.pop(Coords(*old_coords))
        