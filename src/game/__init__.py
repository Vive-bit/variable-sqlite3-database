# Import Libraries
import os
import importlib
from src.classes.logger.logging import LoggingManager as LMCG
# Get all files.
views = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".py") and f != "__init__.py"]
LMCG().log(type="global").info(f"[game.__init__.py] Fetched components: {', '.join(views)}")
# Import all files from modules folder.

# IMPORTANT:
# filesystem / : importlib.import_module(os.path.dirname(os.path.realpath(__  file__)).split('/')[-1] + "." + view[:-3])
# filesystem \ : importlib.import_module(os.path.dirname(os.path.realpath(__file__)).split('\\')[-1] + "." + view[:-3])
for view in views:
  try:
    importlib.import_module("src."+os.path.dirname(os.path.realpath(__file__)).split('/')[-1] + "." + view[:-3])
    LMCG().log(type="global").info(f"[game.__init__.py] TYPE1 - Successfully imported component: {view}")
  except Exception as e:
    #LMCG().log(type="global").error(f"[game.__init__.py] [ERROR] Failed to import component: {view} | Error: {e} [TRYING AGAIN WITH OTHER FILE SYSTEM]")
    try:
      importlib.import_module("src."+os.path.dirname(os.path.realpath(__file__)).split('\\')[-1] + "." + view[:-3])
      LMCG().log(type="global").info(f"[game.__init__.py] TYPE2 - Successfully imported component: {view}")
    except Exception as e:
      LMCG().log(type="global").critical(f"[game.__init__.py] [ERROR] Failed to import component: {view} | Error: {e}")