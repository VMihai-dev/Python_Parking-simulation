import socket
from . import variables as myvars


def run_from_park():
    myvars.flagExit2 = 1


def run_from_home():
    ClientMultiSocket = socket.socket()
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((myvars.host, myvars.port))
    except socket.error as e:
        print(str(e))
    while True:
        if myvars.flagExit2 == 1:
            message = "Exit"
            ClientMultiSocket.send(str.encode(message))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
            myvars.flagExit2 = 0
