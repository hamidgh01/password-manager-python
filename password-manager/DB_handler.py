"""
database handler, has been specially designed and is specially utilized
for this project (password generator and manager using python)
"""

import sqlite3


class DBHandler:
    """database handler for the app"""
    
    # superuser (admin)
    # current_user (logged-in user)
    
    def __init__(self, database: str = "database"):
        if database == ":memory:":
            pass
        elif not database.endswith(".db"):
            database += ".db"
        
        self.database = database
    
    def __enter__(self):
        self.connector = sqlite3.connect(database=self.database)
        self.db_cursor = self.connector.cursor()
        
        create_table_users = """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT(32) NOT NULL UNIQUE,
                password TEXT(32) NOT NULL
            );
        """
        create_table_passwords = """
            CREATE TABLE IF NOT EXISTS passwords(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service_name TEXT(64) DEFAULT "NOT PROVIDED",
                username TEXT(64) DEFAULT "NOT PROVIDED",
                password TEXT(32) NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
            """
        
        self.db_cursor.execute(create_table_users)
        self.db_cursor.execute(create_table_passwords)
        self.connector.commit()
        
        # note:
        # with ... as variable:
        #     ...
        # point: variable = what will be returned from __enter__
        # so:
        return self
    
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
    
    def register_user(self, username: str, password: str) -> bool:
        """register new user"""
        try:
            sql = "INSERT INTO users (username, password) VALUES (?, ?)"
            self.db_cursor.execute(sql, (username, password))
            self.connector.commit()
            return True
        except sqlite3.IntegrityError:
            self.connector.rollback()
            print(f"the username {username!r} is already taken! "
                  f"please enter a different username.\n")
            return False
        except sqlite3.Error:
            self.connector.rollback()
            return False
    
    def change_user_password(self):
        """change user password"""
        pass
    

def test():
    """complete here later"""
    
    with DBHandler("my_database"):
        pass


if __name__ == '__main__':
    test()
