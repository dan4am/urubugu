import socket
from _thread import *
import sys

server = ""
port = 5555


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    my_socket.bind((server,port))
except socket.error as e:
    str(e)

my_socket.listen(2)
print("Server Started, Waiting for connection")

def threaded_client(connection):
    connection.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            connection.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    connection.close()


def main():
    while True:
        connection, addr = my_socket.accept()
        print("connected to: ", addr)


        start_new_thread(threaded_client, (connection,))


if __name__ == "__main__":
    main()