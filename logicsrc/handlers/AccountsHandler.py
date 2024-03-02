import sqlite3
from datetime import datetime
import os

class UserAccountHandler:
    def __init__(self):
        self.db_name = f"{os.getcwd()}\\.secret\\userdb.db"
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS user_accounts (
                unqid INTEGER PRIMARY KEY,
                username TEXT,
                firstname TEXT,
                lastname TEXT,
                foldername TEXT,
                password TEXT,
                role TEXT,
                date_of_creation TEXT
            )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def create_account(self, username, firstname, lastname, foldername, password, role):
        date_of_creation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = '''
            INSERT INTO user_accounts (username, firstname, lastname, foldername, password, role, date_of_creation)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, (username, firstname, lastname, foldername, password, role, date_of_creation))
        self.conn.commit()

    def update_account(self, unqid, username=None, firstname=None, lastname=None, foldername=None, password=None, role=None):
        updates = []
        if username:
            updates.append(('username', username))
        if firstname:
            updates.append(('firstname', firstname))
        if lastname:
            updates.append(('lastname', lastname))
        if foldername:
            updates.append(('foldername', foldername))
        if password:
            updates.append(('password', password))
        if role:
            updates.append(('role', role))
        updates.append(('date_of_creation', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        update_query = ', '.join([f'{field}=?' for field, _ in updates])
        query = f'''
            UPDATE user_accounts
            SET {update_query}
            WHERE unqid=?
        '''
        values = [value for _, value in updates]
        values.append(unqid)

        self.conn.execute(query, values)
        self.conn.commit()

    def get_account(self, unqid):
        query = '''
            SELECT * FROM user_accounts WHERE unqid=?
        '''
        cursor = self.conn.execute(query, (unqid,))
        return cursor.fetchone()

    def delete_account(self, unqid):
        query = '''
            DELETE FROM user_accounts WHERE unqid=?
        '''
        self.conn.execute(query, (unqid,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()