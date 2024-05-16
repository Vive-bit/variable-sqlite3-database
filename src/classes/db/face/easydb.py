from src.classes.db.dbdatamanager import dbDataManager as dDB
from src.classes.db.dbmanager import data as data
from src.classes.wrapper.decorator import TestDecorator
class translator(dDB):
    def __init__(self):
        super().__init__()

    def change_str(self,table:str,value:str):
        x=self.execute("""SELECT * FROM {}""".format(table))
        if bool(x[0]):
            if x[1]==[]:
                return self.execute("""INSERT INTO {} VALUES ('{}')""".format(table,value))
            else:
                return self.execute("""UPDATE {} SET istwert='{}'""".format(table,value))
        else:
            return False, "Sorry, execution was invalid."
    def change_int(self,table:str,value:int):
        x=self.execute("""SELECT * FROM {}""".format(table))
        if bool(x[0]):
            if x[1]==[]:
                return self.execute("""INSERT INTO {} VALUES ({})""".format(table,value))
            else:
                return self.execute("""UPDATE {} SET istwert={}""".format(table,value))
        else:
            return False, "Sorry, execution was invalid."
    def read_(self,table:str):
        x=self.execute("""SELECT * FROM {}""".format(table))
        if bool(x[0]):
            return True, x[1]
        else:
            return False, "Sorry, execution was invalid."
    def delete_(self,table:str):
        x=self.execute("""SELECT * FROM {}""".format(table))
        if bool(x[0]):
            if x[1]==[]:
                return False, "Already deleted"
            else:
                return self.execute("""DELETE from {}""".format(table))
        else:
            return False, "Sorry, execution was invalid."

    @TestDecorator(bool(data["active"]), "DataBase loader not ready!")
    def send(self,action:str=None,tx:str=None,table:str=None,value=None):
        if self.aloader:
            if action=="ISTWERT" and tx=="str":
                return self.change_str(table,value)
            elif action=="ISTWERT" and tx=="int":
                return self.change_int(table,value)
        else:
            return False, "Sorry, database is not ready."

    @TestDecorator(bool(data["active"]), "DataBase loader not ready!")
    def read(self, table: str = None):
        if self.aloader:
            result=self.read_(table)
            return result[1] if result[0]==True else result
        else:
            return False, "Sorry, database is not ready."

    @TestDecorator(bool(data["active"]), "DataBase loader not ready!")
    def delete(self, table: str = None):
        if self.aloader:
            return self.delete_(table)
        else:
            return False, "Sorry, database is not ready."