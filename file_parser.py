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
    events = []
    logger.info(f"entering {insert_logs.__name__}")
    """ check if output dir exists if not create directory"""
    dir_isExist = os.path.exists(output_files_directory)
    if dir_isExist != True:
        logger.info(f"Directory: {output_files_directory} does not exist, will be created")
        os.mkdir(output_files_directory)
    else: 
        logger.info(f"Directory {output_files_directory} exists")

    with open(read_file, mode='r') as input_file:
        logger.info(f"Reading file {read_file}")
        for line in input_file:
                # logger.info(line.strip().split(" || "))
                with open(split_out, mode='a') as output_file:
                    # event_list = line.split(": ||")
                    event_list = line.split(": || ", 4 )
                    events = (f"{event_list}\n")
                    output_file.write(f"{events}")
                    rec = events.split(', ')
                    print(rec)
                    """ inserting records into DB """
                    conn = create_connection(sqlite3_db_file)
                    insert_statement = " insert into events ( level, file_name, event_message ) values ('$s', '$s', '$s') "
                    vals = rec
                    conn.execute(insert_statement, vals[0], vals[1], vals[3])
                    #conn = cursor.execute("select * from events")
                    conn.commit()
                    conn.close()

                    # input_file.close()
                    return events
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

    dada = insert_logs()
    # print(f"lala {dada[]}")