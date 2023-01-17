import sqlite3 
from sqlite3 import Error
import logging

#import cust_log
#windows
logfile = (r"C:\Users\eliasm1\Documents\learn\python\log-parser\sqllite-python.log_new")

#linux

# logfile = "/mnt/c/Users/eliasm1/Documents/learn/python/log-parser/sqllite-python.log_new"

logger = logging.basicConfig(level=logging.DEBUG, 
                    format='%(levelname)s: || file name: %(filename)s.%(funcName)s - line: %(lineno)d || date: || %(asctime)s: || message: %(message)s',
                    handlers=[
                        logging.FileHandler(filename=logfile, mode="a"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(name='python')
sqlite3_db_file = "mySQLite3.db"

def create_connection(sqlite3_db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(sqlite3_db_file)
        logger.info(f"Database created, version: {sqlite3.version}")
        logger.info(f"DB file {sqlite3_db_file}")

    except Error as e:
        logger.debug(e)

    return conn

def create_table(conn, create_table_sql):
    """
    create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        logger.debug(f"error: {e}")


def main():
    database = sqlite3_db_file
    table_name = "events"

    sql_create_events_table = """ CREATE TABLE IF NOT EXISTS events (
                                    events_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    event_date timestamp not null,
                                    level text  NOT NULL,
                                    file_name text NOT NULL,
                                    event_message text NOT NULL
                                    );"""

    #create connection to the database
    conn = create_connection(sqlite3_db_file)
    logger.info(f"Testing connection: {conn}")

    if conn is not None:
        logger.info(f"{conn}")
        create_table(conn, sql_create_events_table)
        logger.info(f"Table {table_name} has been created")
        conn.commit()
    else: 
        logger.error(f"Failed to create table {table_name}")
    conn.close()

if __name__ == '__main__':
    create_connection(sqlite3_db_file)

    main()