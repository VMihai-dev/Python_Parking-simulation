import socket
import os
from _thread import *
from .variables import *

#from threading import Thread
def handle_input(input):
    global parkingSpaces
    global queue
    with a_lock:
        print("I am thread id: ", str(get_ident()))
        if get_ident() == threads[0] or get_ident() == threads[1]:
            if input.strip() == "Enter":
                if parkingSpaces > 0:
                    return "You can come in"
                else:
                    queue+=1
                    return "Not enough spaces, you have to wait... queue size: ".__add__(str(queue))
            elif input.strip() == "Coming in":
                parkingSpaces-=1
                return "Car has parked, spaces available: ".__add__(str(parkingSpaces))
            else:
                return "I don't understand, try to \"Enter\""
        elif get_ident() == threads[2] or get_ident() == threads[3]:
            if input.strip() == "Exit":
                if parkingSpaces > 4:
                    return "There are no cars in the parking lot.."
                elif queue > 0:
                    queue-=1
                    return "Car has left, there is a queue.. letting a car from the queue to come in".__add__(str(queue))
                else:
                    parkingSpaces += 1
                    return "Car has left, spaces available: ".__add__(str(parkingSpaces))
            else:
                return "I don't understand, try to \"Exit\""

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(1024).decode()
        print("This is the data we receive", data)
        if data == "Enter" or data == "Exit" or data == "Coming in":
            response = handle_input(data).encode()
            connection.sendall(response)
        if not data:
            print("I am breaking?")
            break
    connection.close()

def run_on_click():
    global ThreadCount
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Socket is listening..')
    ServerSideSocket.listen(5)

    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        identifier = start_new_thread(multi_threaded_client, (Client, ))
        threads.append(identifier)
        ThreadCount+=1
        print("This is the list of identidifers: ", threads)
        print("This is native id: ", str(get_ident()))
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()

"""
# server.py
import socket
import time
import signal
import sys
# import thread module
from _thread import *
import threading
from threading import Thread
#from SocketServer import ThreadingMixIn
print_lock = threading.Lock()

# thread function
# Multithreaded Python server : TCP Server Socket Thread Pool


def start_server():
   host = "127.0.0.1"
   port = 6570 # arbitrary non-privileged port
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   print("Socket created")
   try:
      soc.bind((host, port))
   except:
      print("Bind failed. Error : " + str(sys.exc_info()))
      sys.exit()
   soc.listen(6) # queue up to 6 requests
   print("Socket now listening")
   # infinite loop- do not reset for every requests
   while True:
      connection, address = soc.accept()
      ip, port = str(address[0]), str(address[1])
      print("Connected with " + ip + ":" + port)
   try:
      Thread(target=client_thread, args=(connection, ip, port)).start()
   except:
      print("Thread did not start.")
      traceback.print_exc()
   soc.close()


def clientThread(connection, ip, port, max_buffer_size = 5120):
   is_active = True
   while is_active:
      client_input = receive_input(connection, max_buffer_size)
      if "--QUIT--" in client_input:
         print("Client is requesting to quit")
         connection.close()
         print("Connection " + ip + ":" + port + " closed")
         is_active = False
      else:
         print("Processed result: {}".format(client_input))
         connection.sendall("-".encode("utf8"))


def receive_input(connection, max_buffer_size):
   client_input = connection.recv(max_buffer_size)
   client_input_size = sys.getsizeof(client_input)
   if client_input_size > max_buffer_size:
      print("The input size is greater than expected {}".format(client_input_size))
   decoded_input = client_input.decode("utf8").rstrip()
   result = process_input(decoded_input)
   return result


def process_input(input_str):
   print("Processing the input received from client")
   return "Hello " + str(input_str).upper()

if __name__ == "__main__":
   start_server()


"""
"""
class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New server socket thread started for ", ip, ":", str(port))

    def run(self):
        while True:
            print("Came in the run function: ", str(Thread.getName(self)))
            data = conn.recv(1024).decode()
            print("This is the data received for:",str(Thread.getName(self)), " ", data)
            if data.strip() == 'exit':
                break
            conn.send(handle_input(data).encode())  # echo


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
port = 6570     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
threads = []

while True:
    s.listen(4)
    print("Multithreaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip,port2)) = s.accept()
    newthread = ClientThread(ip, port2)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
"""
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