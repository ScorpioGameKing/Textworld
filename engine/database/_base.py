import logger
import sqlite3
from engine.database._cursor import Cursor
from engine.database._functions import load_world, store_world
import os


class Database():
    __file_name: str = ""
    __connection: sqlite3.Connection = None
    is_open: bool = False

    def __init__(self, file_name: str="./Data/textworld.db"):
        if not os.path.exists(file_name):
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
        self.__file_name = file_name
        
    def __del__(self):
        self.close()

    def open(self):
        logger.trace(f'Opening database connecton at file {self.__file_name}')
        try:
            self.__connection = sqlite3.connect(self.__file_name)
            self.__connection.isolation_level = None
            self.__connection.create_function('load_world', 1, load_world)
            self.__connection.create_function('store_world', 1, store_world)
            self.is_open = True
        except FileNotFoundError:
            logger.error(f'File {self.__file_name} not found')


    def close(self):
        logger.trace('Closing database connection')
        if self.__connection:
            self.__connection.close()
            self.__connection = None
            self.is_open = False
            
    def init_db(self, *initalization_queries: list[str]):
        logger.trace('Initializing database')
        with self._get_cursor() as cur:
            for q in initalization_queries:
                cur.execute(q)
            
    def _get_cursor(self):
        return Cursor(self.__connection)
            
    def execute_one(self, query: str, params: tuple = ()):
        logger.trace(f'Executing query on database {self.__file_name}')
        with self._get_cursor() as cur:
            return cur.fetch_one(query, params=params)
        
    def execute_many(self, query: str, params: tuple = (), amount: int = -1):
        logger.trace(f'Executing query on database {self.__file_name}')
        with self._get_cursor() as cur:
            return cur.fetch_many(query, params=params, amount=amount)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, _, __, ___):
        self.close()
