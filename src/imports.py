### IMPORTS ###########
from src.classes.logger.logging import LoggingManager as LMCG
from src.classes.configparser.engine import provider as configData
from src.classes.db.dbdatamanager import dbDataManager as dDM

db=dDM()
data=configData()
log=LMCG()

'''
print(db.point("base64"))
print(db.execute("SELECT * FROM money"))
import src.classes.db.file.dbcreator as c
c.create_db("base64")
import src.classes.db.dbmanager as dbm
dbm.__load__()
print(db.point("base64"))
print(db.execute("SELECT * FROM money"))
'''