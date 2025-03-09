import logger
import sqlite3
from typing import Any

class Cursor:
    __connection: sqlite3.Connection
    __cursor: sqlite3.Cursor = None
    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()

    def fetch_one(self, query, params=()) -> Any:
        logger.trace(f'Executing {query}with\n {params}')
        self.__cursor.execute(query, params)
        self.__connection.commit()
        return self.__cursor.fetchone()
    
    def fetch_many(self, query, params=(), amount=-1) -> list:
        logger.trace(f'Executing {query}with\n {params}\nexpected return amount {amount}')
        
        self.__cursor.execute(query, params)
        return self.__cursor.fetchmany(size=amount)
    
    def execute(self, query, params=()) -> None:
        logger.trace(f'Executing {query}with\n {params}')
        self.__cursor.execute(query, params)
        self.__connection.commit()
