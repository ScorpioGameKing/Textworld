import sqlite3, pickle, gzip

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

class SaveDBInterface():
    def __init__(self) -> None:
        con = sqlite3.connect('data\\textworld_world_saves.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS worlds (save_name TEXT PRIMARY KEY, world BLOB)")
        cur.close()
        con.close()

    def saveWorldToDB(self, world, save_name:str):
        print(f'SAVING: {world}')
        world_pickle = pickle.dumps(world)
        pickle_zip = gzip.compress(world_pickle)
        con = sqlite3.connect('data\\textworld_world_saves.db')
        cur = con.cursor()
        cur.execute("REPLACE INTO worlds (save_name, world) VALUES (?, ?)", (f'{save_name}', pickle_zip))
        con.commit()
        cur.close()
        con.close()
        #print(pickle_zip, world.world_name, save_name)

    def loadWorldFromDB(self, save_name:str):
        world = None
        con = sqlite3.connect('data\\textworld_world_saves.db')
        cur = con.cursor()
        db_world = cur.execute("SELECT * FROM worlds").fetchall()
        cur.close()
        con.close()
        for save in db_world:
            if save[0] == save_name:
                print("LOADING SAVE!!!!!!!!!!")
                world_decomp = gzip.decompress(save[1])
                world = pickle.loads(world_decomp)
                print(world)
        return world
