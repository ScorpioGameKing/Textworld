from database._base import IDatabase
import pickle
import gzip
from database._queries import World as WorldQueries
class WorldDatabase(IDatabase):

    def save_world_to_db(self, world, save_name:str):
        print(f'SAVING: {world}')
        world_pickle = pickle.dumps(world)
        pickle_zip = gzip.compress(world_pickle)
        with self.get_cursor() as cur:
            cur.execute(WorldQueries.REPLACE_BY_NAME, (f'{save_name}', pickle_zip))
        #print(pickle_zip, world.world_name, save_name)

    def load_world_from_db(self, save_name:str):
        world = None
        with self.get_cursor() as cur:
            db_world = cur.fetch_one(WorldQueries.SELECT_BY_NAME, [save_name])

        print("LOADING SAVE!!!!!!!!!!")
        world_decomp = gzip.decompress(db_world[0])
        world = pickle.loads(world_decomp)
        return world
