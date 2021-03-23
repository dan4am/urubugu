import board
import numpy as np
import pygame
import os
import time
import artificial_intelligence


_image_library = {}
DATABASE = []
menu_path = "compressed_pictures1/menu_button.png"
restart_path = "compressed_pictures1/restart_button.png"
done_path = "compressed_pictures1/done.png"
player2_path = "compressed_pictures1/player2.png"
default_path = "compressed_pictures1/default.png"
dukenyure_button_unclicked_path = "picture/dukenyure_button_unclicked.png"
dukenyure_button_clicked_path = "picture/dukenyure_button_clicked.png"
dukenyure_button_clicked_path = "picture/dukenyure_button_clicked.png"
dukine_button_unclicked_path = "picture/dukine_button_unclicked.png"
dukine_button_clicked_path = "picture/dukine_button_clicked.png"
ingeneBakina_button_unclicked_path = "picture/ingeneBakina_button_uncliked.png"
ingeneBakina_button_clicked_path = "picture/ingeneBakina_button_cliked.png"
def getpath(beads):
    result ="compressed_pictures2/"+str(beads)+"_beads.png"
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
    for bead in range (1,65):
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
gukenyura_button=[0,0]
start_button=[0,0]
help_button =[0,0]
done = False
menu_game_gameover = 0#menu = 0, game = 1, gameover=2
GUKENYURA=3
MENU=0
REPLAY=2
PLAY=1
HELP=4
click_on_hole=5
vs_computer = True
# vs_computer = False
# def Draw_board():



pygame.init()

# Set the width and height of the screen [width, height]
size = (800,600)
screen = pygame.display.set_mode(size)
circle_filled=pygame.Surface(size)
place =[int((800-BOARD_LENGTH) / 2 ), int((600 - BOARD_WIDTH) / 2), BOARD_LENGTH, BOARD_WIDTH]

def change_state(state):
    global menu_game_gameover
    menu_game_gameover = state

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




def draw_slots():
    # pygame.draw.circle(screen, WHITE, hole_to_coordinates(hole),40, 1)
    for line in range (len(board.BOARD)):
        for row in range (len(board.BOARD[0])):
            # circle_filled=pygame.Surface(size)
            pygame.draw.circle(screen, GREY, board_coordinates_to_screen_coordinates(line, row), SLOTS - 5)
            pygame.draw.circle(screen, WHITE, board_coordinates_to_screen_coordinates(line, row), SLOTS - 2, 1)# à revoir
            font_obj = pygame.font.SysFont('comicsans.ttf', 15)
            text_surface_obj = font_obj.render(" "+str(board.BOARD[line][row]), False, BLACK, GREY)
            text_rect_obj = text_surface_obj.get_rect()
            x = board_coordinates_to_screen_coordinates(line, row)[0] + 32
            y=board_coordinates_to_screen_coordinates(line, row)[1] - 32
            text_rect_obj.center = (x, y)
            screen.blit(text_surface_obj, text_rect_obj)
            if(not board.BOARD[line][row] == 0):
                screen.blit(get_img(board.BOARD[line][row]), (board_coordinates_to_screen_coordinates(line, row)[0] - 65, board_coordinates_to_screen_coordinates(line, row)[1] - 55))
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
    # screen.blit(get_image(restart_path), 300, 200)
    pygame.display.flip()
    player_display()

def draw_end():
    screen.fill(BLACK)
    screen.blit(get_image(menu_path), (150,200))
    screen.blit(get_image(restart_path), (450,200))
    pygame.display.flip()

def draw_gukenyura():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, place)
    draw_frame()
    draw_slots()
    draw_gukenyura_buttons()
    pygame.display.flip()

def draw_gukenyura_buttons():
    screen.blit(get_image(done_path), (10, 540))
    # screen.blit(get_image(player2_path), (70, 540))
    screen.blit(get_image(default_path), (740, 540))

