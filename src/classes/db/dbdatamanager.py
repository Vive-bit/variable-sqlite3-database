import sqlite3 as sql

### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
from src.classes.wrapper.decorator import TestDecorator

data = {"locked":True,"data": {}}

class dbDataManager:
    def __init__(self):
        self.locked=bool(data["locked"])
        if not bool(data["locked"])==True:
            self.DATABASE_LOCALDATE_CURSOR = data["data"]["DATABASE_LOCALDATE_CURSOR"]
            self.DATABASE_LOCALDATE = data["data"]["DATABASE_LOCALDATE"]
    def __save__(self):
        LMCG().log(type="global").debug(f"DataBase SQLITE3 is saving...")
        return self.DATABASE_LOCALDATE.commit()

    def check_db_table_(self, tablename:str):
        try:
            listOfTables = self.DATABASE_LOCALDATE_CURSOR.execute(
                """SELECT name FROM sqlite_master WHERE type='table' AND name='{}'""".format(tablename)).fetchall()
        except:
            return True
        if listOfTables == []:
            return False
        else:
            return True

    @TestDecorator(lambda self: self.locked,"DataBase is still loading!")
    def __call__(self,record:str="") -> bool:
            try:
                self.DATABASE_LOCALDATE_CURSOR.execute(record)
            except Exception as e:
                LMCG().log(type="global").error(f"Record was incorrectly expressed! More details: {e}")
                return False
            return True

'''
DELETE from {} WHERE id={} AND type='{}'
UPDATE {} SET content='{}' WHERE id={} AND type='{}'
INSERT INTO {} VALUES ({}, '{}', '{}')
SELECT * FROM {} WHERE id={} AND type='{}'

from src.classes.db.dbdatamanager import dbDataManager as dDM
dDM()

dDM("""SELECT""",format())
'''