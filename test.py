import time
from src.client import Client
from src.parser import Parser

def test_conexion():
    #2 seconds of delay to prevent the "a lot of request ban"
    time.sleep(2)

    #the init of the client object
    client = Client()

    #You can search any level, the only thing that you need is the ID of the level
    #this return a dictionary with the relevant data, you can also change this in client.py
    #finally a json file will create it in the root folder
    data = client.search_level(89886591)


    print(data)



def test_de_encoder():
    parser = Parser()
    text = "QUJD"
    print(parser.de_encoder64(text))

if __name__ == "__main__":
    test_conexion()