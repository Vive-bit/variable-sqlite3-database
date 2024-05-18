class DataBaseStructure(object):
    def __init__(self,path:str):
        self.DATABASE_PATH:str=path
        self.dbfiles = []
        self.dbstorage = {}
    def __repr__(self):
        return "The DataBase manager"