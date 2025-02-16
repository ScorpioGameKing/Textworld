from database._base import Database
from database._queries import Tile as TileQueries

class TileDatabase(Database):

    def get_tile_by_tile_char(self, tile_char:str) -> tuple:
        return self.execute_one(TileQueries.SELECT_WITH_COLORS_BY_TILE, [tile_char])
    
    def get_tile_by_noise(self, noise: float) -> tuple:
        self.execute_one(TileQueries.SELECT_WITH_COLORS_BY_NOISE, [noise, noise])