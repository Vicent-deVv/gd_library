import json
import sqlite3

from .DatabaseManager import DatabaseManager


class LevelDatabase(DatabaseManager):
    def create(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS "level" (
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
                    "downloads"     INTEGER NOT NULL,
                    "likes"         INTEGER NOT NULL
                );
            """
            cursor.execute(query)

            conn.commit()


    def insert(self, data: object):
        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()
                query = """
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
                    VALUES (
                        :raw_data, 
                        :level_id, 
                        :name, 
                        :creator, 
                        :description, 
                        :difficulty, 
                        :stars, 
                        :level_length, 
                        :song,
                        :downloads,
                        :likes
                    );
                """

                valores = {
                    "raw_data": json.dumps(data.raw_data),
                    "level_id": data.level_id,
                    "name": data.name,
                    "creator": data.creator["username"],
                    "description": data.description,
                    "difficulty": data.difficulty.value,
                    "stars": data.stars,
                    "level_length": data.length,
                    "song": data.song,
                    "downloads": data.downloads,
                    "likes": data.likes,
                }

                cursor.execute(query, valores)
                conn.commit()

            except Exception as e:
                conn.rollback()
                print(f"An error occurred while inserting the level: {e}")

    def update(self, data: object):
        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    UPDATE level
                    SET raw_data     = :raw_data,
                        name         = :name,
                        creator      = :creator,
                        description  = :description,
                        difficulty   = :difficulty,
                        stars        = :stars,
                        level_length = :level_length,
                        song         = :song,
                        downloads    = :downloads,
                        likes        = :likes
                    WHERE level_id   = :level_id;
                """

                valores = {
                    "raw_data": json.dumps(data.raw_data),
                    "level_id": data.level_id,
                    "name": data.name,
                    "creator": data.creator["username"],
                    "description": data.description,
                    "difficulty": data.difficulty.value,
                    "stars": data.stars,
                    "level_length": data.length,
                    "song": data.song,
                    "downloads": data.downloads,
                    "likes": data.likes,
                }

                cursor.execute(query, valores)
                conn.commit()

            except Exception as e:
                conn.rollback()
                print(f"An error occurred while updating the level: {e}")

    def search(self, level_id: int):
        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    SELECT * 
                    FROM level 
                    WHERE level_id = :level_id;
                """
                values = {"level_id": level_id}

                cursor.execute(query, values)
                level = cursor.fetchone()

                if level is not None:
                    print("The level is already on the database")

                return level

            except Exception as e:
                print(f"An error has occurred: {e}")
                return None
    
    
    def delete(self, level_id: int):
        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    DELETE FROM level 
                    WHERE level_id = :level_id;
                """
                values = {"level_id": level_id}

                cursor.execute(query, values)
                conn.commit()

            except Exception as e:
                conn.rollback()
                print(f"An error occurred while deleting the level: {e}")