class Song:
    def __init__(
        self,
        song_id,
        name,
        artist,
        custom=True,
    ):
        self.song_id = song_id
        self.name = name
        self.artist = artist
        self.custom = custom

    #this will return all the data already parsed
    def raw_data(self):
        pass

    #if you want to add o remove data, you can change this part
    def relevant_data(self):
        pass
