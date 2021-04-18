import socket
from _thread import *
import sys

server = ""
port = 5555
current_player = 1
player_one_starting_settings = ""
player_one_moves = []

player_two_starting_settings = ""
player_two_moves = []



my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    my_socket.bind((server,port))
except socket.error as e:
    str(e)

my_socket.listen(2)
print("Server Started, Waiting for connection")

def decode_data(data_string, player):
    global player_two_starting_settings, player_one_starting_settings,player_two_moves,player_one_moves
    code = data_string[0]

    if code == "A":
        if player == 1:
            return player_one_moves.pop(0)
        else :
            return player_two_moves.pop(0)

    if code == "B":
        if player == 1:
            player_one_moves.append(data_string[1:])
            return (" your move have been successfully registered player 1")
        else :
            player_two_moves.append(data_string[1:])
            return (" your move have been successfully registered player 2")

    if code == "C":
        if player == 1:
            return player_two_starting_settings
        else :
            return player_one_starting_settings
    if code == "D":
        if player == 1:
            player_one_starting_settings = data_string[1:]
            return (" your starting settings have been successfully registered player 1")
        else :
            player_two_starting_settings = data_string[1:]
            return (" your starting settings have been successfully registered player 2")





def threaded_client(connection, player):
    global current_player
    if (current_player <= 3):
        connection.send(str.encode("you are player "+ str(player)))
        reply = ""
        while True:
            try:
                data = connection.recv(2048)
                data_string = data.decode("utf-8")
                reply = decode_data(data_string, player)

                if not data:
                    print("Disconnected")
                    break
                else:
                    print("Received: "+ data_string + " from player " + str(player))
                    print("Sending : "+ reply + " to player " + str(player))

                connection.sendall(str.encode(reply))
            except:
                break

        print("Lost connection")
        connection.close()

        current_player -= 1
    else:
        connection.send(str.encode("there cannot be more than 2 players"))
        connection.close()
        current_player -= 1


def main():
    global current_player
    current_player = 1
    while True:
        connection, addr = my_socket.accept()
        print("connected to: ", addr)
        start_new_thread(threaded_client, (connection, current_player))
        current_player += 1




if __name__ == "__main__":
    main()