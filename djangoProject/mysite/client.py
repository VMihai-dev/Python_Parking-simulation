# client.py
import socket

import socket
import sys
import signal


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    s.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
host = '127.0.0.1'
port = 6568                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    for line in sys.stdin:
        line = line.encode()
        s.send(line)
        data = s.recv(1024)
        print('Received', repr(data))
s.close()

"""
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
"""