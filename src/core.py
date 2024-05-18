from src.classes.wrapper.decorator import TestDecorator
from src.classes.checker.watchdog import watchdog as WG

class Start:
    @TestDecorator(bool(WG()()),"Something went wrong!")
    def __call__(self) -> None:
        import src.imports
        import src.classes.db.dbdatamanager
        import src.classes.configparser.engine
Start()()