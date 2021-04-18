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


def main():
    s = "ndagenda kunya unomusi"
    print( s[:])


if __name__ == "__main__":
    main()