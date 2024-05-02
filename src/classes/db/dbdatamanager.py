import sqlite3 as sql

### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
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
    def t(self):
        if not self.locked:
            print("ok")
            return
        print("no")