import sqlite3
sqlite3_db_file = "mySQLite3.db"

def insertMultipleRecords(recordList):
    try:
        sqliteConnection = sqlite3.connect(sqlite3_db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO test_table
                            (id, name, email, joining_date, salary) 
                            VALUES (?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")



recordsToInsert = [(4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500),
                   (5, 'Chris', 'chris@gmail.com', '2019-05-15', 7600),
                   (6, 'Jonny', 'jonny@gmail.com', '2019-03-27', 8400)]


if __name__ == '__main__':
    insertMultipleRecords(recordsToInsert)