def draw_left_click(clicked, tmp_position,maximum,beads):
    draw_gukenyura_buttons()
    if (clicked == True):
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, place)
        draw_frame()
        draw_slots()
        draw_gukenyura_buttons()
        for i in range(0, 32):
            font_obj = pygame.font.SysFont('comicsans.ttf', 12)
            if (maximum - (i+1 - beads) >= 0 and maximum - (i+1 - beads) <= 32):
                text_surface_obj = font_obj.render(" " + str(i + 1) + " BEADS ", True, BLACK, GREY)
            else:
                text_surface_obj = font_obj.render(" " + str(i + 1) + " BEADS ", True, GREY, GREY)

            text_rect_obj = text_surface_obj.get_rect()
            if (i <= 15):
                text_rect_obj.center = (tmp_position[0] + 22, tmp_position[1] + i * 11 + 4)
                screen.blit(text_surface_obj, text_rect_obj)
            else:
                text_rect_obj.center = (tmp_position[0] + 22 + 43, tmp_position[1] + (i - 16) * 11 + 4)
                screen.blit(text_surface_obj, text_rect_obj)
        pygame.display.flip()
    else:
        screen.fill(WHITE)
        draw_gukenyura_buttons()
        pygame.draw.rect(screen, BLACK, place)
        draw_frame()
        draw_slots()
        pygame.display.flip()



def draw_menu():


    screen.fill(WHITE)
    # font_obj = pygame.font.SysFont('comicsans.ttf', 40)
    # text_surface_obj = font_obj.render(" Dutangure ", False, WHITE, BLACK)
    # text_rect_obj = text_surface_obj.get_rect()
    # text_rect_obj.center = (400, 300)
    # screen.blit(text_surface_obj, text_rect_obj)
    # global start_button
    # start_button = text_rect_obj.center
    #
    # font_obj = pygame.font.SysFont('comicsans.ttf', 40)
    # text_surface_obj = font_obj.render(" Dukenyure ", False, WHITE, BLACK)
    # text_rect_obj = text_surface_obj.get_rect()
    # text_rect_obj.center = (400, 268)
    # screen.blit(text_surface_obj, text_rect_obj)
    # global gukenyura_button
    # gukenyura_button = text_rect_obj.center
    #
    # font_obj = pygame.font.SysFont('comicsans.ttf', 40)
    # text_surface_obj = font_obj.render(" Ingene bakina ", False, WHITE, BLACK)
    # text_rect_obj = text_surface_obj.get_rect()
    # text_rect_obj.center = (400, 333)
    # screen.blit(text_surface_obj, text_rect_obj)
    # global help_button
    # help_button = text_rect_obj.center

    screen.blit(get_image(dukine_button_unclicked_path), (225, 185))
    global start_button
    start_button = [225,185]
    screen.blit(get_image(dukenyure_button_unclicked_path), (225, 265))
    global gukenyura_button
    gukenyura_button = [225, 265]
    screen.blit(get_image(ingeneBakina_button_unclicked_path), (225, 345))
    global help_button
    help_button = [225, 345]


    pygame.display.flip()


