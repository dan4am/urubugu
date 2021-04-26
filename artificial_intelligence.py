import board
import numpy as np



def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor][1] <= right[right_cursor][1]:
            merged[left_cursor + right_cursor]= left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def beads_left(player):

    result  = 0
    if (player == 1):
        for i in range(2,4):
            for j in range (0,8):
                result = result + board.BOARD_AI[i][j]
    else:
        for i in range(0,2):
            for j in range (0,8):
                result = result + board.BOARD_AI[i][j]

    return result


def simulate_one_play(hole):
    board.copy_to_board_ai()

    if (board.current_player == 1):
        original_opponents_beads = beads_left(2)
    else:
        original_opponents_beads = beads_left(1)
    # board.BOARD_AI = np.copy(board.BOARD)

    original_board = np.copy(board.BOARD_AI)
    board.play_AI(hole,board.BOARD_AI)
    remaining_opponents_beads = 0
    if (board.current_player == 1):
        remaining_opponents_beads = beads_left(2)
    else:
        remaining_opponents_beads = beads_left(1)

    board.BOARD_AI = np.copy(original_board)
    opponnents_loss  = original_opponents_beads - remaining_opponents_beads
    return (hole,remaining_opponents_beads,opponnents_loss)

def simulate_all_the_plays():

    result = []
    for hole in range(1, 17):
        if (not board.beads(hole) == 0):
            temp = simulate_one_play(hole)
            result.append(temp)

    return merge_sort(result)


def hole_to_play_hard():
    result = simulate_all_the_plays()

    if not result[0][2] == 0:
        if result[0][1] == 0:
            return result[0][0]
    elif result[0][2] == 0:
        pass



def hole_to_play_medium():
    return (simulate_all_the_plays()[0][0])




def main():
    print (str(beads_left(2)))

    print (simulate_all_the_plays())
    print (hole_to_play_medium())

if __name__ == "__main__":
    main()