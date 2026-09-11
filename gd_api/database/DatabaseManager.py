import sqlite3
from abc import ABC, abstractmethod

class DatabaseManager(ABC):
    def __init__(self, db_name: str = "gd_api_database.db"):
        self.db_name = db_name
        self.init_database()

    def get_connection(self):
        return sqlite3.connect(self.db_name, check_same_thread=False, timeout=30)

    #Only 1 time
    def init_database(self):
        with self.get_connection() as conn:
           conn.execute("PRAGMA journal_mode=WAL;")
           conn.commit()


    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def search(self):
        pass

    def commit(self):
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            self.connection.rollback()
            print(f"There was an error: {e}")

     




