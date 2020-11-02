import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 7007

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
while True:
        if res.decode('utf-8').strip() == "You can come in":
            ClientMultiSocket.send(str.encode("Coming in"))
            res = ClientMultiSocket.recv(1024)
            print(res.decode('utf-8'))
            continue
        Input = input()
        ClientMultiSocket.send(str.encode(Input))
        res = ClientMultiSocket.recv(1024)
        print(res.decode('utf-8'))

ClientMultiSocket.close()