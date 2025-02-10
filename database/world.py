from database._base import IDatabase
import pickle
import gzip
from database._queries import SELECT_SPECIFIC_WORLD, REPLACE_WORLD
class WorldDatabase(IDatabase):

    def save_world_to_db(self, world, save_name:str):
        print(f'SAVING: {world}')
        world_pickle = pickle.dumps(world)
        pickle_zip = gzip.compress(world_pickle)
        cur = self._connection.cursor()
        cur.execute(REPLACE_WORLD, (f'{save_name}', pickle_zip))
        self._connection.commit()
        cur.close()
        #print(pickle_zip, world.world_name, save_name)

    def load_world_from_db(self, save_name:str):
        world = None
        cur = self._connection.cursor()
        db_world = cur.execute(SELECT_SPECIFIC_WORLD, [save_name]).fetchone()
        cur.close()
        print("LOADING SAVE!!!!!!!!!!")
        world_decomp = gzip.decompress(db_world[0])
        world = pickle.loads(world_decomp)
        return world
