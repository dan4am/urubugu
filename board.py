import numpy as np

# BOARD = np.zeros((4,8), int)
# BOARD = np.array([ [2,  2,  2,  2,  2,  2,  2,  2],
#                    [2,  2,  2,  2,  2,  2,  2,  2],
#                    [0,  4,  4,  4,  4,  0,  0,  0],
#                    [0,  4,  4,  4,  4,  0,  0,  0]])

BOARD = np.array([ [0,  0,  0,  0,  0,  0,  1,  0],
                   [0,  0,  0,  1,  1,  3,  0,  2],
                   [4,  4,  4,  4,  0,  0,  17,  0],
                   [0,  4,  4,  4,  3,  0,  0,  1]])

BOARD_DEFAULT = np.array([ [2,  2,  2,  2,  2,  2,  2,  2],
                           [2,  2,  2,  2,  2,  2,  2,  2],
                           [2,  2,  2,  2,  2,  2,  2,  2],
                           [2,  2,  2,  2,  2,  2,  2,  2]])

BOARD_DEFAULT_P1 = np.array([[0,  0,  0,  0,  0,  0,  0,  0],
                             [0,  0,  0,  0,  0,  0,  0,  0],
                             [2,  2,  2,  2,  2,  2,  2,  2],
                             [2,  2,  2,  2,  2,  2,  2,  2]])

BOARD_DEFAULT_P2 = np.array([[2,  2,  2,  2,  2,  2,  2,  2],
                             [2,  2,  2,  2,  2,  2,  2,  2],
                             [0,  0,  0,  0,  0,  0,  0,  0],
                             [0,  0,  0,  0,  0,  0,  0,  0]
                           ])

BOARD_REPLAY = np.array([ [0,  0,  0,  0,  0,  0,  0,  0],
                        [0,  0,  0,  0,  0,  0,  2,  0],
                        [0,  4,  4,  4,  4,  0,  0,  0],
                        [0,  4,  4,  4,  4,  0,  0,  0]])

BOARD_gukenyura = np.array([ [0,  0,  0,  0,  0,  0,  0,  0],
                             [0,  0,  0,  0,  0,  0,  0,  0],
                             [0,  0,  0,  0,  0,  0,  0,  0],
                             [0,  0,  0,  0,  0,  0,  0,  0]])
MAX_INIT = 4
MAX_BEADS = 64
player_one = True
in_the_back = True
in_front = not in_the_back
current_player = 1
back_Board = BOARD.copy()
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

def copier():
    global back_Board
    for line in range (len (BOARD)):
        for row in range (len(BOARD[0])):
            back_Board[line][row] = BOARD[line][row]


def play(hole):
    copier()
    loop_can_go_on = True
    result = beads(hole)
    current_hole = hole
    tmp_beads = beads(current_hole)
    take_beads(current_hole, beads(current_hole))
    tmp_beads_at_previous_play = 0
    loop = 0
    if (tmp_beads == 1):
        # board.take_beads(current_hole,1)
        if (current_hole == 16):
            current_hole = 1
        else:
            current_hole += 1
        add_bead(current_hole)
        tmp_beads_at_previous_play = tmp_beads
        tmp_beads = beads(current_hole)
        # print(BOARD)
        if (current_hole > 8):
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
                tmp_beads_at_previous_play = tmp_beads
                tmp_beads = beads_row1 + beads_row2
                if (not beads(row1_crsp) == 0):
                    take_beads(row1_crsp, beads_row1)
                if (not beads(row2_crsp) == 0):
                    take_beads(row2_crsp, beads_row2)
                current_hole -= 1
                if (not player_one):
                    player(1)
                else:
                    player(2)
            else:
                if (not player_one):
                    player(1)
                else:
                    player(2)

                if (beads(current_hole) == 1):
                    loop_can_go_on = False
                else:
                    loop_can_go_on = True
                    tmp_beads = beads(current_hole)
                    take_beads(current_hole, beads(current_hole))
        else:
            if (beads(current_hole) == 1):
                loop_can_go_on = False
            else:
                loop_can_go_on = True
                tmp_beads = beads(current_hole)
                take_beads(current_hole, beads(current_hole))
            ##if (tmp_beads >15 ):
    while (loop_can_go_on):
        loop += 1
        print(loop)
        # print (BOARD)
        temp_hole = 0
        # if(loop_can_go_on):

        for a_hole in range(current_hole + 1, current_hole + tmp_beads + 1):

            remainder = a_hole % 16
            if (remainder == 0):
                remainder = 16
            add_bead(remainder)
            temp_hole = (remainder)

        if (temp_hole > 8):
            result2 = hole_correspondance(temp_hole)
            row2_crsp = result2[1]
            row1_crsp = result2[0]

            if (player_one):
                player(2)
            else:
                player(1)
            empty_p2_holes = beads(row1_crsp) == 0 and beads(row2_crsp) == 0
            if (not empty_p2_holes):
                loop_can_go_on = True
                beads_row1 = beads(row1_crsp)
                beads_row2 = beads(row2_crsp)
                tmp_beads_at_previous_play = tmp_beads
                tmp_beads = beads_row1 + beads_row2
                if (not beads(row1_crsp) == 0):

                    take_beads(row1_crsp, beads_row1)

                if (not beads(row2_crsp) == 0):

                    take_beads(row2_crsp, beads_row2)

                if (not player_one):
                    player(1)
                else:
                    player(2)
            else:  # if the corresponding rows in P2 are empty
                if (not player_one):
                    player(1)
                else:
                    player(2)
                if (beads(temp_hole) == 1):
                    loop_can_go_on = False
                else:
                    loop_can_go_on = True
                    current_hole = temp_hole
                    tmp_beads_at_previous_play = tmp_beads
                    tmp_beads = beads(current_hole)

                    take_beads(current_hole, beads(current_hole))
        else:
            if (beads(temp_hole) == 1):
                loop_can_go_on = False
            else:
                loop_can_go_on = True
                current_hole = temp_hole
                tmp_beads_at_previous_play = tmp_beads
                tmp_beads = beads(current_hole)

                take_beads(current_hole, beads(current_hole))
        print(BOARD)


def back(board):
    for line in range(len (board)):
        for row in range (len (board[0])):
            BOARD[line][row] = board[line][row]
    if (player_one) :
        player(2)
        global current_player
        current_player = 2
    else :
        player(1)
        current_player = 1

def choose_board(board):
    for line in range(len (board)):
        for row in range (len (board[0])):
            BOARD[line][row] = board[line][row]

def default_player1():
    for x in range (2,4):
        for y in range (0,8):
            BOARD[x][y] = 2

def default_player2():
    for x in range (0,2):
        for y in range (0,8):
            BOARD[x][y] = 2

def game_over():
    gameover=True
    for hole in range (1, 17):
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



####################################################GUI#########################################################"




def main():

    player(1)
    two_players()
    # play(1)
    # play(6)
    print(BOARD)
if __name__ == '__main__':
    main()