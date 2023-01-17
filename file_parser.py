import os
import sys
import time
import json
import datetime
from datetime import datetime
from db import *

def connect_to_db():
    
        try:
            # create_connection(sqlite3_db_file)
            sqlite3_db_file="mySQLite3.db"
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
    now = datetime.now()
    event_date = now.strftime("%d/%m/%Y %H:%M:%S")
    events = []
    """ check if output dir exists if not create directory"""
    dir_isExist = os.path.exists(output_files_directory)
    if dir_isExist != True:
        logger.info(f"Directory exists: {dir_isExist}")
        os.mkdir(output_files_directory)
    else:
        logger.info(f"Directory {output_files_directory} exists: {dir_isExist}")
        

    conn = create_connection(sqlite3_db_file)
    
    cursor = conn.cursor()
    logger.info(f"Connection status: {conn}")
    insert_statement = "insert into events (event_date, level, file_name, event_message) values (:event_date, :level, :file_name, :event_message);"

    with open(read_file, mode='r') as input_file:
        for line in input_file:
            event_list = line.strip().split(" || ")
            
            if len(event_list) == 4:
                level, file_name, _, event_message = event_list            
                cursor.execute(insert_statement, {"event_date":event_date, 
                                                   "level": level.replace(':', ''), 
                                                   "file_name": file_name, 
                                                   "event_message":event_message})
    conn.commit()
    cursor.close()
    conn.close()
    logger.info(f"exiting {insert_logs.__name__}")




if __name__ == '__main__':

    #windows
    read_file = (r"logs\sqllite-python.log")
    output_files_directory = os.getcwd()
    split_out = (r"output\split_out.txt")


    #linux
    # read_file = "/mnt/c/Users/eliasm1/Documents/learn/python/log-parser/logs/sqllite-python.log"
    # output_files_directory = "/mnt/c/Users/eliasm1/Documents/learn/python/log-parser/output"
    # split_out = "/mnt/c/Users/eliasm1/Documents/learn/python/log-parser/output/split_out.txt"

    print(f"checking variables:")
    print(f"""
                    read file: {read_file}
                    output directory: {output_files_directory}
                    split file: {split_out}"

    """

    )

    connect_to_db()
    insert_logs()