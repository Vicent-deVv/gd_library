import time
from gd.client import Client
from gd.parser import Parser

def test_conexion():
    time.sleep(2)
    client = Client()
    data = client.search_level(54953085)

    print(data)



def test_de_encoder():
    parser = Parser()
    text = "QUJD"
    print(parser.de_encoder64(text))

if __name__ == "__main__":
    test_conexion()