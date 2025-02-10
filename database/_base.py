import sqlite3

class IDatabase():
    _file_name: str = ""
    _connection: sqlite3.Connection = None

    def __init__(self, file_name: str="./Data/textworld.db"):
        self._file_name = file_name

    def open(self):
        self._connection = sqlite3.connect(self._file_name)

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, _, __, ___):
        self.close()
