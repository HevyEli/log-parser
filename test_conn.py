import sqlite3 
from db import *


def test_connection():
    try:
        create_connection(sqlite3_db_file)
        return True
    except Exception as e:
        logger.info(e)
        if create_connection() == False:
            logger.info(f"Not connected!")
        else:
            logger.info(f"Connected!")

    return False

# print (f"Connection test: {test_connection}")


def select_data():
    conn = None
    conn = create_connection(sqlite3_db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM EVENTs")
    rows = cur.fetchall()
    
    for index, row in enumerate(rows):
        print(f"rownum: {index}, {row}")
        logger.info(f"select output: {row}")

if __name__ == '__main__':
    test_connection()
    logger.info (f"Connection test: {test_connection}")
    #select_data()
