from database._base import Database
from database._queries import Tile as TileQueries

class TileDatabase(Database):

    # Select tile by ID
    def get_tile(self, tile_char:str) -> tuple:
        return self.execute_one(TileQueries.SELECT_WITH_COLORS_BY_TILE, [tile_char])
    
    def get_tile_by_noise(self, noise: float) -> tuple:
        self.execute_one(TileQueries.SELECT_WITH_COLORS_BY_NOISE, [noise, noise])