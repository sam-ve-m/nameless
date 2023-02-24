import os

from tinydb import TinyDB


class TinyDbInfrastructure:
    _connection: TinyDB = None

    @classmethod
    def get_connection(cls) -> TinyDB:
        if cls._connection is None:
            path = os.path.join("src", "static", "tinydb", "db.json")
            cls._connection = TinyDB(path)
        return cls._connection
