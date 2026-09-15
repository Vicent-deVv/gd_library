class leaderboard:
    def __init__(self, raw_data, top_10):
        self.raw_data = raw_data
        self.top_10 = top_10

        def __str__(self):
            return (
                f"Top 10: {self.top_10}"
            )
    