def game_coordinates_to_hole(x, y):
    result =[0,0]
    if(menu_game_gameover == MENU):
        if (x >= start_button[0] and x <= start_button[0] + 350 and y >= start_button[1] and y <= start_button[1] + 69  ):
            return [4,0]
        elif (x >= gukenyura_button[0] and x <= gukenyura_button[0] + 350 and y >= gukenyura_button[1] and y <= gukenyura_button[1] + 69  ):
            return [5,0]
        else:
            return[0,0]

    elif(menu_game_gameover == GUKENYURA):
        if (x >= 57 and x <= 742) and (y >= 125 and y <= 475):#in the board

            if (not (y >= 125 and y <= 300)):#in the 1st player half
                result[0] = 8
                tmp = int((x - 57) / 85)
                if (tmp >= 8):
                    slot_temp = 8
                else:
                    slot_temp = tmp + 1
                if (y > 300 and y <= 382):
                    result[1] = 17 - slot_temp
                    return result
                else:
                    result[1] = slot_temp
                    return result
            else :
                return [8,0]
        elif (x >= 740 and x <= 790) and (y >= 540 and y <= 590):#default button
            return [8,17]

        elif (x >= 10 and x <= 60) and (y >= 540 and y <= 590):#default button
            return [8,18]


        else : return [8,0]
    elif(menu_game_gameover == REPLAY):
        if(y > 210 and y <= 390 and x > 150 and x <= 350):
            return[6,0]
        elif(y > 210 and y <= 390 and x > 460 and x <= 640):
            return [7,0]
        else : return[0,0]
    elif(menu_game_gameover == 1):
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
    loop_can_go_on = True
    result = board.beads(hole)
    current_hole = hole
    tmp_beads = board.beads(current_hole)
    board.take_beads(current_hole, board.beads(current_hole))
    tmp_beads_at_previous_play = 0
    loop = 0
    if (tmp_beads == 1):
        # board.take_beads(current_hole,1)
        draw()
        time.sleep(0.5)
        if (current_hole == 16):
            current_hole = 1
        else:
            current_hole += 1
        board.add_bead(current_hole)
        draw()
        time.sleep(0.5)
        tmp_beads_at_previous_play = tmp_beads
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
                tmp_beads_at_previous_play = tmp_beads
                tmp_beads = beads_row1 + beads_row2
                if (not board.beads(row1_crsp) == 0):
                    time.sleep(0.5)
                    board.take_beads(row1_crsp, beads_row1)
                    draw()
                if (not board.beads(row2_crsp) == 0):
                    time.sleep(0.5)
                    board.take_beads(row2_crsp, beads_row2)
                    draw()
                current_hole -= 1
                if (not board.player_one):
                    board.player(1)
                else:
                    board.player(2)
            else:
                if (not board.player_one):
                    board.player(1)
                else:
                    board.player(2)

                if (board.beads(current_hole) == 1):
                    loop_can_go_on = False
                else:
                    loop_can_go_on = True
                    tmp_beads = board.beads(current_hole)
                    board.take_beads(current_hole, board.beads(current_hole))

        else:
            if(board.beads(current_hole) == 1):
                loop_can_go_on = False
            else:
                loop_can_go_on = True
                tmp_beads = board.beads(current_hole)
                board.take_beads(current_hole, board.beads(current_hole))
            ##if (tmp_beads >15 ):
    while(loop_can_go_on):
        loop += 1
        print (loop)
        # print (BOARD)
        temp_hole = 0
        # if(loop_can_go_on):

        draw()
        # time.sleep(0.5)

        for a_hole in range (current_hole+1, current_hole+tmp_beads+1):
            time.sleep(0.5)
            remainder = a_hole % 16
            if( remainder == 0):
                remainder = 16
            board.add_bead(remainder )
            draw()
            temp_hole = (remainder )
            # print(BOARD)

            # gui.draw_frame()
        if(temp_hole>8):
            result2 = board.hole_correspondance(temp_hole)
            row2_crsp = result2[1]
            row1_crsp = result2[0]

            if(board.player_one) :board.player(2)
            else: board.player(1)

            empty_p2_holes = board.beads(row1_crsp) == 0 and board.beads(row2_crsp) == 0
            if(not empty_p2_holes):
                loop_can_go_on = True
                beads_row1 = board.beads(row1_crsp)
                beads_row2 = board.beads(row2_crsp)
                tmp_beads_at_previous_play = tmp_beads
                tmp_beads = beads_row1 + beads_row2
                if (not board.beads(row1_crsp) == 0):
                    time.sleep(0.5)
                    board.take_beads(row1_crsp,beads_row1)
                    draw()
                if (not board.beads(row2_crsp) == 0):
                    time.sleep(0.5)
                    board.take_beads(row2_crsp,beads_row2)
                    draw()
                # time.sleep(0.5)
                if (not board.player_one):board.player(1)
                else:board.player(2)
            else: # if the corresponding rows in P2 are empty
                if (not board.player_one):
                    board.player(1)
                else:
                    board.player(2)
                if (board.beads(temp_hole) == 1):
                    loop_can_go_on = False
                else:
                    loop_can_go_on = True
                    current_hole = temp_hole
                    tmp_beads_at_previous_play = tmp_beads
                    tmp_beads = board.beads(current_hole)
                    time.sleep(0.5)
                    board.take_beads(current_hole, board.beads(current_hole))
        else:
            # if (not player_one):
            #     player(1)
            # else:
            #     player(2)
            if (board.beads(temp_hole) == 1):
                loop_can_go_on = False
            else:
                loop_can_go_on = True
                current_hole = temp_hole
                tmp_beads_at_previous_play = tmp_beads
                tmp_beads = board.beads(current_hole)
                time.sleep(0.5)
                board.take_beads(current_hole, board.beads(current_hole))
        print(board.BOARD)

