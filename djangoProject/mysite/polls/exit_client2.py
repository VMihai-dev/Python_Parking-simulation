import socket
from . import variables as myvars


def run_on_click2():
    myvars.flag4 = 1


def run_on_click():
    ClientMultiSocket = socket.socket()
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((myvars.host, myvars.port))
    except socket.error as e:
        print(str(e))
    while True:
        if myvars.flag4 == 1:
            message = "Exit"
            ClientMultiSocket.send(str.encode(message))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
            myvars.flag4 = 0
