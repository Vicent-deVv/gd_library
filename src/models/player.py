class Player:
    def __init__(
        self,
        account_id,
        player_id,
        username,
        stars=None,
        demons=None,
        creator_points=None,
        rank=None,
    ):
        self.account_id = account_id
        self.player_id = player_id
        self.username = username

        self.stars = stars
        self.demons = demons
        self.creator_points = creator_points
        self.rank = rank

            
    #this will return all the data already parsed
    def raw_data(self):
        pass

    #if you want to add o remove data, you can change this part
    def relevant_data(self):
        pass

