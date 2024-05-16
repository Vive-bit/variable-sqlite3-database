from src.classes.logger.logging import LoggingManager as LMCG
class FailureCounter:

    def __init__(self, message):
        self.message = message
        self.function = None
        self.failcount = 0

    def __call__(self, func):
        self.function = func
        return self.safe_call

    def safe_call(self, *args):
        try:
            self.function(*args)
        except Exception as e:
            self.failcount += 1
            LMCG().log(type="global").error(f"Error detected. Fail #{self.failcount}, Function: {self.function.__name__}, Message: {self.message}, Error: {e}")