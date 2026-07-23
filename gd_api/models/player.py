class Player:
    def __init__(
        self,
        raw_data,
        player_id,
        username,
        stars=None,
        demons=None,
        creator_points=None,
        rank=None,
    ):
        self.raw_data = raw_data

        self.player_id = player_id
        self.username = username

        self.stars = stars
        self.demons = demons
        self.creator_points = creator_points
        self.rank = rank


    
    def __str__(self):
        return f"Player(name={self.username}, id={self.player_id}, stars={self.stars}, demons={self.demons},creator_points={self.creator_points},rank={self.rank})"
