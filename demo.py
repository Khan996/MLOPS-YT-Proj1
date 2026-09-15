# # below code is to check the logging file 

# from src.logger import logging

# logging.debug("This is a DEBUG message.")
# logging.info("This is an INFO message")
# logging.warning("This is a WARNING message")
# logging.error("This is an ERROR message")
# logging.critical("This is a CRITICAL message")

# below code is to check the exception file 

from src.exception import MyException
from src.logger import logging 
import sys

try:
    a = 1 +'Z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e 