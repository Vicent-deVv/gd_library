import json
import sqlite3

from .DatabaseManager import DatabaseManager

class LevelDatabase(DatabaseManager):
    def create(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE "level" (
                    "id"            INTEGER PRIMARY KEY AUTOINCREMENT,
                    "raw_data"      TEXT NOT NULL,
                    "level_id"      INTEGER NOT NULL UNIQUE,
                    "name"          TEXT NOT NULL,
                    "creator"       TEXT NOT NULL,
                    "description"   TEXT NOT NULL,
                    "difficulty"    TEXT NOT NULL,
                    "stars"         INTEGER NOT NULL,
                    "level_length"  TEXT NOT NULL,
                    "song"          TEXT,
	                "downloads"		INTEGER NOT NULL,
	                "likes"			INTEGER NOT NULL
                );
            ''')




        self.commit()

    def insert(self, data: object):

        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                #The parameters are in an incorrect order so i have to change it before trying other methods
                cursor.execute('''
                    INSERT INTO level (
                        raw_data, 
                        level_id, 
                        name, 
                        creator, 
                        description, 
                        difficulty, 
                        stars, 
                        level_length, 
                        song,
                        downloads,
                        likes
                    )
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                ''',(json.dumps(data.raw_data), 
                     data.level_id, 
                     data.name, 
                     data.creator.username,
                     data.description, 
                     data.difficulty.value, 
                     data.stars,
                     data.length,
                     data.song,
                     data.downloads,
                     data.likes
                     ))
                conn.commit()
            except sqlite3.IntegrityError as e:
                print(f"Constraint error: {e}")

        

    def update(self):
        pass

    def search(self, level_id):
        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM level WHERE level_id = ?", [level_id])

                level = cursor.fetchone()

                if level is not None:
                    print("The level is already on the database")
                
                return level
            except:
                print("An error has ocurred")
                return None

    def delete(self):
        pass