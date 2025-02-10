from database._base import IDatabase
from database._queries import SELECT_SPECIFIC_TILE

class TileDatabase(IDatabase):

    # Select tile by ID
    def get_tile(self, tile_id:int) -> tuple:
        cur = self._connection.cursor()
        tile = cur.execute(SELECT_SPECIFIC_TILE, [tile_id]).fetchone()
        cur.close()
        return tile[0]