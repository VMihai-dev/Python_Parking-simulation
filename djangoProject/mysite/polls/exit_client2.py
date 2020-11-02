import socket
from .variables import *
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 7011

def run_on_click2():
    global flag4
    flag4 = 1

def run_on_click():
    global flag4
    ClientMultiSocket = socket.socket()
    host = '127.0.0.1'
    port = 7011
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    while True:
        if flag4 == 1:
            Input = "Exit"
            ClientMultiSocket.send(str.encode(Input))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
            flag4 = 0