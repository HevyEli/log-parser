import os
import datetime
from datetime import datetime
import logging


def cust_logger():
    logfile = "/mnt/c/Users/eliasm1/Documents/learn/python/sqllite-python.log_new"
    logger = logging.basicConfig(level=logging.DEBUG, 
                        format='%(levelname)s: || file name: %(filename)s.%(funcName)s - line: %(lineno)d || date: || %(asctime)s: || message: %(message)s',
                        handlers=[
                            logging.FileHandler(filename=logfile, mode="a"),
                            logging.StreamHandler()
                        ])
    logger = logging.getLogger(name='python')
    return logger