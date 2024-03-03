import sqlite3

class AccountsHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS accounts (
                unqid INTEGER PRIMARY KEY,
                role TEXT,
                username TEXT,
                password TEXT,
                foldername TEXT,
                seccode TEXT
            )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def get_account(self, unqid):
        query = '''
            SELECT * FROM accounts WHERE unqid=?
        '''
        cursor = self.conn.execute(query, (unqid,))
        return cursor.fetchone()

    def write_account(self, role, username, password, foldername, seccode):
        query = '''
            INSERT INTO accounts (role, username, password, foldername, seccode)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, (role, username, password, foldername, seccode))
        self.conn.commit()

    def update_account(self, unqid, role=None, username=None, password=None, foldername=None, seccode=None):
        updates = []
        if role:
            updates.append(('role', role))
        if username:
            updates.append(('username', username))
        if password:
            updates.append(('password', password))
        if foldername:
            updates.append(('foldername', foldername))
        if seccode:
            updates.append(('seccode', seccode))

        update_query = ', '.join([f'{field}=?' for field, _ in updates])
        query = f'''
            UPDATE accounts
            SET {update_query}
            WHERE unqid=?
        '''
        values = [value for _, value in updates]
        values.append(unqid)

        self.conn.execute(query, values)
        self.conn.commit()

    def delete_account(self, unqid):
        query = '''
            DELETE FROM accounts WHERE unqid=?
        '''
        self.conn.execute(query, (unqid,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()