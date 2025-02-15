from database._base import Database
from database._queries import Color as ColorQueries

class ColorDatabase(Database):
    def get_color_by_id(self, color_id: int):
        return self.execute_one(ColorQueries.SELECT_BY_ID, [color_id])
            