import socket
from .variables import *

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 7011
def run_on_click2():
    global flag
    #res = ClientMultiSocket.recv(1024)
    #if res.decode('utf-8').strip() == "You can come in":
    #    ClientMultiSocket.send(str.encode("Coming in"))
    #    res = ClientMultiSocket.recv(1024)
    #    print(res.decode('utf-8'))
    #    return
    #ClientMultiSocket = socket.socket()
    #host = '127.0.0.1'
    #port = 7010
    #print('Waiting for connection response')
    #try:
    #    ClientMultiSocket.connect((host, port))
    #except socket.error as e:
    #    print(str(e))
    flag = 1


def run_on_click():
    global flag
    ClientMultiSocket = socket.socket()
    host = '127.0.0.1'
    port = 7011
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    res = ClientMultiSocket.recv(1024)
    while True:
        if res.decode('utf-8').strip() == "You can come in":
            Input = "Coming in"
            ClientMultiSocket.send(str.encode(Input))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
        if flag == 1:
            Input = "Enter"
            ClientMultiSocket.send(str.encode(Input))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
            flag = 0