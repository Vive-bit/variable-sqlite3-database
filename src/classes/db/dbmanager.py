import sqlite3 as sql
import os
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
from src.classes.db.dbstructurizer import databaseStructurizerReader as dSR
dSR=dSR()()
# database (sqlite3) python3 builtin

data={"active":False,"data":{}}

if not os.path.isfile('{}'.format(configData.DATABASE_PATH)):
    LMCG().log(type="global").critical(
        f">> Database file ({configData.DATABASE_PATH}) not found!")
    LMCG().log(type="global").critical(
        f">> Creating database file in {configData.DATABASE_PATH} > FOLDERS ARE NOT AUTOMATICIALLY CREATED; RESULT IN ERROR")
    pass

try:
    DATABASE_LOCALDATE = sql.connect('{}'.format(configData.DATABASE_PATH), check_same_thread=False)
    LMCG().log(type="global").info(f"Database was loaded/created!")
except Exception as e:
    LMCG().log(type="global").critical(
        f">> [!!!] Database couldn't be loaded/created!\n[sqlite3 Database] [WARNING] ERROR: {e}")
    DATABASE_LOCALDATE = None
if os.path.isfile('{}'.format(configData.DATABASE_PATH)):
    LMCG().log(type="global").info(
        f"{configData.DATABASE_PATH} detected! Loading the Database..")
    pass
else:
    LMCG().log(type="global").critical(f">> [!!!] {configData.DATABASE_PATH} not detected!")
    pass
try:
    DATABASE_LOCALDATE_CURSOR = DATABASE_LOCALDATE.cursor()
except:
    DATABASE_LOCALDATE_CURSOR = None



class check:
    def __call__(self):
        return {"status": True if not DATABASE_LOCALDATE == None else False}  # dbmstat class; ignore


def get_db_contents():
    DATABASE_LOCALDATE_CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = DATABASE_LOCALDATE_CURSOR.fetchall()

    # Für jede Tabelle den Inhalt abrufen und in die Textdatei schreiben
    with open("table_contents.txt", "w") as output_file:
        for table in table_names:
            table_name = table[0]
            output_file.write(f"Inhalt der Tabelle '{table_name}':\n")

            # Inhalt der Tabelle abrufen
            DATABASE_LOCALDATE_CURSOR.execute(f"SELECT * FROM {table_name};")
            rows = DATABASE_LOCALDATE_CURSOR.fetchall()

            # Inhalt in die Textdatei schreiben
            for row in rows:
                output_file.write(str(row) + '\n')
        output_file.close()

    print("Inhalte wurden in 'table_contents.txt' gespeichert.")


# get_db_contents()
# AKTIVIEREN DIESER FUNKTION SCHREIBT ALLE DATEN DER DATENBANK AUS


class dataBaseClassManager:
    def __init__(self):
        self.DATABASE_LOCALDATE_CURSOR = DATABASE_LOCALDATE_CURSOR
        self.DATABASE_LOCALDATE = DATABASE_LOCALDATE
        if self.status:
            LMCG().log(type="global").info(f"DataBase SQLITE3 seems all fine, initializing Tablechecker...")
            if self.db_tablechecker():
                self.__save__()
                LMCG().log(type="global").info(f"Looks alright, getting dbDataManager ready...")
                global data
                data={"active":True,"data":{"DATABASE_LOCALDATE_CURSOR":self.DATABASE_LOCALDATE_CURSOR,"DATABASE_LOCALDATE":self.DATABASE_LOCALDATE}}

    def __save__(self):
        LMCG().log(type="global").debug(f"DataBase SQLITE3 is saving...")
        return self.DATABASE_LOCALDATE.commit()
    @property
    def status(self)-> bool:
        if check()()["status"] == False:
            LMCG().log(type="global").critical(
                f"[TABLECHECKER] [FATAL ERROR] [!!!] Database was never loaded!")
            return False
        return True

    def db_tablechecker(self) -> bool:
        tables = self.DATABASE_LOCALDATE_CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        existing_tables = [table[0] for table in tables]

        for n, (table_name, structure) in enumerate(dSR, 1):
            if table_name not in existing_tables:
                self.create_db_table_(table_name, structure)
                status_message = 'Table just created.'
            else:
                status_message = 'Table already exists. No new table was created.'
            LMCG().log(type="global").info(
                f"[TABLECHECKER] - Table #{n} (TABLE_NAME: '{table_name}', STRUCTURE: '{structure}'). {status_message}"
            )

        tables_to_drop = set(existing_tables) - set([table[0] for table in dSR])
        for table_to_drop in tables_to_drop:
            self.DATABASE_LOCALDATE_CURSOR.execute(f"DROP TABLE IF EXISTS {table_to_drop};")
            LMCG().log(type="global").warning(
                f"[TABLECHECKER] - Table {table_to_drop} was dropped."
            )
        return True
        ############################
        # database function (accessing and more..)

    def check_db_table_(self, name) -> bool:
        try:
            listOfTables = self.DATABASE_LOCALDATE_CURSOR.execute(
                """SELECT name FROM sqlite_master WHERE type='table' AND name='{}'""".format(name)).fetchall()
        except:
            return True
        if listOfTables == []:
            return False
        else:
            return True
    def create_db_table_(self, name:str, structure:str) -> bool:
        resl = self.check_db_table_(name)
        if resl == False:
            self.DATABASE_LOCALDATE_CURSOR.execute("""CREATE TABLE {} ({})""".format(str(name),str(structure)))
            return True
        else:
            return False
    ############################