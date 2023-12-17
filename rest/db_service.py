import re
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

    def close(self):
        self.conn.close()

    def create(self, name, email):
        if not self.is_valid_email(email):
            raise Exception("Invalid email: " + email)
        try:
            self.cursor.execute('''
                INSERT INTO users (name, email)
                VALUES (?, ?)
            ''', (name, email))
            self.conn.commit()
        except Exception as e:
            raise Exception("Error creating user: " + str(e))

    def get_all_users(self):
        try:
            self.cursor.execute('''
                SELECT name, email
                FROM users
            ''')
            return self.cursor.fetchall()
        except Exception as e:
            raise Exception("Error getting all users: " + str(e))

    def get_user_by_name(self, name):
        try:
            self.cursor.execute('''
                SELECT email
                FROM users
                WHERE name = ?
            ''', (name,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            return None
        except Exception as e:
            raise Exception("Error getting user by name: " + str(e))

    def update_email(self, name, new_email):
        if not self.is_valid_email(new_email):
            raise Exception("Invalid email: " + new_email)
        try:
            self.cursor.execute('''
                SELECT name
                FROM users
                WHERE name = ?
            ''', (name,))
            result = self.cursor.fetchone()
            if not result:
                raise Exception("User does not exist: " + name)
            self.cursor.execute('''
                UPDATE users
                SET email = ?
                WHERE name = ?
            ''', (new_email, name))
            self.conn.commit()
        except Exception as e:
            raise Exception("Error updating user email: " + str(e))

    def delete_user_by_name(self, name):
        try:
            self.cursor.execute('''
                DELETE FROM users
                WHERE name = ?
            ''', (name,))
            self.conn.commit()
        except Exception as e:
            raise Exception("Error deleting user by name: " + str(e))

    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None