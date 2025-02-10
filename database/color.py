from database._base import IDatabase

class ColorDatabase(IDatabase):
    def get_color_by_id(self, color_id: int):
        with self.get_cursor() as cur:
            return cur.fetch_one('SELECT * FROM colors WHERE cid = ?', [color_id])
            