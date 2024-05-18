import os
from src.classes.db.file.dbstruct import DataBaseStructure as DBS
class DataBaseFinder(DBS):
    def __init__(self,x):
        super().__init__(x)
        self.get_db()

    def get_db(self):
        for x,y in enumerate(os.listdir(self.DATABASE_PATH)):
            if str(y).endswith(".db") and not str(y) in self.dbfiles:
                self.dbfiles.append(y)