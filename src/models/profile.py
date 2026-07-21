class Profile:
    def __init__(
        self,
        player,
        bio=None,
        youtube=None,
        twitter=None,
        twitch=None,
    ):
        self.player = player

        self.bio = bio

        self.youtube = youtube
        self.twitter = twitter
        self.twitch = twitch

            
    #this will return all the data already parsed
    def raw_data(self):
        pass

    #if you want to add o remove data, you can change this part
    def relevant_data(self):
        pass

