from database import TileDatabase

class TileBuilder():
    db: TileDatabase
    def __init__(self):
        self.db = TileDatabase()
        self.db.open()
