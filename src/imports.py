### LOGGER IMPORTS ###########
from src.classes.logger.logging import LoggingManager as LMCG
LMCG()
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
configData()
### DATABASE IMPORTS #########
from src.classes.db.dbmanager import dataBaseClassManager as db
db()
from src.classes.db.dbdatamanager import dbDataManager as dDM
dDM()

LMCG.log(type="global").info("Importer starting")

db=dDM
data=configData
log=LMCG
