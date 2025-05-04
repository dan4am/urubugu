import httpx


def get_other_player_move(network, user_id: int):
    """
    Fetches the latest move from the other player in the match.
    """
    response = network.send("/game/get_move", {"user_id": user_id})
    return response


def send_my_move(network, match_id: int, player_id: int, my_move: int):
    """
    Sends the player's move to the server.
    """
    data = {"match_id": match_id, "player_id": player_id, "move": f"B{my_move}"}
    response = network.send("/game/move", data)
    return response


def get_starting_setting(network, user_id: int):
    """
    Fetches the starting board configuration for the match.
    """
    response = network.send(f"/game/get_starting_setting?player_id={user_id}")
    return response


def send_starting_setting(network, user_id: int, start_sett: str):
    """
    Sends the starting board configuration to the server.
    """
    data = {"user_id": user_id, "starting_setting": f"D{start_sett}"}
    response = network.send("/game/set_starting_setting", data)
    return response


def string_to_list(beads: str):
    """
    Converts a comma-separated string of beads into a list of integers.
    """
    return [int(b) for b in beads.split(",") if b.isdigit()]


def decode_reply(reply: str):
    """
    Decodes server responses.
    """
    print(reply)
    if reply.startswith("E0") or reply.startswith("F0") or reply.startswith("G0") or reply.startswith("H0"):
        return "waiting"
    elif reply.startswith(("E1", "F1", "G1", "H1")):
        return reply[2:]
    else:
        return "error"


def main():
    """
    Testing functions.
    """
    test_str = "ndagenda kunya unomusi"
    print(test_str[0:2])  # Output: nd
    print((2 % 2) + 1)  # Output: 1
    print((1 % 2) + 1)  # Output: 2


if __name__ == "__main__":
    main()
