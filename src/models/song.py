class Song:
    def __init__(
        self,
        raw_data,
        song_id,
        name,
        artist,
        custom=True,
    ):
        self.raw_data = raw_data

        self.song_id = song_id
        self.name = name
        self.artist = artist
        self.custom = custom
