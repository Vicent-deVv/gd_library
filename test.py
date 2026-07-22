import time
from src.gd_api.client import Client
from src.gd_api.parser import Parser
from src.gd_api.models.player import Player

# You can use this file to test the entire library, but it is not required for the library to work correctly.

def conection_test():
    #2 seconds of delay to prevent the "a lot of request ban"
    time.sleep(2)

    #the init of the client object
    client = Client()

    #data = client.search_level(127323087)
    #print(data)

    #plyer = client.search_player("ForkyVerstappen")
    #print(plyer)

    song = client.search_song(1569886)

    print(song)



def encoder_test():
    parser = Parser()
    text = "QUJD"
    print(parser.de_encoder64(text))

if __name__ == "__main__":
    conection_test()