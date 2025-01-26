def get_other_player_move(network):
    return network.send("A")


def send_my_move(network, my_move):
    return network.send("B"+str(my_move))

def get_starting_setting(network):
    return network.send("C")


def send_starting_setting(network, start_sett):
    return network.send("D"+start_sett)

def string_to_list(beads):
    result  = []
    result = beads.split(",")
    for i in range(len (result)):
        result[i] = int(result[i])

    return result

def decode_reply(reply):
    if reply[0:2] == "E0":
        return "waiting"
    elif reply[0:2] == "E1":
        return reply [2:]
    elif reply[0:2] == "F0":
        return "waiting"
    elif reply[0:2] == "F1":
        return reply[2:]
    elif reply[0:2] == "G0":
        return "waiting"
    elif reply[0:2] == "G1":
        return reply[2:]
    elif reply[0:2] == "H0":
        return "waiting"
    elif reply[0:2] == "H1":
        return reply[2:]
    else:
        return "error"



def main():
    s = "ndagenda kunya unomusi"
    print( s[0:2])
    print( (2 % 2) + 1)
    print( (1% 2 ) + 1)


if __name__ == "__main__":
    main()