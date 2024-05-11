import sqlite3 as sql

### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
from src.classes.wrapper.decorator import TestDecorator
from src.classes.db.dbmanager import data as gh
data = gh

class dbDataManager:
    def __save__(self):
        LMCG().log(type="global").debug(f"DataBase SQLITE3 is saving...")
        return data["data"]["DATABASE_LOCALDATE"].commit()

    @TestDecorator(bool(data["active"]),"DataBase is still loading!")
    def __call__(self,record:str=""):
            try:
                x=data["data"]["DATABASE_LOCALDATE_CURSOR"].execute(record)
                if "DELETE" or "INSERT" or "UPDATE" in record:
                    self.__save__()
                if "SELECT" in record:
                    return True,x.fetchall()
                return True
            except Exception as e:
                LMCG().log(type="global").error(f"Record was incorrectly expressed! More details: {e}")
                return False

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