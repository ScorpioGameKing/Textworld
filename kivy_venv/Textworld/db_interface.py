import sqlite3

# Used to connect and interact with the tile database
class TileDBInterface():
    def __init__(self) -> None:
        con = sqlite3.connect('Data\\textworld_tiles.db')
        cur = con.cursor()
        # Eventually make this more "global"
        self.tile_db = cur.execute("SELECT * FROM tiles").fetchall()
        cur.close()
        con.close()

    # Select tile by ID
    def getTile(self, id:int) -> tuple:
        for tile in self.tile_db:
            if tile[0] == id:
                return tile
        return ()
