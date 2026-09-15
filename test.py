import time
from gd_api.parser import Parser
from gd_api.models.player import Player
from gd_api.client import Client

from gd_api.database.LevelDatabase import LevelDatabase

# You can use this file to test the entire library, but it is not required for the library to work correctly.

def conection_test():
    #2 seconds of delay to prevent the rate limit
    time.sleep(2)

    #the init of the client object
    client = Client()


    id_list = [10565740, 4284013, 27690100, 26681070, 23262780]

    for i in id_list:
        time.sleep(5)
        data = client.search_level(i)
        print(data)

    #data = client.search_level(10565740)
    #print(data)

    #plyer = client.search_player("KyudenM")
    #print(plyer)

    #song = client.search_song(1569886)
    #print(song)

def database_test():
    level_db = LevelDatabase()

    print(level_db.delete(10565740))


def encoder_test():
    parser = Parser()
    text = "QUJD"
    print(parser.de_encoder64(text))

if __name__ == "__main__":
    database_test()