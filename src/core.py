from src.classes.wrapper.decorator import TestDecorator
from src.classes.checker.watchdog import watchdog as WG

class Start:
    @TestDecorator(bool(WG()()),"Something went wrong!")
    def __call__(self) -> None:
        from src.classes.logger.logging import LoggingManager as LMCG
        LMCG().log(type="global").info("[SETUP] Program initializing...")
        import src.classes.db.dbmanager as dbm
        dbm.__load__()
        import src.classes.db.dbdatamanager
        import src.classes.configparser.engine
        import src.imports
        import main
        import src.game
Start()()