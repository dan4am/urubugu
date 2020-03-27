import numpy as np
from numpy import half

# BOARD = np.zeros((4,8), int)
BOARD = np.array([ [ 0, 0, 0,  0,  0,  0,  0,  0],
                   [ 4,  4,  4,  4,  4,  4,  4,  4],
                   [ 0,  4,  4,  4,  4,  0,  0,  0],
                   [ 0,  4,  4,  4,  4,  0,  0,  0]])
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
            player(2)
            empty_p2_holes = beads(row1_crsp) == 0 and beads(row2_crsp) == 0
            if(not empty_p2_holes):
                beads_row1 = beads(row1_crsp)
                beads_row2 = beads(row2_crsp)
                tmp_beads = beads_row1 + beads_row2
                take_beads(row1_crsp,beads_row1)
                take_beads(row2_crsp,beads_row2)
                player(1)
            else:
                player(1)
                current_hole = temp_hole
                tmp_beads = beads(current_hole)
        else:
            player(1)
            current_hole = temp_hole
            tmp_beads = beads(current_hole)



def main():

    player(1)
    # BOARD[2][3] = 0
    # BOARD[3][3] = 9
    # # BOARD[3][7] = 1
    # BOARD[0][3] = 5
    # BOARD[0][2] = 17
    # BOARD[1][3] = 5
    print(BOARD)
    # print(beads(13))
    # print(beads(4))
    play(5)
    print(BOARD)
if __name__ == '__main__':
    main()