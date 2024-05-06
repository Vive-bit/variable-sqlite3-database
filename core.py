### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
LMCG().log(type="global").info("[SETUP] Program initializing...")
### CONFIGPARSER IMPORTS #####
import src.classes.configparser.engine
### DATABASE IMPORTS #########
from src.classes.db.dbmanager import dataBaseClassManager as db
db()
from src.classes.db.dbdatamanager import dbDataManager as dDM
dDM()
##############################



### START main file (for game)
import main
### START game dir ###########
##############################
import src.game




#print(configData.TEST_INFORMATION)
#LMCG().log(type="global").info("zeile 3 code")