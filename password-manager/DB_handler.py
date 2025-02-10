"""
a simple ORM, specially was designed & is utilized for
this project (password generator and manager)
"""

import sqlite3


class DB:
    """orm"""
    
    def __init__(self, database="database"):
        self.database = database
    
    def __enter__(self):
        self.connector = sqlite3.connect(database=self.database)
        self.db_cursor = self.connector.cursor()
        self._create_table()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connector.close()
    
    def insert(self):
        """insert"""
        pass
    
    def read(self):
        """read"""
        pass
    
    def update(self):
        """update"""
        pass

    def delete(self):
        """delete"""
        pass
    
    def create_table(self):
        """create_table"""
        pass
    
    def create_table(self):
        """create_table"""
        pass
    
    def create_table(self):
        """create_table"""
        pass
    
    def create_table(self):
        """create_table"""
        pass
    
    def create_table(self):
        """create_table"""
        pass
