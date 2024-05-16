import sqlite3 as sql
import os
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
from src.classes.db.file.dbfinder import DataBaseFinder as DBF
# database (sqlite3) python3 builtin

class DataBaseLoader(DBF):
    def __init__(self,x):
        super().__init__(x)
        for x,y in enumerate(self.dbfiles):
            if os.path.isfile(f'{self.DATABASE_PATH}{y}'):
                self.dbstorage[str(y).split(".")[0]]=self.load_db(x+1,y)

    def load_db(self,num:int=None,dbname:str=None,state:bool=False):
        try:
            DATABASE_LOCALDATE = sql.connect(f'{self.DATABASE_PATH}{dbname}', check_same_thread=False)
            DATABASE_LOCALDATE_CURSOR=DATABASE_LOCALDATE.cursor()
            LMCG().log(type="global").info(f"DataBase {dbname} in {self.DATABASE_PATH} | Successfully loaded!")
            state=True
        except Exception as e:
            LMCG().log(type="global").info(f"DataBase {dbname} in {self.DATABASE_PATH} | Incorrectly loaded! Error: {e}")
        return {"loading_status": state,"num":num,"dbname":dbname,"DATABASE_LOCALDATE":DATABASE_LOCALDATE,"DATABASE_LOCALDATE_CURSOR":DATABASE_LOCALDATE_CURSOR}