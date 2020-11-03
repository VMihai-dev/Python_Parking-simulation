import socket
from _thread import *
from . import variables as myvars


def handle_input(message):
    a_lock = allocate_lock()
    with a_lock:
        print("I am thread id: ", str(get_ident()))
        if get_ident() == myvars.threads[0] or get_ident() == myvars.threads[1]:
            if message.strip() == "Enter":
                if myvars.parkingSpaces > 0:
                    return "You can come in"
                else:
                    myvars.queue += 1
                    return "Not enough spaces, you have to wait... queue size: ".__add__(str(myvars.queue))
            elif message.strip() == "Coming in":
                myvars.parkingSpaces -= 1
                return "Car has parked, spaces available: ".__add__(str(myvars.parkingSpaces))
            else:
                return "I don't understand, try to \"Enter\""
        elif get_ident() == myvars.threads[2] or get_ident() == myvars.threads[3]:
            if message.strip() == "Exit":
                if myvars.parkingSpaces > 4:
                    return "There are no cars in the parking lot.."
                elif myvars.queue > 0:
                    myvars.queue -= 1
                    return "Car has left, there is a queue.. letting a car from the queue to come in" \
                        .__add__(str(myvars.queue))
                else:
                    myvars.parkingSpaces += 1
                    return "Car has left, spaces available: ".__add__(str(myvars.parkingSpaces))
            else:
                return "I don't understand, try to \"Exit\""


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(1024).decode()
        print("This is the data we receive", data)
        if "Enter" in data or "Exit" in data or "Coming in" in data:
            response = handle_input(data).encode()
            connection.sendall(response)
        if not data:
            print("I am breaking?")
            break
    connection.close()


def run_on_click():
    ServerSideSocket = socket.socket()
    try:
        ServerSideSocket.bind((myvars.host, myvars.port))
    except socket.error as e:
        print(str(e))

    print('Socket is listening..')
    ServerSideSocket.listen(5)

    while True:
        client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        identifier = start_new_thread(multi_threaded_client, (client,))
        myvars.threads.append(identifier)
        myvars.threadCount += 1
        print("This is the list of identifiers: ", myvars.threads)
        print("This is native id: ", str(get_ident()))
        print('Thread Number: ' + str(myvars.threadCount))
# ServerSideSocket.close()
