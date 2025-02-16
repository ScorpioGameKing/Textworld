from database._base import Database
from database._queries import Tile as TileQueries
from models import Tile

class TileDatabase(Database):

    # Select tile by ID
    def get_tile(self, tile_char:str) -> Tile:
        try:
            return Tile(*self.execute_one(TileQueries.SELECT_WITH_COLORS_BY_TILE, [tile_char]))
        except: 
            return None
    
    def get_tile_by_noise(self, noise: float) -> Tile:
        try:
            tiles = self.execute_many(TileQueries.SELECT_WITH_COLORS)
            
            for t in tiles:
                if t[2] != None and t[3] != None and t[2] <= noise < t[3]:
                    return Tile(t[0], t[1])
                
        except:
            return None
