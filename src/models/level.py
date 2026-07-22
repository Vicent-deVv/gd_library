from src.parser import Parser
class Level:
    def __init__(
        self,
        raw_data,
        level_id,
        name,
        creator,
        description = None,
        difficulty=None,
        stars=None,
        downloads=None,
        likes=None,
        song=None,
    ):
        self.raw_data = raw_data

        self.level_id = level_id
        self.name = name
        self.creator = creator
        self.description = description

        self.difficulty = difficulty
        self.stars = stars
        self.downloads = downloads
        self.likes = likes

        self.song = song
    
