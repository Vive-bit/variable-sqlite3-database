import logging
import logging.config

class LoggingManager:
  def __init__(self):
    self.logfile = 'src/data/settings/logging.conf' # path of config file
    self.logger_list = ['root','global']
    # root: global logger used for external libarys
    # global: intern program global logger
    # external package werkzeug: set level to warning so log doesnt get spammed but will log as INFO
    self.loggers = {str(d[0]): d[1] for d in list(self.get_loggers())}
  def start(self):
    for i in self.logger_list:
      self.log(type=i).info("--//-- PROGRAM STARTUP --//--")
  def get_loggers(self):
    logging.config.fileConfig(fname=self.logfile, disable_existing_loggers=False)
    return [[str(i),logging.getLogger(str(i))] for i in self.logger_list]
  def log(self,**kwargs):
      if kwargs["type"]:
        try:
          return self.loggers[kwargs["type"]]
        except KeyError:
          return self.loggers["global"]
      else:
        return self.loggers["global"]
LoggingManager().start()