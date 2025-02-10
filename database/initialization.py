import sqlite3
from database._queries import INIT_COLOR, INIT_TILE, INIT_WORLD


def init(file_name:str = './Data/textworld.db'):
    connection = sqlite3.connect(file_name)
    cur = connection.cursor()
    cur.execute(INIT_COLOR)
    cur.execute(INIT_TILE)
    cur.execute(INIT_WORLD)
    connection.commit()
    connection.close()