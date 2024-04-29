### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
LMCG().log(type="global").info("[SETUP] Program initializing...")
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.engine import provider as configData
##############################

print(configData.TEST_INFORMATION)
LMCG().log(type="global").info("zeile 3 code")


import game