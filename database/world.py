from database._base import Database
import pickle
import gzip
from database._queries import World as WorldQueries
class WorldDatabase(Database):

    def save_world_to_db(self, world, save_name:str):
        # print(f'SAVING: {world}')
        # world_pickle = pickle.dumps(world)
        # pickle_zip = gzip.compress(world_pickle)
        with self.get_cursor() as cur:
            cur.execute(WorldQueries.REPLACE_BY_NAME, (f'{save_name}', world))
        #print(pickle_zip, world.world_name, save_name)

    def load_world_from_db(self, save_name:str):
        world = None
        with self.get_cursor() as cur:
            db_world = cur.fetch_one(WorldQueries.SELECT_BY_NAME, [save_name])
            if not db_world:
                return None

        print("LOADING SAVE!!!!!!!!!!")
        world = pickle.loads(db_world[0])
        return world
