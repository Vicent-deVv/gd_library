import requests
import json
from .parser import Parser
from .models.player import Player
from .models.level import Level

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

        data = self.parser.data_parser(req.text)

        #You can uncomment this, this only is for testing purposes
        #relevant_data = {
        #    'levelID' : data['1'],
        #    'levelName' : data['2'],
        #    'description' : self.parser.de_encoder64(data['3']),
        #    'playerID' : data['6'],
        #    'officialSong' : data['12'],
        #    'length' : data['15'],
        #    'CustomSongID' : data['35']
        #}
#
        #with open('data.json','w',encoding='utf-8') as file:
        #    json.dump(relevant_data,file,indent=4,ensure_ascii=False)

        return Level(
            raw_data=data,
            level_id=data['1'],
            name=data['2'],
            description=self.parser.de_encoder64(data['3']),
            
            )

        

    def search_player(self, player_name: str):

        headers = {
            "User-Agent" : ""
        }
        

        data = {
            "secret" : "Wmfd2893gb7",
            "str" : player_name
        }

        url = self.base_url + "database/getGJUsers20.php"

        req = requests.post(url=url, data=data,headers=headers)

        data = self.parser.data_parser(req.text)

        #I have to fix this because i modified the model
        return Player(
            data['2'],
            data['1'],
            data['3'],
            data['4'],
            data['8'],
            data['6']
        )

