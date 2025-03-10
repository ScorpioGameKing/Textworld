from engine.database._base import Database
from engine.database._queries import Mobs as MobQueries
from engine.database._queries import Players as PlayerQueries
from engine.entities import Player, Mob
from models import Tile, Coords, Size
import logger

class EntityDatabase(Database):

    def select_mob_by_name(self, name:str):
        logger.trace(f'Getting Mob by Name: {name}')
        try:
            print(self.execute_one(MobQueries.SELECT_BY_NAME, [name]))
            mob_props = self.execute_one(MobQueries.SELECT_BY_NAME, [name])
            return Mob(Tile(mob_props[0], mob_props[2], mob_props[1], Coords(0, 0)), Size(mob_props[3], mob_props[4]), mob_props[5], mob_props[6], mob_props[7], mob_props[8])
        except:
            return None