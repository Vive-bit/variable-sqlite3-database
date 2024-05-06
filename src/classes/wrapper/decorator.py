### LOGGER SETUP #############
from src.classes.logger.logging import LoggingManager as LMCG
###############

class TestDecorator:
    def __init__(self, func, msg:str="No error message provided."):
        self.test_func = func
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.test_func:
                return func(*args, **kwargs)
            else:
                LMCG().log(type="global").warning(self.msg)
        return wrapper