from datetime import datetime
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############
from src.classes.db.dbstructurizer import databaseStructurizerReader as dSR
dSR=dSR()()
# database (sqlite3) python3 builtin
from src.classes.db.file.dbloader import DataBaseLoader as DBL
data={"active":False,"data":{}}


class dataBaseClassManager(DBL):
    def __init__(self):
        LMCG().log(type="global").info(f"Initializing DataBase loader.")
        stamp= datetime.now().timestamp()
        super().__init__(str(configData.DATABASE_PATH))
        if not self.dbstorage=={}:
            global data
            for il in self.dbstorage:
                i=self.dbstorage[str(il)]
                if i["loading_status"]==True:
                    self.DATABASE_LOCALDATE=i["DATABASE_LOCALDATE"]
                    self.DATABASE_LOCALDATE_CURSOR=i["DATABASE_LOCALDATE_CURSOR"]
                    self.name=f"[{i['num']}] {i['dbname']}"
                    if self.db_tablechecker():
                        self.__save__()
                        data["data"][str(il)]=i
            data["active"]=True
        else:
            LMCG().log(type="global").error(f"Couldn't find any DataBase files? Status remains unchanged.")
        duration=int(datetime.now().timestamp())-int(stamp)
        LMCG().log(type="global").info(f"DataBase loader has finished in {duration}s.")
    def __save__(self):
        LMCG().log(type="global").debug(f"{self.name} DataBase SQLITE3 is saving...")
        return self.DATABASE_LOCALDATE.commit()

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
                f"{self.name} - Table #{n} (TABLE_NAME: '{table_name}', STRUCTURE: '{structure}'). {status_message}"
            )

        tables_to_drop = set(existing_tables) - set([table[0] for table in dSR])
        for table_to_drop in tables_to_drop:
            self.DATABASE_LOCALDATE_CURSOR.execute(f"DROP TABLE IF EXISTS {table_to_drop};")
            LMCG().log(type="global").warning(
                f"{self.name} - Table {table_to_drop} was dropped."
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

def __load__():
    dataBaseClassManager()