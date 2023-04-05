import logging
import os
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s: {} — %(name)s — %(levelname)s — %(message)s".format(os.getpid()), datefmt='%Y-%m-%d %H:%M:%S')
LOGGER_NAME = 'demo-py'
def get_logger(logger_name=LOGGER_NAME , level = logging.DEBUG):
   logger = logging.getLogger(logger_name)
   logger.setLevel(level)
   handler = logging.StreamHandler()
   handler.setFormatter(FORMATTER)
   logger.addHandler(handler)
   logger.propagate = False
   return logger