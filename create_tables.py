import sqlite3

def create_tables(database_path):
    # Connect to SQLite database (creates a new one if not exists)
    conn = sqlite3.connect(database_path)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create 'user' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')

    # Create 'task' table with a foreign key reference to 'user' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL,
            begin_date DATE NOT NULL,
            end_date DATE NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES user (id)
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Tables 'user' and 'task' created successfully.")




# Example usage:
database_path = '/mnt/c/Users/kelly/OneDrive/Desktop/spittler/db/database.db'
create_tables(database_path)
