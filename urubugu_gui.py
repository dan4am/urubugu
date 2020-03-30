import board
import threading
import pygame
import os
import time
import math


_image_library = {}
DATABASE = []

def getpath(beads):
    result ="compressed_pictures1/"+str(beads)+"_beads.png"
    # print (result)
    return result
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def database():
    global DATABASE
    for bead in range (1,64):
        image = get_image(getpath(bead))
        DATABASE.append(image)

database()

def get_img(beads):
    path = getpath(beads)
    # return get_image(path)
    return DATABASE[beads - 1 ]

# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BEAD = 5
BETWEEN_SLOTS = 5
SLOTS = 40
BOARD_WIDTH = BETWEEN_SLOTS*6+ SLOTS*2 * 4
BOARD_LENGTH = BETWEEN_SLOTS*9+ SLOTS*2 * 8
back_button = [0,0]
done = False
# def Draw_board():



pygame.init()

# Set the width and height of the screen [width, height]
size = (800,600)
screen = pygame.display.set_mode(size)
circle_filled=pygame.Surface(size)
place =[(800-BOARD_LENGTH) / 2 , (600 - BOARD_WIDTH) / 2, BOARD_LENGTH, BOARD_WIDTH]


def draw_frame():
    pygame.draw.line(screen, BLACK, [54, 122], [54, 478], 1)
    pygame.draw.line(screen, BLACK, [744, 122], [744, 478], 1)
    pygame.draw.line(screen, BLACK, [54, 122], [743, 122], 1)
    pygame.draw.line(screen, BLACK, [54, 478], [743, 478], 1)
    pygame.draw.line(screen, WHITE, [57, 300], [742, 300], 8)
    pygame.draw.line(screen, BLACK, [54, 300], [743, 300], 2)

def board_coordinates_to_screen_coordinates(line, row):
        # result = board.hole_to_index(hole)
    if (line > 1):
        x = 57+BETWEEN_SLOTS + BETWEEN_SLOTS*row + SLOTS *2 *row + SLOTS
        y = 125+BETWEEN_SLOTS *2 + BETWEEN_SLOTS*line + SLOTS*2*line+ SLOTS
        return [x,y]
    else :
        x = 57+BETWEEN_SLOTS + BETWEEN_SLOTS * row + SLOTS * 2 * row + SLOTS
        y =125+ BETWEEN_SLOTS + BETWEEN_SLOTS * line + SLOTS * 2 * line + SLOTS
        return [x, y]


# font_obj = pygame.font.Font('freesansbold.ttf', 20)
# def how_many_beads(line,row):
#     result = str(board.BOARD[line][row])
#     return result



def draw_slots():
    # pygame.draw.circle(screen, WHITE, hole_to_coordinates(hole),40, 1)
    for line in range (len(board.BOARD)):
        for row in range (len(board.BOARD[0])):
            # circle_filled=pygame.Surface(size)
            pygame.draw.circle(screen, GREY, board_coordinates_to_screen_coordinates(line, row), SLOTS - 5)
            pygame.draw.circle(screen, WHITE, board_coordinates_to_screen_coordinates(line, row), SLOTS - 2, 1)# à revoir
            font_obj = pygame.font.Font('freesansbold.ttf', 10)
            text_surface_obj = font_obj.render(" "+str(board.BOARD[line][row]), False, BLACK, GREY)
            text_rect_obj = text_surface_obj.get_rect()
            x = board_coordinates_to_screen_coordinates(line, row)[0] + 32
            y=board_coordinates_to_screen_coordinates(line, row)[1] - 32
            text_rect_obj.center = (x, y)
            screen.blit(text_surface_obj, text_rect_obj)
            if(not board.BOARD[line][row] == 0):
                screen.blit(get_img(board.BOARD[line][row]), (board_coordinates_to_screen_coordinates(line, row)[0] - 65, board_coordinates_to_screen_coordinates(line, row)[1] - 68))
                pygame.draw.circle(screen, GREY, board_coordinates_to_screen_coordinates(line, row), SLOTS - 2, 1)


