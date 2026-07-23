from parser import Parser
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
        length=None
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

        self.length = length

        self.song = song

    def __str__(self):
        diff = getattr(self.difficulty, "value", self.difficulty)
        return (
            f"Level '{self.name}' ({self.level_id}) | "
            f"Creator: {self.creator} | "
            f"Diff: {diff} ({self.stars}★) | "
            f"Downloads: {self.downloads} | Likes: {self.likes}"
        )
    
