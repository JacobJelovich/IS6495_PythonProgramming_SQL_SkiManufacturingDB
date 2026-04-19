#Base database file that contains a DBbase class that serves as a baseline for creating the
#necessary database for the ski manufacturing. It contains a constructor that sets up the connection and
#cursor as well as methods for connecting, executing scripts, resetting the database, closing
#the database, as well as properties to get the connection and cursor.

import sqlite3

class DBbase:

    _conn = None
    _cursor = None

    def __init__(self, db_name):
        self._db_name = db_name
        self.connect()

    def connect(self):
        self._conn = sqlite3.connect(self._db_name)
        self._cursor = self._conn.cursor()

    def execute_script(self, sql_string):
        self._cursor.executescript(sql_string)

    def reset_database(self):
        raise NotImplementedError("Must implement from the derived class")

    def close_db(self):
        self._conn.close()

    @property
    def get_cursor(self):
        return self._cursor

    @property
    def get_connection(self):
        return self._conn