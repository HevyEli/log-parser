import os
import sys
import time
import json
import datetime
from datetime import datetime
from db import *

def connect_to_db():
        try:
            create_connection(sqlite3_db_file)
            logger.info(f"status: {create_connection}")
            return True
        except Exception as e:
            logger.info(e)
            if create_connection() == False:
                logger.info(f"Not connected!")
            else:
                logger.info(f"Connected!")

        return False



def insert_logs():
    logger.info(f"entering {insert_logs.__name__}")
    # events = []
    """ check if output dir exists if not create directory"""
    dir_isExist = os.path.exists(output_files_directory)
    if dir_isExist != True:
        os.mkdir(output_files_directory)

    conn = create_connection(sqlite3_db_file)
    cursor = conn.cursor()
    insert_statement = "insert into events (event_date, level, file_name, event_message) values (?, ?, ?, ?)"

    with open(read_file, mode='r') as input_file:
        for line in input_file:
            event_list = line.strip().split(" || ")
            if len(event_list) == 4:
                level, file_name, _, event_message = event_list
                cursor.execute(insert_statement, (datetime.now(), level, file_name, event_message))
    conn.commit()
    cursor.close()
    conn.close()
    logger.info(f"exiting {insert_logs.__name__}")


if __name__ == '__main__':

    current_time = datetime.now()
    datetime = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    #windows
    read_file = (r"C:\Users\eliasm1\Documents\learn\python\log-parser\logs\sqllite-python.log")
    output_files_directory = (r"C:\Users\eliasm1\Documents\learn\python\log-parser")
    split_out = (r"C:\Users\eliasm1\Documents\learn\python\log-parser\split_out.txt")


    #linux
    # read_file = "/mnt/c/Users/eliasm1/Documents/learn/python/log-parser/logs/sqllite-python.log"
    # output_files_directory = "/mnt/c/Users/eliasm1/Documents/learn/python/log-parser/output"
    # split_out = "/mnt/c/Users/eliasm1/Documents/learn/python/log-parser/output/split_out.txt"

    connect_to_db()
    insert_logs()