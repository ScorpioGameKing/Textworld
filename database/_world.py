from database._base import Database
import pickle
import logger
from database._queries import World as WorldQueries
class WorldDatabase(Database):

    def save_world_to_db(self, world, save_name:str):
        logger.trace(f'Saving world to database with name {save_name}')
        with self._get_cursor() as cur:
            cur.execute(WorldQueries.REPLACE_BY_NAME, (f'{save_name}', world))

    def load_world_from_db(self, save_name:str):
        logger.trace(f'Loading world from database with name {save_name}')
        world = None
        with self._get_cursor() as cur:
            db_world = cur.fetch_one(WorldQueries.SELECT_BY_NAME, [save_name])
            if not db_world:
                return None

        world = pickle.loads(db_world[0])
        return world

    def delete_world_from_db(self, save_name:str):
        logger.trace(f'Deleting world from database with name {save_name}')
        with self._get_cursor() as cur:
            cur.fetch_one(WorldQueries.DELETE_BY_NAME, [save_name])
            logger.debug(f"DELETED: {save_name}")

    def load_save_names(self):
        logger.trace('Loading save names from database')
        names = []
        with self._get_cursor() as cur:
            name = cur.fetch_many(WorldQueries.SELECT_ALL_NAMES)
            logger.debug(f"FROM DB SELECT_ALL_NAMES: {name}")
            for n in name:
                names.append(n[0])
            return names
