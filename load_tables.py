import sqlite3
from datetime import datetime


def load_data(database_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Insert sample data into the 'user' table
    users_data = [
        ('Kelly', 'Khalil'),
        ('Hassan', 'Khalil'),
        ('Celine', 'Khalil'),
        # Add more user data as needed
    ]
    cursor.executemany('INSERT INTO user (first_name, last_name) VALUES (?, ?)', users_data)

    # Insert sample data into the 'task' table
    tasks_data = [
        ('Task 2', 1, datetime(2023, 11, 23), datetime(2023, 11, 30), 2),
        ('Task 3', 1, datetime(2023, 11, 23), datetime(2023, 11, 30), 3),
        ('Task 4', 1, datetime(2023, 11, 23), datetime(2023, 11, 30), 4),
        # Add more task data as needed
    ]
    cursor.executemany('INSERT INTO task (name, priority, begin_date, end_date, user_id) VALUES (?, ?, ?, ?, ?)', tasks_data)



    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Data loaded into 'user' and 'task' tables successfully.")

# Example usage:
database_path = '/mnt/c/Users/kelly/OneDrive/Desktop/spittler/db/database.db'


# Call load_data to insert sample information
load_data(database_path)
