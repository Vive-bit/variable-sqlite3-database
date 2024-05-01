import json
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############

class databaseStructurizerReader:
    def __init__(self):
        self.path = configData.DATABASE_STRUCTURE_PATH
        self.content = self.read
        LMCG().log(type="global").info(
            f"DataBase SQLITE3 structure was loaded ({self.path})")
        LMCG().log(type="global").debug(
            f"DataBase SQLITE3 structure loaded: ({self.read})")
    @property
    def read(self):
        with open(self.path, 'r') as f:
            data = f.read()
        return json.loads(data)["structures"]
    def __call__(self):
        return self.content