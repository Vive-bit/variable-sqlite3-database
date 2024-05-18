from datetime import datetime
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
from typing import Dict, Any, Union, Tuple
from functools import lru_cache, cached_property
from src.classes.db.dbstructurizer import databaseStructurizerReader as dSR
dSR=dSR()()
# database (sqlite3) python3 builtin
from src.classes.db.file.dbloader import DataBaseLoader as DBL
data={"active":False,"data":{}}

class DatabaseRegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.registry[name] = new_class
        return new_class

class BaseModel(metaclass=DatabaseRegistryMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__class__.__annotations__:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Unknown attribute: {key}")

    def __repr__(self):
        attrs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class dataBaseClassManager(DBL, BaseModel):
    dbstorage: Dict[str, Any] = {}
    logger = LMCG().log(type="global")

    def __init__(self):
        self.logger.info("Initializing DataBase loader.")
        stamp = datetime.now().timestamp()

        super().__init__(configData.DATABASE_PATH)
        if self.dbstorage:
            global data
            for db_key, db_info in self.dbstorage.items():
                if db_info["loading_status"]:
                    self._setup_db_info(db_info, db_key)
            data["active"] = True
        else:
            self.logger.error("Couldn't find any DataBase files? Status remains unchanged.")

        duration = int(datetime.now().timestamp()) - int(stamp)
        self.logger.info(f"DataBase loader has finished in {duration}s.")

    def _setup_db_info(self, db_info: Dict[str, Any], db_key: str):
        self.DATABASE_LOCALDATE = db_info["DATABASE_LOCALDATE"]
        self.DATABASE_LOCALDATE_CURSOR = db_info["DATABASE_LOCALDATE_CURSOR"]
        self.name = f"[{db_info['num']}] {db_info['dbname']}"
        if self.db_tablechecker():
            self.__save__()
            data["data"][db_key] = db_info

    def __save__(self):
        self.logger.debug(f"{self.name} DataBase SQLITE3 is saving...")
        self.DATABASE_LOCALDATE.commit()

    def db_tablechecker(self) -> bool:
        tables = self._fetch_tables()
        existing_tables = {table[0] for table in tables}

        for n, (table_name, structure) in enumerate(dSR, 1):
            status_message = self._process_table(table_name, structure, existing_tables)
            self.logger.info(
                f"{self.name} - Table #{n} (TABLE_NAME: '{table_name}', STRUCTURE: '{structure}'). {status_message}"
            )

        self._drop_obsolete_tables(existing_tables)
        return True

    def _fetch_tables(self) -> list:
        return self.DATABASE_LOCALDATE_CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

    def _process_table(self, table_name: str, structure: str, existing_tables: set) -> str:
        if table_name not in existing_tables:
            self.create_db_table_(table_name, structure)
            return 'Table just created.'
        return 'Table already exists. No new table was created.'

    def _drop_obsolete_tables(self, existing_tables: set):
        tables_to_drop = existing_tables - {table[0] for table in dSR}
        for table_to_drop in tables_to_drop:
            self.DATABASE_LOCALDATE_CURSOR.execute(f"DROP TABLE IF EXISTS {table_to_drop};")
            self.logger.warning(f"{self.name} - Table {table_to_drop} was dropped.")

    def check_db_table_(self, name) -> bool:
        try:
            listOfTables = self.DATABASE_LOCALDATE_CURSOR.execute(
                """SELECT name FROM sqlite_master WHERE type='table' AND name=?""", (name,)
            ).fetchall()
        except Exception as e:
            self.logger.error(f"Error checking table {name}: {e}")
            return True
        return bool(listOfTables)

    def create_db_table_(self, name: str, structure: str) -> bool:
        if not self.check_db_table_(name):
            self.DATABASE_LOCALDATE_CURSOR.execute(f"CREATE TABLE {name} ({structure})")
            return True
        return False

    @staticmethod
    def log_db_status(status: str):
        LMCG().log(type="global").info(status)

    @cached_property
    def table_count(self) -> int:
        return len(self._fetch_tables())


def __load__():
    dataBaseClassManager()
