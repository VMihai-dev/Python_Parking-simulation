import socket
from . import variables as myvars


def run_from_park():
    myvars.flagEntrance2 = 1


# We send an Enter message, if "You can come in" then we occupy a space otherwise we wait in the queue
def run_from_home():
    ClientMultiSocket = socket.socket()
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((myvars.host, myvars.port))
    except socket.error as e:
        print(str(e))
    res = ClientMultiSocket.recv(1024)
    while True:
        if res.decode('utf-8').strip() == "You can come in":
            message = "Coming in"
            ClientMultiSocket.send(str.encode(message))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
        if myvars.flagEntrance2 == 1:
            message = "Enter"
            ClientMultiSocket.send(str.encode(message))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
            myvars.flagEntrance2 = 0
