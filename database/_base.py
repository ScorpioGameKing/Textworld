import sqlite3
from database._cursor import Cursor
from database._functions import load_world, store_world
import os


class Database():
    _file_name: str = ""
    _connection: sqlite3.Connection = None

    def __init__(self, file_name: str="./Data/textworld.db"):
        if not os.path.exists(file_name):
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
        self._file_name = file_name
        
    def __del__(self):
        self.close()

    def open(self):
        self._connection = sqlite3.connect(self._file_name)
        self._connection.isolation_level = None
        self._connection.create_function('load_world', 1, load_world)
        self._connection.create_function('store_world', 1, store_world)
        
        # self._connection.create_function('gzcompress', 1, gzip.compress)
        # self._connection.create_function('gzdecompress', 1, gzip.decompress)

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None
            
    def init_db(self, *initalization_queries: list[str]):
        with self.get_cursor() as cur:
            for q in initalization_queries:
                cur.execute(q)
            
    def get_cursor(self):
        return Cursor(self._connection)
            
    def execute_one(self, query: str, params: tuple = ()):
        with self.get_cursor() as cur:
            return cur.fetch_one(query, params=params)
        
    def execute_many(self, query: str, params: tuple = (), amount: int = -1):
        with self.get_cursor() as cur:
            return cur.fetch_many(query, params=params, amount=amount)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, _, __, ___):
        self.close()
