import sqlite3
from sqlite3 import Error 


db_file = "/mnt/c/Users/kelly/OneDrive/Desktop/spittler/db/database.db"
def create_database(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()

create_database(db_file)
