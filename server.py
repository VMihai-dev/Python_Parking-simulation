# server.py
import socket
import time
import signal
import sys


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    conn.close()
    sys.exit(0)


def handle_input(input):
    if input.strip() == "This":
        return "I found a match"
    else:
        return input


signal.signal(signal.SIGINT, signal_handler)
host = '127.0.0.1'      # Symbolic name meaning all available interfaces
port = 6568     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024).decode()
    if not data: break
    conn.send(handle_input(data).encode())

"""
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
"""