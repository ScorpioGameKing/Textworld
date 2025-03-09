from database._base import Database
from database._queries import Color as ColorQueries
import logger

class ColorDatabase(Database):
    def get_color_by_id(self, color_id: int):
        logger.trace(f'Getting color with id {color_id}')
        return self.execute_one(ColorQueries.SELECT_BY_ID, [color_id])
            