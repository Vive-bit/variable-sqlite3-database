import configparser
config = configparser.ConfigParser()
config.read("src/data/settings/config.ini") # i am too dumb to put it in a file because that wouldn't look professional enough uwu

"""
### CONFIGPARSER IMPORTS #####
from src.classes.configparser.fetch import provider as configData
##############################
"""

class provider:
    DATABASE_PATH = str(config.get("DATABASE", "DATABASE_PATH"))