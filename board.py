import numpy as np
from numpy import half

# BOARD = np.zeros((4,8), int)
BOARD = np.array([ [ 0,  0,  0,  4,  4,  4,  4,  0],
                   [ 0,  0,  0,  4,  4,  4,  4,  0],
                   [ 4,  4,  4,  4,  4,  4,  4,  4],
                   [ 0,  0,  0,  0,  0,  0,  0,  0]])
MAX_INIT = 4
MAX_BEADS = 64
player_one = True
in_the_back = True
in_front = not in_the_back
# PLAYER_TWO = 2


def player( which) :
    if(which == 2 ):
        global player_one
        player_one = False
    elif(which == 1):
        # global player_one
        player_one = True

def hole_to_index(hole):#handling that the value does not exceed 16
    if (player_one):
        if (hole > 8):
            # global in_the_back
            # in_the_back = False
            # global in_front
            # in_front = not in_the_back
            return[2,16 - hole]

        elif (hole <= 8):
            # in_the_back = True
            # in_front = not in_the_back
            return [3, hole - 1]
    else:
        if (hole > 8):
            # in_the_back = False
            # in_front = not in_the_back
            return [1 ,hole - 9]
        elif (hole <= 8):
            # in_the_back = True
            # in_front = not in_the_back
            return [0, 8 - hole]

def hole_correspondance(hole):
    if(hole > 8):
        row2_p2_corsp = 25 - hole
        row1_p2_corsp  = 17 - row2_p2_corsp
        return [row1_p2_corsp, row2_p2_corsp]

def beads (hole):
    result = hole_to_index(hole)
    return BOARD[result[0]][result[1]]

def add_bead(hole):
    result = hole_to_index(hole)
    BOARD[result[0]][result[1]] += 1

def take_beads(hole, how_many):
    result = hole_to_index(hole)
    BOARD[result[0]][result[1]] -= how_many

def play(hole):
    result = beads(hole)
    current_hole = hole
    tmp_beads = beads(current_hole)
    loop = 0
    if (tmp_beads == 1):
        take_beads(current_hole,1)
        current_hole += 1
        add_bead(current_hole)
        tmp_beads = beads(current_hole)
        print(BOARD)
        if(current_hole > 8):
            result3 = hole_correspondance(current_hole)
            row2_crsp = result3[1]
            row1_crsp = result3[0]

            if (player_one):
                player(2)
            else:
                player(1)

            empty_p2_holes = beads(row1_crsp) == 0 and beads(row2_crsp) == 0
            if (not empty_p2_holes):
                beads_row1 = beads(row1_crsp)
                beads_row2 = beads(row2_crsp)
                tmp_beads = beads_row1 + beads_row2
                take_beads(row1_crsp, beads_row1)
                take_beads(row2_crsp, beads_row2)
                current_hole -= 1
                if (not player_one):
                    player(1)
                else:
                    player(2)
            else:
                if (not player_one):
                    player(1)

    while(not beads(current_hole)== 1):
        loop += 1
        print (loop)
        print (BOARD)
        temp_hole = 0
        take_beads(current_hole, beads(current_hole))

        for a_hole in range (current_hole, current_hole+tmp_beads):
            add_bead((a_hole % 16) + 1)
            temp_hole = (a_hole % 16 )+ 1
        if(temp_hole>8):
            result2 = hole_correspondance(temp_hole)
            row2_crsp = result2[1]
            row1_crsp = result2[0]

            if(player_one) :player(2)
            else: player(1)

            empty_p2_holes = beads(row1_crsp) == 0 and beads(row2_crsp) == 0
            if(not empty_p2_holes):
                beads_row1 = beads(row1_crsp)
                beads_row2 = beads(row2_crsp)
                tmp_beads = beads_row1 + beads_row2
                take_beads(row1_crsp,beads_row1)
                take_beads(row2_crsp,beads_row2)
                if (not player_one):player(1)
                else:player(2)
            else:
                if (not player_one):
                    player(1)
                else:
                    player(2)
                current_hole = temp_hole
                tmp_beads = beads(current_hole)
        else:
            # if (not player_one):
            #     player(1)
            # else:
            #     player(2)
            current_hole = temp_hole
            tmp_beads = beads(current_hole)
        print(BOARD)

def game_over():
    gameover=True
    for hole in range (1, 16):
        gameover = gameover and beads(hole) == 0
    return gameover

def two_players():
    while (not game_over()):
        if(player_one):
            slot =int ( input("player one choose slot between 1 and 16 : "))
            result = beads(slot)
            while(result == 0):
                slot = int(input("player one choose another slot between 1 and 16 that one is empty : "))
                result = beads(slot)
            play(slot)
            player(2)
        else:
            slot = int(input("player two choose slot between 1 and 16 : "))
            result = beads(slot)
            while (result == 0):
                slot = int(input("player twoo choose another slot between 1 and 16 that one is empty : "))
                result = beads(slot)
            play(slot)
            player(1)

    if player_one:
        print("player two wins")
    else:
        print("player one wins")



def main():

    player(1)
    two_players()
    # play(1)
    # play(6)
    print(BOARD)
if __name__ == '__main__':
    main()