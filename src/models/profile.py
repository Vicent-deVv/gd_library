class Profile:
    def __init__(
        self,
        raw_data,
        player,
        bio=None,
        youtube=None,
        twitter=None,
        twitch=None,
    ):
        self.raw_data = raw_data

        self.player = player

        self.bio = bio

        self.youtube = youtube
        self.twitter = twitter
        self.twitch = twitch
        
