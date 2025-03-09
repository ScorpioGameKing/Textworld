from engine.database._base import Database
from engine.database._queries import Tile as TileQueries
from models import Tile, Coords
import logging

class TileDatabase(Database):

    # Select tile by ID
    def get_tile(self, tile_char:str) -> Tile:
        try:
            return Tile(*self.execute_one(TileQueries.SELECT_WITH_COLORS_BY_TILE, [tile_char]))
        except: 
            return None
    
    def get_tile_by_noise(self, noise: float) -> Tile:
        try:
            tiles = self.execute_many(TileQueries.SELECT_ALL)
            #logging.debug(f"Tiles: {tiles}")
            for t in tiles:
                if t[2] != None and t[3] != None and t[2] <= noise < t[3]:
                    return Tile(t[0], t[4], t[1], Coords(0, 0))
                
        except:
            logging.debug(f"FAILED TO GET TILE WITH NOISE: {noise}")
            return None