def player_display():
    # print(board.current_player)
    font_obj = pygame.font.SysFont('comicsans.ttf', 40)
    text_surface_obj = font_obj.render(" Back ", False, WHITE, BLACK)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (70, 550)
    screen.blit(text_surface_obj, text_rect_obj)
    global back_button
    back_button = text_rect_obj.center
    if (board.current_player == 1):
        font_obj = pygame.font.SysFont('comicsans.ttf', 40)
        text_surface_obj = font_obj.render("Player one", False, WHITE, BLACK)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (642, 515)
        screen.blit(text_surface_obj, text_rect_obj)
    else :
        font_obj = pygame.font.SysFont('comicsans.ttf', 40)
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

    # draw()
    clicked_default = False
    while ( (not done)):

        if(menu_game_gameover == 1 ):  draw()
        elif(menu_game_gameover == 0 ):  draw_menu()
        elif(menu_game_gameover == 3) :
            if(clicked_default == False):
                board.choose_board(board.BOARD_gukenyura)
            draw_gukenyura()
            # clicked_default = False
        else:  draw_end()

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
                                if(board.game_over()):
                                    time.sleep(0.5)
                                    change_state(2)
                            else:
                                # something to prevent the other player to play
                                pass

                            if (vs_computer):
                                time.sleep(0.5)
                                hole_to_play = artificial_intelligence.hole_to_play_medium() #TODO if the game is over by the time player one finishes
                                #add averification for game over
                                beads = board.beads(hole_to_play)
                                if (not board.player_one and (not beads == 0)):
                                    # play(hole)
                                    play(hole_to_play)
                                    board.player(1)
                                    board.current_player = 1
                                    if (board.game_over()):
                                        time.sleep(0.5)
                                        change_state(2)
                                else:
                                    # something to prevent the other player to play
                                    pass
                        elif(player == 2 and (not vs_computer)):
                            beads = board.beads(hole)
                            # hole_to_play = artificial_intelligence.hole_to_play()
                            if(not board.player_one and (not beads == 0)):
                                play(hole)
                                # play(hole_to_play)
                                board.player(1)
                                board.current_player = 1
                                if (board.game_over()):
                                    time.sleep(0.5)
                                    change_state(2)
                            else:
                                # something to prevent the other player to play
                                pass
                        elif(player == 3):
                            board.back(board.back_Board)
                        elif(player == 4):
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                screen.blit(get_image(dukine_button_clicked_path), (225, 185))
                                screen.blit(get_image(dukenyure_button_unclicked_path), (225, 265))
                                screen.blit(get_image(ingeneBakina_button_unclicked_path), (225, 345))


                                pygame.display.flip()
                                pygame.event.pump()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        done = True
                                        # done = done or board.game_over()
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        tmp_pos = pygame.mouse.get_pos();
                                        if (tmp_pos[0] >= start_button[0] and tmp_pos[0] <= start_button[0] + 350 and tmp_pos[1] >= start_button[
                                            1] and tmp_pos[1] <= start_button[1] + 69):
                                            change_state(1)
                                            # continue
                                clock.tick(60)
                                   # draw()
                        elif(player == 5):
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                screen.blit(get_image(dukine_button_unclicked_path), (225, 185))
                                screen.blit(get_image(dukenyure_button_clicked_path), (225, 265))
                                screen.blit(get_image(ingeneBakina_button_unclicked_path), (225, 345))


                                pygame.display.flip()
                                pygame.event.pump()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        done = True
                                        # done = done or board.game_over()
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        tmp_pos = pygame.mouse.get_pos();
                                        if (tmp_pos[0] >= gukenyura_button[0] and tmp_pos[0] <= gukenyura_button[0] + 350 and
                                                tmp_pos[1] >= gukenyura_button[1] and tmp_pos[1] <= gukenyura_button[1] + 69):
                                            change_state(3)
                                            board.player(1)
                                            draw_gukenyura_buttons()
                                clock.tick(60)


                            # board.choose_board(board.BOARD_gukenyura)
                        elif (player == 6):
                            change_state(0)
                        elif (player == 7):
                            change_state(1)
                            board.BOARD = np.copy(board.BOARD_DEFAULT)

                        elif (player == 8):
                            if (clicked_default == True):
                                maximum = 0
                            else: maximum=32

                            if(data[1] >=1 and data[1]<=16):
                                clicked = True
                                tmp_position =[0,0]
                                tmp_position[0] = position[0]
                                tmp_position[1] = position[1]
                                done_gukenyura = False
                                while(not done_gukenyura):
                                    tmp_data = game_coordinates_to_hole(tmp_position[0],
                                                                        int(tmp_position[1]))
                                    beads_to_take = board.beads(tmp_data[1])
                                    draw_left_click(clicked,tmp_position,maximum,beads_to_take)
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            pygame.display.flip()
                                            # done = done or board.game_over()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if event.button == 1:
                                                if(clicked == False):
                                                    position = pygame.mouse.get_pos()
                                                    data = game_coordinates_to_hole(position[0], int(position[1]))
                                                    print(position)
                                                    print(data)
                                                    if((data[1] >=1 and data[1]<=16)):
                                                            clicked = True
                                                            tmp_position[0] = position[0]
                                                            tmp_position[1] = position[1]
                                                            print(position)
                                                            print(tmp_position)
                                                            print(data)
                                                    elif(data[1]==17):
                                                        clicked = False
                                                        board.default_player1()
                                                        maximum = 0
                                                    elif (data[1] == 18):
                                                        change_state(1)
                                                        board.default_player2()
                                                        done_gukenyura = True
                                                else:
                                                    position = pygame.mouse.get_pos()
                                                    data = game_coordinates_to_hole(position[0], int(position[1]))
                                                    if (data[1] >=1 and data[1]<=16):
                                                        if (not( (position[0] > tmp_position[0] and position[0] <= tmp_position[
                                                            0] + 85) and (position[1] > tmp_position[1] and position[1]<= tmp_position[1] + 175))):
                                                            clicked = True
                                                            tmp_position[0] = position[0]
                                                            tmp_position[1] = position[1]
                                                            print(position)
                                                            print(data)
                                                        else:
                                                            clicked = False
                                                            number_of_beads = 0
                                                            temp =   position[1] - tmp_position[1]
                                                            temp = int (temp /11) + 1
                                                            temp_x = position[0]- tmp_position[0]
                                                            temp_x = int(temp_x / 42) + 1
                                                            if temp_x == 1 : number_of_beads = temp
                                                            elif temp_x == 2 : number_of_beads = temp + 16
                                                            print(maximum)
                                                            tmp_data = game_coordinates_to_hole(tmp_position[0],
                                                                                            int(tmp_position[1]))
                                                            beads_to_take = board.beads(tmp_data[1])
                                                            tmp_max = maximum - (number_of_beads - beads_to_take)
                                                            # maximum = maximum - (number_of_beads - beads_to_take)
                                                            print(tmp_max)
                                                            if (tmp_max >= 0 and tmp_max <= 32):
                                                                maximum = tmp_max
                                                                board.take_beads(tmp_data[1], beads_to_take)
                                                                for i in range(1, number_of_beads + 1):
                                                                    board.add_bead(tmp_data[1])
                                                            print(position)
                                                            data = game_coordinates_to_hole(position[0], int(position[1]))
                                                            print(data)
                                                    elif(data[1]==17):
                                                        clicked = False
                                                        board.default_player1()
                                                        maximum = 0
                                                    elif (data[1] == 18):
                                                        change_state(1)
                                                        board.default_player2()
                                                        done_gukenyura = True
                                                    elif(data[1] == 0):
                                                        clicked = False
                                                        if (((position[0] > tmp_position[0] and position[0] <=
                                                                  tmp_position[
                                                                      0] + 85) and (
                                                                         position[1] > tmp_position[1] and position[
                                                                     1] <= tmp_position[1] + 175))):
                                                            number_of_beads = 0
                                                            temp = position[1] - tmp_position[1]
                                                            temp = int(temp / 11) + 1
                                                            temp_x = position[0] - tmp_position[0]
                                                            temp_x = int(temp_x / 42) + 1
                                                            if temp_x == 1:
                                                                number_of_beads = temp
                                                            elif temp_x == 2:
                                                                number_of_beads = temp + 16

                                                            tmp_data = game_coordinates_to_hole(tmp_position[0],
                                                                                                int(tmp_position[1]))
                                                            beads_to_take = board.beads(tmp_data[1])
                                                            tmp_max = maximum - (number_of_beads - beads_to_take)
                                                            # maximum = maximum - (number_of_beads - beads_to_take)
                                                            print(tmp_max)
                                                            if(tmp_max >= 0 and tmp_max <= 32):
                                                                maximum = tmp_max
                                                                board.take_beads(tmp_data[1], beads_to_take)
                                                                for i in range(1, number_of_beads + 1):
                                                                    board.add_bead(tmp_data[1])
                                                            print(position)
                                                            data = game_coordinates_to_hole(position[0], int(position[1]))
                                                            print(data)

                                    clock.tick(60)
                            elif(data[1] == 17):
                                clicked_default = True
                                board.default_player1()
                            elif (data[1] == 18):
                                change_state(1)
                                board.default_player2()
                                done_gukenyura = True


        clock.tick(60)
    pygame.quit()
    # pygame.quit()
    print ("fin")
    print (board.BOARD)
if __name__ == '__main__':
    main()
