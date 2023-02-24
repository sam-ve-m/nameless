from src.infrastructure.tinydb.infrastructure import TinyDbInfrastructure
from tinydb.table import Table


class TinyDbRepository:
    infrastructure = TinyDbInfrastructure
    table: Table = None
    table_name: str

    @classmethod
    def _get_table(cls) -> Table:
        if not cls.table:
            connection = cls.infrastructure.get_connection()
            cls.table = connection.table(cls.table_name)
        return cls.table
