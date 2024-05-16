from src.classes.logger.logging import LoggingManager as LMCG
LMCG().log(type="global").info("[SETUP] Program initializing...")
import src.classes.db.dbmanager as dbm
dbm.__load__()
### IMPORTS ###########
from src.classes.logger.logging import LoggingManager as LMCG
from src.classes.configparser.engine import provider as configData
from src.classes.db.dbdatamanager import dbDataManager as dDM
from src.classes.db.face.easydb import translator as T

easydb=T()
db=dDM()
data=configData()
log=LMCG()
'''
import src.classes.db.file.dbcreator as c
c.create_db("base64")
import src.classes.db.dbmanager as dbm
dbm.__load__()

geld=7000


db.point("test")

geld_hinzufügen=db.execute("""UPDATE money SET zahl={}""".format(geld))
geld_auslesen=db.execute("""SELECT * FROM money""")[1][0][0]
print(geld_hinzufügen)
print(geld_auslesen)

'''
















