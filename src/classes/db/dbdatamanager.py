import sqlite3 as sql

### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
from src.classes.wrapper.decorator import TestDecorator
from src.classes.db.dbmanager import data as data
class dbDataManager:
    def __init__(self):
        self.pointer=None
    def __repr__(self):
        return f"Currently operating with pointer: {self.pointer}. Database availability status: {self.aloader}"
    @property
    def aloader(self):
        return False if not self.pointer or not bool(data["active"]) else True
    @property
    def name(self):
        if self.aloader:
            return f"[{data['data'][self.pointer]['num']}] {data['data'][self.pointer]['dbname']}"
        else:
            return False, "Pointer was not set / database is not ready"
    def __save__(self):
        if self.aloader:
            LMCG().log(type="global").debug(f"{self.name} DataBase SQLITE3 is saving...")
            return True, data["data"][self.pointer]["DATABASE_LOCALDATE"].commit()
        else:
            return False, "Pointer was not set / database is not ready"

    @TestDecorator(bool(data["active"]),"DataBase loader not ready!")
    def execute(self,record:str=""):
        if self.aloader and not record=="":
            try:
                x=data["data"][self.pointer]["DATABASE_LOCALDATE_CURSOR"].execute(record)
                if "DELETE" or "INSERT" or "UPDATE" in record:
                    self.__save__()
                if "SELECT" in record:
                    return True,x.fetchall()
                return True, "Job finished."
            except Exception as e:
                LMCG().log(type="global").error(f"{self.name} Error detected! More details: {e}")
                return False,f"{self.name} Error detected! More details: {e}"
        else:
            return False, "Please point to a database first!"

    @TestDecorator(bool(data["active"]), "DataBase loader not ready!")
    def point(self, record: str = None):
        if not record==None:
            if str(record) in data["data"].keys():
                if data["data"][record]["loading_status"]==True:
                    self.pointer=str(record)
                    LMCG().log(type="global").info(f"Now pointing to {record} (Fetch: {self.name}).")
                    return True, "Job finished."
                else:
                    LMCG().log(type="global").error(f"DataBase {record} is not ready.")
                    return False,f"DataBase {record} is not ready."
            else:
                LMCG().log(type="global").error(f"Record was incorrectly expressed! DataBase does not exist.")
                return False,"Record was incorrectly expressed! DataBase does not exist."
        else:
            LMCG().log(type="global").info(f"Pointer was reset.")
            self.pointer=None
            return True, "Job finished."

'''
DELETE from {} WHERE id={} AND type='{}'
UPDATE {} SET content='{}' WHERE id={} AND type='{}'
INSERT INTO {} VALUES ({}, '{}', '{}')
SELECT * FROM {} WHERE id={} AND type='{}'

from src.classes.db.dbdatamanager import dbDataManager as dDM
dDM=dDM()

x=dDM("""SELECT * FROM {}""".format("db_table_a"))
y=dDM("""INSERT INTO {} VALUES ({})""".format("db_table_a",13))
z=dDM("""SELECT * FROM {}""".format("db_table_a"))
print(x)
print(y)
print(z)
'''

