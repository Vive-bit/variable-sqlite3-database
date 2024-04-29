import sqlite3 as sql
import os
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
# database (sqlite3) python3 builtin


if not os.path.isfile('{}'.format(configData.DATABASE_PATH)):
    LMCG().log(type="global").critical(
        f">> [src.classes.db.dbmanager.py] database file ({configData.DATABASE_PATH}) not found!")
    LMCG().log(type="global").critical(
        f">> [src.classes.db.dbmanager.py] Creating database file in {configData.DATABASE_PATH} > FOLDERS ARE NOT AUTOMATICIALLY CREATED; RESULT IN ERROR")
    pass

try:
    DATABASE_LOCALDATE = sql.connect('{}'.format(configData.DATABASE_PATH), check_same_thread=False)
    LMCG().log(type="global").info(f"[src.classes.db.dbmanager.py] Database was loaded/created!")
except Exception as e:
    LMCG().log(type="global").critical(
        f">> [src.classes.db.dbmanager.py] [!!!] Database couldn't be loaded/created!\n[sqlite3 Database] [WARNING] ERROR: {e}")
    DATABASE_LOCALDATE = None
if os.path.isfile('{}'.format(configData.DATABASE_PATH)):
    LMCG().log(type="global").info(
        f"[src.classes.db.dbmanager.py] {configData.DATABASE_PATH} detected! Loading the Database..")
    pass
else:
    LMCG().log(type="global").critical(f">> [src.classes.db.dbmanager.py] [!!!] {configData.DATABASE_PATH} not detected!")
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
    pass