def draw():
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            global done
            done = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, place)
    draw_frame()
    draw_slots()
    player_display()
    # if (board.current_player == 1):
    #     font_obj = pygame.font.Font('freesansbold.ttf', 40)
    #     text_surface_obj = font_obj.render("Player one", False, GREEN, GREY)
    #     text_rect_obj = text_surface_obj.get_rect()
    #     text_rect_obj.center = (300, 500)
    #     screen.blit(text_surface_obj, text_rect_obj)
    pygame.display.flip()
    # player_display()


def game_coordinates_to_hole(x, y):
    result =[0,0]
    if (x >= 57 and x <= 742 ) and (y >= 125 and y <= 475):
        if( y >= 125 and y <= 300 ):
            result[0] = 2
            tmp = int((x - 57) / 85)
            if(tmp>=8) :
                slot_temp = 8
            else:
                slot_temp = tmp + 1
                slot_temp = 9 - slot_temp
            if (y>=125 and y<=207):
                result[1] = slot_temp
                return  result
            else:
                result[1] = 17-slot_temp
                return result
        else:
            result[0] = 1
            tmp = int((x - 57) / 85)
            if (tmp >= 8):
                slot_temp = 8
            else:
                slot_temp = tmp + 1
            if(y>300 and y <= 382 ):
                result[1] = 17-slot_temp
                return result
            else:
                result[1] = slot_temp
                return result

    elif (x >= back_button[0] - 60 and x <= back_button[0] + 60 and y >= back_button[1] - 20 and y <= back_button[1] + 20  ):
        return [3,0]
    else:
        return [0,0]


def play(hole):
    board.copier()
    result = board.beads(hole)
    current_hole = hole
    tmp_beads = board.beads(current_hole)
    loop = 0
    if (tmp_beads == 1):
        board.take_beads(current_hole,1)
        draw()
        time.sleep(0.5)
        if (current_hole == 16):
            current_hole = 1
        else:
            current_hole += 1
        board.add_bead(current_hole)
        draw()
        time.sleep(0.5)
        tmp_beads = board.beads(current_hole)
        # print(board.BOARD)
        if(current_hole > 8):
            result3 = board.hole_correspondance(current_hole)
            row2_crsp = result3[1]
            row1_crsp = result3[0]

            if (board.player_one):
                board.player(2)
            else:
                board.player(1)

            empty_p2_holes = board.beads(row1_crsp) == 0 and board.beads(row2_crsp) == 0
            if (not empty_p2_holes):
                beads_row1 = board.beads(row1_crsp)
                beads_row2 = board.beads(row2_crsp)
                tmp_beads = beads_row1 + beads_row2
                board.take_beads(row1_crsp, beads_row1)
                draw()
                time.sleep(0.5)
                board.take_beads(row2_crsp, beads_row2)
                draw()
                time.sleep(0.5)
                current_hole -= 1
                if (not board.player_one):
                    board.player(1)
                else:
                    board.player(2)
            else:
                if (not board.player_one):
                    board.player(1)

    while(not board.beads(current_hole)== 1):
        loop += 1
        print (loop)
        # print (BOARD)
        temp_hole = 0
        board.take_beads(current_hole, board.beads(current_hole))
        draw()
        time.sleep(0.5)

        for a_hole in range (current_hole, current_hole+tmp_beads):
            board.add_bead((a_hole % 16) + 1)
            draw()
            temp_hole = (a_hole % 16 )+ 1
            # print(BOARD)
            time.sleep(0.5)
            # gui.draw_frame()
        if(temp_hole>8):
            result2 = board.hole_correspondance(temp_hole)
            row2_crsp = result2[1]
            row1_crsp = result2[0]

            if(board.player_one) :board.player(2)
            else: board.player(1)

            empty_p2_holes = board.beads(row1_crsp) == 0 and board.beads(row2_crsp) == 0
            if(not empty_p2_holes):
                beads_row1 = board.beads(row1_crsp)
                beads_row2 = board.beads(row2_crsp)
                tmp_beads = beads_row1 + beads_row2
                board.take_beads(row1_crsp,beads_row1)
                draw()
                time.sleep(0.5)
                board.take_beads(row2_crsp,beads_row2)
                draw()
                time.sleep(0.5)
                if (not board.player_one):board.player(1)
                else:board.player(2)
            else:
                if (not board.player_one):
                    board.player(1)
                else:
                    board.player(2)
                current_hole = temp_hole
                tmp_beads = board.beads(current_hole)
        else:
            # if (not player_one):
            #     player(1)
            # else:
            #     player(2)
            current_hole = temp_hole
            tmp_beads = board.beads(current_hole)
        print(board.BOARD)

