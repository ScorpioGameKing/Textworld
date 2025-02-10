import sqlite3
from database._queries import Tile, World, Color
from database._cursor import Cursor

def init(file_name:str = './Data/textworld.db'):
    connection = sqlite3.connect(file_name)
    with Cursor(connection) as cur:
        cur.execute(Color.INIT)
        cur.execute(Tile.INIT)
        cur.execute(World.INIT)
    connection.close()