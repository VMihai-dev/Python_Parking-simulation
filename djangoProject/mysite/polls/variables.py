import socket
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 7011
threadCount = 0
threads = []
a_lock = allocate_lock()
parkingSpaces = 5
queue = 0
flag = 0
flag2 = 0
flag3 = 0
flag4 = 0
