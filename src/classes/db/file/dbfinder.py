import os

class DataBaseFinder(object):
    def __init__(self,path:str):
        self.DATABASE_PATH:str=path
        self.dbfiles = []
        self.dbstorage = {}
        self.get_db()
    def get_db(self):
        for x,y in enumerate(os.listdir(self.DATABASE_PATH)):
            if str(y).endswith(".db") and not str(y) in self.dbfiles:
                self.dbfiles.append(y)