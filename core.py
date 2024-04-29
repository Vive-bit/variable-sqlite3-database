### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
LMCG().log(type="global").info("[SETUP] Program initializing...")
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################
### DATABASE IMPORTS #########
from src.classes.db.dbmanager import dataBaseClassManager as db
##############################
import src.classes.db.dbmanager

import main

### START game dir ###########
import game
##############################

#print(configData.TEST_INFORMATION)
#LMCG().log(type="global").info("zeile 3 code")


