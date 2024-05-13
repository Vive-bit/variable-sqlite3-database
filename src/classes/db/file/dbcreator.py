from src.classes.configparser.engine import provider as configData
from src.classes.logger.logging import LoggingManager as LMCG
def create_db(name:str=None):
    path:str=f"{str(configData.DATABASE_PATH)}{name}.db"
    with open(path,"w") as f:
        f.close()
    LMCG().log(type="global").info(f"new DataBase {name}.db created.")
    return True