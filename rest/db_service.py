import sqlite3


class DbService:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                name TEXT PRIMARY KEY,
                email TEXT
            )
        ''')
        self.conn.commit()

    def clear_table(self):
        self.cursor.execute('''
            DELETE FROM users
        ''')
        self.conn.commit()
