### LOGGER IMPORTS ###########
from src.classes.logger.logging import LoggingManager as LMCG
LMCG()
from src.classes.configparser.engine import provider as configData
from src.classes.db.dbdatamanager import dbDataManager as dDM

LMCG.log(type="global").info("Importer starting")

db=dDM()
data=configData()
log=LMCG
