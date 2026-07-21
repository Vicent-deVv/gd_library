from src.parser import Parser
class Level:
    def __init__(
        self,
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
        self.level_id = level_id
        self.name = name
        self.creator = creator
        self.description = description

        self.difficulty = difficulty
        self.stars = stars
        self.downloads = downloads
        self.likes = likes

        self.song = song
    
    #this will return all the data already parsed
    def raw_data(self):
        pass

    #if you want to add o remove data, you can change this part
    def relevant_data(self):
        pass