def player_display():
    # print(board.current_player)
    font_obj = pygame.font.Font('freesansbold.ttf', 40)
    text_surface_obj = font_obj.render(" Back ", False, WHITE, BLACK)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (70, 550)
    screen.blit(text_surface_obj, text_rect_obj)
    global back_button
    back_button = text_rect_obj.center
    if (board.current_player == 1):
        font_obj = pygame.font.Font('freesansbold.ttf', 40)
        text_surface_obj = font_obj.render("Player one", False, WHITE, BLACK)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (642, 515)
        screen.blit(text_surface_obj, text_rect_obj)
    else :
        font_obj = pygame.font.Font('freesansbold.ttf', 40)
        text_surface_obj = font_obj.render("Player two", False, BLACK, GREY)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (157, 85)
        screen.blit(text_surface_obj, text_rect_obj)

pygame.display.set_caption("URUBUGU")
def main():
    # Loop until the user clicks the close button.
    # done = False
    global done
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    draw()

    while ((not board.game_over()) and (not done)):
        # if (board.player_one):
        #     slot = int(input("player one choose slot between 1 and 16 : "))
        #     result = board.beads(slot)
        #     while (result == 0):
        #         slot = int(input("player one choose another slot between 1 and 16 that one is empty : "))
        #         result = board.beads(slot)
        #     play(slot)
        #     board.player(2)
        # else:
        #     slot = int(input("player two choose slot between 1 and 16 : "))
        #     result = board.beads(slot)
        #     while (result == 0):
        #         slot = int(input("player twoo choose another slot between 1 and 16 that one is empty : "))
        #         result = board.beads(slot)
        #     play(slot)
        #     board.player(1)

        # -------- Main Program Loop -----------
        place =[(800-BOARD_LENGTH) / 2 , (600 - BOARD_WIDTH) / 2, BOARD_LENGTH, BOARD_WIDTH]
        # board.player(2)
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # done = done or board.game_over()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position =pygame.mouse.get_pos()
                    print(position)
                    data = game_coordinates_to_hole(position[0],int(position[1]))
                    print(data)
                    if(not data[0] == 0):
                        player = data[0]
                        hole = data[1]

                        if (player == 1):
                            beads = board.beads(hole)
                            if(board.player_one and(not beads == 0)):
                                play(hole)
                                board.player(2)
                                board.current_player = 2
                            else:
                                # something to prevent to play for the other player
                                pass
                        elif(player == 2):
                            beads = board.beads(hole)
                            if(not board.player_one and (not beads == 0)):
                                play(hole)
                                board.player(1)
                                board.current_player = 1
                            else:
                                #something to prevent to play for the other player
                                pass
                        elif(player == 3):
                            board.back(board.back_Board)

        draw()
        clock.tick(60)
    pygame.quit()
    # pygame.quit()
    print ("fin")
    print (board.BOARD)
if __name__ == '__main__':
    main()
