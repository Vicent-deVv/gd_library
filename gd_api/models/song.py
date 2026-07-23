class Song:
    def __init__(
        self,
        raw_data,
        song_id,
        name,
        artistID,
        artistName,
        link=None,
        youtubeURL=None,
        extraArtistNames=None,
        custom=True,
    ):
        self.raw_data = raw_data

        self.song_id = song_id
        self.name = name
        self.artistID = artistID
        self.artistName = artistName
        self.link = link
        self.youtubeURL = youtubeURL
        self.extraArtistNames = extraArtistNames
        self.custom = custom

    def __str__(self):
        return (
            f"Song(id={self.song_id}, name='{self.name}', artist='{self.artistName}', "
            f"artist_id={self.artistID}, extra_artists='{self.extraArtistNames}', "
            f"link='{self.link}', youtube='{self.youtubeURL}')"
        )
