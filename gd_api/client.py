import requests
import json

from .parser import Parser

from .utils import difficulties

from .models.player import Player
from .models.level import Level
from .models.song import Song

class Client:

    def __init__(self):
        self.base_url = "https://www.boomlings.com/"
        self.secret = "Wmfd2893gb7"
        self.game_version = "22"
        self.binary_version = "47"
        self.parser = Parser()

    def search_level(self, level_id: int):
        headers = {
            "User-Agent" : ""
        }

        data = {
            "levelID" : level_id,
            "secret" : self.secret,
            "gameVersion" : self.game_version,
            "binaryVersion" : self.binary_version,
            "type" : 0,
            "str" : str(level_id),
            "page" : 0
        }

        url = self.base_url + "database/getGJLevels21.php"

        req = requests.post(url=url,data=data,headers=headers)

        raw_dict = self.parser.data_parser(req.text)

        return Level(
        raw_data=raw_dict,
        level_id=int(raw_dict.get("1", 0)),
        name=raw_dict.get("2", "Unkown"),
        description=self.parser.de_encoder64(raw_dict.get("3", "")),
        creator=self.search_player(raw_dict.get("6", "")),
        difficulty=difficulties.get_level_difficulty(
            dif_denominator=int(raw_dict.get("8", 0)),
            dif_numerator=int(raw_dict.get("9", 0)),
            is_demon=raw_dict.get("17") == "1", 
            is_auto=raw_dict.get("25") == "1",
            demon_diff=int(raw_dict.get("43", 0)),
        ),
        stars=int(raw_dict.get("18", 0)),
        downloads=int(raw_dict.get("10", 0)),
        likes=int(raw_dict.get("14", 0)),
        length=raw_dict.get("15", "0"),
        song=raw_dict.get("35", "0"),
    )

        

    def search_player(self, player_name):
        headers = {
            "User-Agent" : ""
        }
        
        data = {
            "secret" : "Wmfd2893gb7",
            "str" : player_name
        }

        url = self.base_url + "database/getGJUsers20.php"

        req = requests.post(url=url, data=data,headers=headers)

        raw_dict = self.parser.data_parser(req.text)

        return Player(
            raw_data=raw_dict,
            player_id=raw_dict.get("2"),
            username=raw_dict.get("1"),
            stars=raw_dict.get("3", None),
            demons=raw_dict.get("4", None),
            creator_points=raw_dict.get("8", None),
            rank=raw_dict.get("6", None)

        )

    def search_song(self, song_id):
        headers = {
            "User-Agent" : ""
        }
                
        data = {
            "secret" : "Wmfd2893gb7",
            "songID" : song_id
        }

        url = self.base_url + "database/getGJSongInfo.php"

        req = requests.post(url=url,data=data,headers=headers)

        raw_dict = self.parser.song_parser(req.text)

        print(raw_dict)
        
        return Song(
            raw_data=raw_dict,
            song_id=raw_dict.get("1"),
            name=raw_dict.get("2"),
            artistID=raw_dict.get("3"),
            artistName=raw_dict.get("4"),
            link=raw_dict.get("10"),
            youtubeURL=raw_dict.get("7"),
            extraArtistNames=raw_dict.get("15")
        )