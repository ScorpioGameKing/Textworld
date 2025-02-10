from database._base import IDatabase
from database._queries import Tile as TileQueries

class TileDatabase(IDatabase):

    # Select tile by ID
    def get_tile(self, tile_id:int) -> tuple:
        return self.execute_one(TileQueries.SELECT_WITH_COLORS_BY_ID, [tile_id])