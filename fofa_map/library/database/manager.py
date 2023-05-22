import sqlite3

class DatabaseManager:
    connection = None
    cursor = None

    def __init__(self):
        self.connect()
    def connect(self):
        self.connection = sqlite3.connect('databse.db',check_same_thread=False)
        self.cursor = self.connection.cursor()
    def colse(self):
        self.connection.close()

    def execute(self,*args,**kwargs) -> sqlite3.Cursor:
        result = self.connection.execute(*args,**kwargs)
        self.connection.commit()
        return result
class Sqlite3Cache():
    def __init__(self):
        pass
