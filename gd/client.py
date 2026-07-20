import requests
import json
from .parser import Parser

class Client:
    def __init__(self):
        self.base_url = "https://www.boomlings.com/database/"
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

        url = self.base_url + "getGJLevels21.php"

        req = requests.post(url=url,data=data,headers=headers)

        data = self.parser.data_parser(req.text)

        relevant_data = {
            'levelID' : data['1'],
            'levelName' : data['2'],
            'description' : self.parser.de_encoder64(data['3']),
            'playerID' : data['6'],
            'officialSong' : data['12'],
            'length' : data['15']
        }

        with open('data.json','w',encoding='utf-8') as file:
            json.dump(relevant_data,file,indent=4,ensure_ascii=False)



        return relevant_data

        

    def search_song(self):
        pass