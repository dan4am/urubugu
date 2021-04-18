import board
import numpy as np
import pygame
import os
import time
import artificial_intelligence
from network import Network
import online_helper


_image_library = {}


config_language = "fr"
languages = ["bi", "en"]
# design = "design_1/"
design = "design_2/"
DATABASE = []

####################
# play state assets#
####################

player1_banner_path="buttons/"+design+config_language+"/player1_banner.png"
player2_banner_path="buttons/"+design+config_language+"/player2_banner.png"
back_button_clicked_path = "buttons/"+design+config_language+"/back_button_clicked.png"
back_button_unclicked_path = "buttons/"+design+config_language+"/back_button_unclicked.png"
hider_pannel_path = "buttons/"+design+"/hider_white.png"


###################
# game-over assets#
###################

menu_path = "compressed_pictures1/menu_button.png"
restart_path = "compressed_pictures1/restart_button.png"

###################
# gukenyura assets#
###################

done_path = "buttons/"+design+"/done_button_unclicked.png"
done_unclicked_path = "buttons/"+design+"/done_button_unclicked.png"
done_clicked_path = "buttons/"+design+"/done_button_clicked.png"
player2_path = "compressed_pictures1/player2.png"
default_path="buttons/"+design+"/bi/default_button_unclicked.png"
default_unclicked_path = "buttons/"+design+config_language+"/default_button_unclicked.png"
default_clicked_path = "buttons/"+design+config_language+"/default_button_clicked.png"
menu_gukenyura_button_unclicked_path="buttons/"+design+"/menu_gukenyura_button_unclicked.png"
menu_gukenyura_button_clicked_path="buttons/"+design+"/menu_gukenyura_button_clicked.png"


##################
# language assets#
##################


dukenyure_button_unclicked_path = "buttons/"+design+config_language+"/dukenyure_button_unclicked.png"
dukenyure_button_clicked_path = "buttons/"+design+config_language+"/dukenyure_button_clicked.png"
dukenyure_button_clicked_path = "buttons/"+design+config_language+"/dukenyure_button_clicked.png"
dukine_button_unclicked_path = "buttons/"+design+config_language+"/dukine_button_unclicked.png"
dukine_button_clicked_path = "buttons/"+design+config_language+"/dukine_button_clicked.png"
ingeneBakina_button_unclicked_path = "buttons/"+design+config_language+"/ingeneBakina_button_uncliked.png"
ingeneBakina_button_clicked_path = "buttons/"+design+config_language+"/ingeneBakina_button_cliked.png"

#language button

bi_flag_path = "buttons/flag_bi.png"
fr_flag_path = "buttons/flag_fr.png"
en_flag_path = "buttons/flag_en.png"

def get_flag_path(flag):
    if(flag == "bi" ):
        return bi_flag_path
    elif(flag == "fr"):
        return fr_flag_path
    else:
        return en_flag_path

language_drop_down_button_clicked_path = "buttons/"+design+"language_drop_down_menu_clicked.png"
language_drop_down_button_unclicked_path = "buttons/"+design+"language_drop_down_menu_unclicked.png"
language_drop_down_path = "buttons/"+design+"language_drop_down.png"

def animate_drop_down_button(clock):
    time = 0
    destination = 0


    vitesse = 3
    acceleration = 0.528
    screen.blit(get_image(background_click_path), (0, 0))
    while (not destination >= 70):

        destination = int(-0.5 * acceleration * time * time) + (vitesse * time) + destination
        screen.blit(

            pygame.transform.smoothscale(get_image(language_drop_down_path),
                                         (75, 35+destination)), (50, 30 ))

        for i in range(2):
            if (not languages[i] == config_language):
                ##ANIMATION ALTERNATIVE

                # screen.blit(pygame.transform.smoothscale(
                #     get_image(get_flag_path(languages[i])), (38, int(destination* (5/14)))),
                #     (56, 68 + i * 35 ))

                screen.blit(pygame.transform.smoothscale(
                    get_image(get_flag_path(languages[i])), (38, 25)),
                    (56, 68 + i * 35 - 70 + destination))

        path = "buttons/design_2/masquer scroll down.png"
        screen.blit(pygame.transform.smoothscale(
            get_image(path), (75, 30)),
            (50, 0))


        screen.blit(pygame.transform.smoothscale(
            get_image(language_drop_down_button_clicked_path), (75, 35)),
            (50, 30))

        screen.blit(pygame.transform.smoothscale(
            get_image(get_flag_path(config_language)), (38, 25)), (56, 35))

        pygame.display.flip()
        clock.tick(60)
        time += 1



selection_flag_path = "buttons/"+design+"selection_of_flag.png"
selection_flag_path_white = "buttons/"+design+"selection_of_flag_white.png"
selection_flag_path2 = "buttons/"+design+"selection_of_flag2.png"
selection_flag_path2_white = "buttons/"+design+"selection_of_flag2_white.png"
background_click_path = "buttons/background_click.png"


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
language_button=[0,0]
language_button_choice_1=[0,0]
language_button_choice_2=[0,0]
done = False
menu_game_gameover = 0 #menu = 0, game = 1, gameover=2, gukenyura = 3
GUKENYURA=3
MENU=0
REPLAY=2
PLAY=1
HELP=4
click_on_hole = 5
vs_computer = True
# vs_computer = False
# def Draw_board():



pygame.init()

# Set the width and height of the screen [width, height]
size = (800,600)
screen = pygame.display.set_mode(size)
circle_filled=pygame.Surface(size)
place =[int((800-BOARD_LENGTH) / 2 ), int((600 - BOARD_WIDTH) / 2), BOARD_LENGTH, BOARD_WIDTH]

def change_language(language):
    global config_language, dukenyure_button_clicked_path, dukenyure_button_unclicked_path, dukine_button_clicked_path, \
        dukine_button_unclicked_path, ingeneBakina_button_unclicked_path, ingeneBakina_button_clicked_path,\
        default_clicked_path,default_unclicked_path,back_button_unclicked_path,back_button_clicked_path,player1_banner_path,player2_banner_path
    if language == languages[0]:
        languages[0] = config_language
        config_language = language
    else:
        languages[1] = config_language
        config_language = language

    dukenyure_button_unclicked_path = "buttons/"+design+"/"+ language +"/dukenyure_button_unclicked.png"
    dukenyure_button_clicked_path="buttons/"+design+"/"+ language +"/dukenyure_button_clicked.png"
    dukine_button_unclicked_path="buttons/"+design+"/"+ language +"/dukine_button_unclicked.png"
    dukine_button_clicked_path = "buttons/"+design+"/"+ language +"/dukine_button_clicked.png"
    ingeneBakina_button_clicked_path="buttons/"+design+"/"+ language +"/ingeneBakina_button_cliked.png"
    ingeneBakina_button_unclicked_path="buttons/"+design+"/"+ language +"/ingeneBakina_button_uncliked.png"
    default_clicked_path = "buttons/"+design+"/"+ language +"/default_button_clicked.png"
    default_unclicked_path = "buttons/"+design+"/"+ language +"/default_button_unclicked.png"
    back_button_unclicked_path = "buttons/"+design+"/"+ language +"/back_button_unclicked.png"
    back_button_clicked_path = "buttons/"+design+"/"+ language +"/back_button_clicked.png"
    player1_banner_path="buttons/"+design+"/"+ language +"/player1_banner.png"
    player2_banner_path="buttons/"+design+"/"+ language +"/player2_banner.png"


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


def draw(back = None):
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
    if (back):
        player_display(back = 1)
    else:
        player_display()

def draw_end():
    screen.fill(BLACK)
    screen.blit(get_image(menu_path), (150,200))
    screen.blit(get_image(restart_path), (450,200))
    pygame.display.flip()

def draw_gukenyura(default = None, done = None, menu = None):
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, place)
    draw_frame()
    draw_slots()

    if (default):
        draw_gukenyura_buttons(default=1)
    elif (done):
        draw_gukenyura_buttons(done=1)
    else:
        draw_gukenyura_buttons()
    if (menu):
        draw_gukenyura_buttons(menu=1)
    elif (menu):
        draw_gukenyura_buttons(menu=1)

    pygame.display.flip()




def draw_gukenyura_buttons(default = None, done = None, menu = None):
    if(done):
        screen.blit(pygame.transform.smoothscale(get_image(done_clicked_path),(92,52)), (30, 520))
    else:
        screen.blit(pygame.transform.smoothscale(get_image(done_unclicked_path),(92,52)), (30, 520))

    if (default):
        screen.blit(pygame.transform.smoothscale(get_image(default_clicked_path),(92,52)), (678, 520))
    else:
        screen.blit(pygame.transform.smoothscale(get_image(default_unclicked_path), (92, 52)), (678, 520))

    if (menu):
        screen.blit(pygame.transform.smoothscale(get_image(menu_gukenyura_button_clicked_path),(40,40)), (30, 30))
    else:
        screen.blit(pygame.transform.smoothscale(get_image(menu_gukenyura_button_unclicked_path), (40, 40)), (30, 30))

    # screen.blit(get_image(player2_path), (70, 540))


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



def draw_menu(play = None, set = None, lang = None, help = None):


    screen.fill(WHITE)

    if(play):
        screen.blit(pygame.transform.smoothscale(get_image(dukine_button_clicked_path), (350,69)), (225, 185))
    else:
        screen.blit(pygame.transform.smoothscale(get_image(dukine_button_unclicked_path), (350,69)), (225, 185))
    global start_button
    start_button = [225,185]

    if(set):
        screen.blit(pygame.transform.smoothscale(get_image(dukenyure_button_clicked_path), (350,69)), (225, 265))
    else:
        screen.blit(pygame.transform.smoothscale(get_image(dukenyure_button_unclicked_path), (350, 69)), (225, 265))
    global gukenyura_button
    gukenyura_button = [225, 265]

    if(help):
        screen.blit(pygame.transform.smoothscale(get_image(ingeneBakina_button_clicked_path),(350,69)), (225, 345))
    else:
        screen.blit(pygame.transform.smoothscale(get_image(ingeneBakina_button_unclicked_path), (350, 69)), (225, 345))
    global help_button
    help_button = [225, 345]

    if (lang == 2):
        screen.blit(get_image(background_click_path), (0, 0))
        screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_path), (75, 105)), (50, 30))
        screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_button_clicked_path), (75,35)), (50,30))

        for i in range(2):
            if(not languages[i] == config_language):
                screen.blit(pygame.transform.smoothscale(get_image(get_flag_path(languages[i])), (38, 25)), (56, 68 + i * 35 ))
    elif(lang == 1):
        screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_button_clicked_path), (75, 35)), (50, 30))
    else:
        screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_button_unclicked_path), (75, 35)),
                    (50, 30))

    global language_button
    language_button = [50, 30]
    screen.blit(pygame.transform.smoothscale(get_image(get_flag_path(config_language)), (38,25)), (56,35))
    # pygame.transform.smoothscale(get_image(getpath(self.intoke)), (105, 161))

    pygame.display.flip()


def game_coordinates_to_hole(x, y):
    result =[0,0]
    if(menu_game_gameover == MENU):
        if (x >= start_button[0] and x <= start_button[0] + 350 and y >= start_button[1] and y <= start_button[1] + 69  ):
            return [4,0]
        elif (x >= gukenyura_button[0] and x <= gukenyura_button[0] + 350 and y >= gukenyura_button[1] and y <= gukenyura_button[1] + 69  ):
            return [5,0]

        elif (x >= language_button[0] and x <= language_button[0] + 74 and y >= language_button[1] and y <= language_button[1] + 35  ):
            return [20,0]
        # (74, 35)
        elif (x >= help_button[0] and x <= help_button[0] + 350 and y >= help_button[1] and y <= help_button[1] + 69  ):
            return [21,0]

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
        elif (x >= 678 and x <= 770) and (y >= 520 and y <= 572):#default button
            return [8,17]

        elif (x >= 30 and x <= 122) and (y >= 520 and y <= 572):#done button
            return [8,18]

        elif (x >= 30 and x <= 70) and (y >= 30 and y <= 70):#back to menu button
            return [8,19]

        else : return [8,0]
    elif(menu_game_gameover == REPLAY):
        if(y > 210 and y <= 390 and x > 150 and x <= 350):
            return[6,0]
        elif(y > 210 and y <= 390 and x > 460 and x <= 640):
            return [7,0]
        else : return[0,0]
    elif(menu_game_gameover == PLAY):
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

        elif (x >= back_button[0] and x <= back_button[0] + 105 and y >= back_button[1] and y <= back_button[1] +  50 ):
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

def player_display(back = None):
    global back_button
    if(back):
        screen.blit(pygame.transform.smoothscale(get_image(back_button_clicked_path), (105, 50)), (50, 510))
        back_button = (50,510)
    else:
        screen.blit(pygame.transform.smoothscale(get_image(back_button_unclicked_path), (105, 50)), (50, 510))
        back_button = (50, 510)

    if (board.current_player == 1):

        screen.blit(pygame.transform.smoothscale(get_image(player1_banner_path), (310, 63)), (447, 485))
    else :

        screen.blit(pygame.transform.smoothscale(get_image(player2_banner_path), (310, 63)), (47, 55))

pygame.display.set_caption("URUBUGU")










def main():

    global done
    clock = pygame.time.Clock()
    n = Network()
    online_player_id = n.player_number

    ######Preparing the online game###############

    if (online_player_id):
        online_player_id = online_player_id[-1]
        board.player(int(online_player_id))
        print("online player_id =" + str (online_player_id))
        pygame.display.set_caption("URUBUGU + player" +str(online_player_id) )















    # -------- Main Program Loop -----------
    clicked_default = False
    while ( (not done)):

        if(menu_game_gameover == 1 ):  draw()
        elif(menu_game_gameover == 0 ):
            if(design == "design_2/"):
                position_menu = pygame.mouse.get_pos()
                x= position_menu[0]
                y= position_menu[1]
                if (x >= start_button[0] and x <= start_button[0] + 350 and y >= start_button[1] and y <= start_button[
                    1] + 69):
                    draw_menu(play=1)
                elif (x >= gukenyura_button[0] and x <= gukenyura_button[0] + 350 and y >= gukenyura_button[1] and y <=
                      gukenyura_button[1] + 69):
                    draw_menu(set=1)
                elif (x >= language_button[0] and x <= language_button[0] + 74 and y >= language_button[1] and y <=
                      language_button[1] + 35):
                    draw_menu(lang=1)
                elif (x >= help_button[0] and x <= help_button[0] + 350 and y >= help_button[1] and y <=
                      help_button[1] + 69):
                    draw_menu(help=1)
                else:
                    draw_menu()
            else:
                draw_menu()
        elif(menu_game_gameover == 3) :
            if(clicked_default == False):
                board.choose_board(board.BOARD_gukenyura)
            draw_gukenyura()
            # clicked_default = False
        else:  draw_end()


        place =[(800-BOARD_LENGTH) / 2 , (600 - BOARD_WIDTH) / 2, BOARD_LENGTH, BOARD_WIDTH]
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
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
                            while not event.type == pygame.MOUSEBUTTONUP:
                                tmp_pos = pygame.mouse.get_pos();
                                if (tmp_pos[0] >= back_button[0] and tmp_pos[0] <= back_button[0] + 105
                                        and tmp_pos[1] >= back_button[1] and tmp_pos[1] <= back_button[1] + 50):
                                    screen.blit(
                                        pygame.transform.smoothscale(get_image(hider_pannel_path), (105, 60)),
                                        (50, 510))
                                    screen.blit(
                                        pygame.transform.smoothscale(get_image(back_button_clicked_path), (105, 50)),
                                        (50, 510))
                                    # draw(back=1)
                                    pass
                                else:
                                    screen.blit(
                                        pygame.transform.smoothscale(get_image(hider_pannel_path), (105, 60)),
                                        (50, 510))

                                    screen.blit(
                                        pygame.transform.smoothscale(get_image(back_button_unclicked_path), (105, 50)),
                                        (50, 510))
                                    # draw()
                                pygame.display.flip()
                                pygame.event.pump()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        # done = done or board.game_over()
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        tmp_pos = pygame.mouse.get_pos()
                                        if (tmp_pos[0] >= back_button[0] and tmp_pos[0] <= back_button[0] + 105
                                        and tmp_pos[1] >= back_button[1] and tmp_pos[1] <= back_button[1] + 50):
                                            board.back(board.back_Board)


                        elif(player == 4): # click on Dukine (Play) button
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos();
                                if (tmp_pos[0] >= start_button[0] and tmp_pos[0] <= start_button[0] + 350 and
                                        tmp_pos[1] >= start_button[1] and tmp_pos[1] <= start_button[1] + 69):
                                    draw_menu(play=1)
                                else:
                                    draw_menu()

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
                                            board.choose_board(board.BOARD_REPLAY)
                                            reply = online_helper.get_starting_setting(n)
                                            print(reply)
                                            result2 = online_helper.string_to_list(reply)
                                            board.player(2)
                                            for i in range (len (result2)):
                                                board.add_beads(i+1, result2[i])
                                            board.player(1)
                                            change_state(1)
                                            # board.player(2)
                                            # print(board.stringify())
                                            # continue
                                clock.tick(60)

                        elif(player == 5):#click on dukenyure (setting up board) button
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos();
                                if (tmp_pos[0] >= gukenyura_button[0] and tmp_pos[0] <= gukenyura_button[0] + 350 and
                                        tmp_pos[1] >= gukenyura_button[1] and tmp_pos[1] <= gukenyura_button[1] + 69):
                                    draw_menu(set=1)
                                else:
                                    draw_menu()

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
                                clock.tick(40)

                        elif (player == 20):
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos();
                                if (tmp_pos[0] >= language_button[0] and tmp_pos[0] <= language_button[0] + 74
                                        and tmp_pos[1] >= language_button[1] and tmp_pos[1] <= language_button[1] + 35):
                                    draw_menu(lang=1)
                                else:
                                    draw_menu()
                                # pygame.display.flip()
                                pygame.event.pump()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        done = True
                                        # done = done or board.game_over()
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        tmp_pos = pygame.mouse.get_pos()
                                        if (tmp_pos[0] >= language_button[0] and tmp_pos[0] <= language_button[0] + 74
                                                and tmp_pos[1] >= language_button[1] and tmp_pos[1] <= language_button[1] + 35  ):
                                            animate_drop_down_button(clock)
                                            draw_menu(lang=2)
                                            temp_done = False
                                            while (not temp_done):
                                                pos = pygame.mouse.get_pos()

                                                # print( pos )
                                                if ((pos[0]>= 50 and pos[0] < 125) and (pos[1]>= 66 and pos[1] < 101)):
                                                    # draw_menu(lang=2)
                                                    if(design == "design_2/"):
                                                        screen.blit(pygame.transform.smoothscale(get_image(selection_flag_path),
                                                            (69, 32)), (53, 65))
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(get_flag_path(languages[0])), (38, 25)),
                                                                    (56, 68 + 0 * 35))

                                                        screen.blit(
                                                            pygame.transform.smoothscale(
                                                                get_image(selection_flag_path2_white),
                                                                (69, 32)), (53, 99))
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(get_flag_path(languages[1])), (38, 25)),
                                                            (56, 68 + 35))

                                                        pygame.display.flip()

                                                    elif (design == "design_1/"):
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(selection_flag_path),
                                                            (70, 35)), (52, 62))
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(get_flag_path(languages[0])), (38, 25)),
                                                            (56, 68 + 0 * 35))

                                                        screen.blit(
                                                            pygame.transform.smoothscale(
                                                                get_image(selection_flag_path2_white),
                                                                (69, 32)), (53, 100))
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(get_flag_path(languages[1])), (38, 25)),
                                                            (56, 68 + 35))

                                                        pygame.display.flip()

                                                elif ((pos[0] >= 50 and pos[0] < 125) and (pos[1] >= 102 and pos[1] < 137)):
                                                    # draw_menu(lang=2)

                                                    if (design == "design_2/"):
                                                        screen.blit(
                                                            pygame.transform.smoothscale(get_image(selection_flag_path_white),
                                                                                         (69, 32)), (53, 65))
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(get_flag_path(languages[0])), (38, 25)),
                                                            (56, 68 + 0 * 35))

                                                        screen.blit(
                                                            pygame.transform.smoothscale(get_image(selection_flag_path2),
                                                                                         (69, 33)), (53, 99))
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(get_flag_path(languages[1])), (38, 25)),
                                                            (56, 68 + 35))
                                                        pygame.display.flip()

                                                    elif (design == "design_1/"):
                                                        screen.blit(
                                                            pygame.transform.smoothscale(
                                                                get_image(selection_flag_path_white),
                                                                (70, 35)), (52, 62))
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(get_flag_path(languages[0])), (38, 25)),
                                                            (56, 68 + 0 * 35))

                                                        screen.blit(
                                                            pygame.transform.smoothscale(
                                                                get_image(selection_flag_path2),
                                                                (69, 32)), (53, 100))
                                                        screen.blit(pygame.transform.smoothscale(
                                                            get_image(get_flag_path(languages[1])), (38, 25)),
                                                            (56, 68 + 35))
                                                        pygame.display.flip()
                                                else:
                                                    draw_menu(lang=2)
                                                    # pass

                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        # temp_done = True
                                                        pygame.quit()
                                                        pass
                                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                                        pos = pygame.mouse.get_pos()
                                                        if (pos[0]>= 50 and pos[0] < 125) and (pos[1]>= 66 and pos[1] < 101):
                                                            dummy_language = languages[0]
                                                            change_language(dummy_language)
                                                            temp_done =True

                                                        elif (pos[0] >= 50 and pos[0] < 125) and (pos[1] >= 102 and pos[1] < 137):
                                                            dummy_language = languages[1]
                                                            change_language(dummy_language)
                                                            temp_done = True
                                                        else:
                                                        # elif (pos[0] >= language_button[0] and pos[0] <=
                                                        #         language_button[0] + 74
                                                        #         and pos[1] >= language_button[1] and pos[1]
                                                        #       <= language_button[1] + 35):
                                                            temp_done= True
                                                clock.tick(60)

                        elif (player == 21):
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos();
                                if (tmp_pos[0] >= help_button[0] and tmp_pos[0] <= help_button[0] + 350 and
                                        tmp_pos[1] >= help_button[1] and tmp_pos[1] <= help_button[1] + 69):
                                    draw_menu(help=1)
                                else:
                                    draw_menu()

                                pygame.display.flip()
                                pygame.event.pump()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        done = True
                                        # done = done or board.game_over()
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        tmp_pos = pygame.mouse.get_pos();
                                        if (tmp_pos[0] >= help_button[0] and tmp_pos[0] <= help_button[0] + 350 and
                                        tmp_pos[1] >= help_button[1] and tmp_pos[1] <= help_button[1] + 69):
                                            pass
                                clock.tick(40)













                                clock.tick(60)
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
                                                        while not event.type == pygame.MOUSEBUTTONUP:
                                                            screen.fill(WHITE)
                                                            tmp_pos = pygame.mouse.get_pos();
                                                            if (tmp_pos[0] >= 678 and tmp_pos[0] <=
                                                                    770 and
                                                                    tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                    572):
                                                                draw_gukenyura(default=1)
                                                            else:
                                                                draw_gukenyura()

                                                            pygame.display.flip()
                                                            pygame.event.pump()
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    pygame.quit()
                                                                    # done = done or board.game_over()
                                                                elif event.type == pygame.MOUSEBUTTONUP:
                                                                    tmp_pos = pygame.mouse.get_pos();
                                                                    if (tmp_pos[0] >= 678 and tmp_pos[0] <=
                                                                            770 and
                                                                            tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                            572):
                                                                        clicked = False
                                                                        board.default_player1()
                                                                        maximum = 0
                                                            clock.tick(60)
                                                        # clicked = False
                                                        # board.default_player1()
                                                        # maximum = 0

                                                    elif (data[1] == 18):

                                                        while not event.type == pygame.MOUSEBUTTONUP:
                                                            screen.fill(WHITE)
                                                            tmp_pos = pygame.mouse.get_pos();
                                                            if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                    122 and
                                                                    tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                    572):
                                                                draw_gukenyura(done=1)
                                                            else:
                                                                draw_gukenyura()

                                                            pygame.display.flip()
                                                            pygame.event.pump()
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    pygame.quit()
                                                                    # done = done or board.game_over()
                                                                elif event.type == pygame.MOUSEBUTTONUP:
                                                                    tmp_pos = pygame.mouse.get_pos();
                                                                    if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                            122 and
                                                                            tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                            572):
                                                                        change_state(1)
                                                                        print(online_helper.send_starting_setting(n, board.stringify()))
                                                                        board.default_player2()
                                                                        done_gukenyura = True

                                                            clock.tick(60)


                                                    elif(data[1] == 19 ):
                                                        while not event.type == pygame.MOUSEBUTTONUP:
                                                            screen.fill(WHITE)
                                                            tmp_pos = pygame.mouse.get_pos()
                                                            if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                    70 and
                                                                    tmp_pos[1] >= 30 and tmp_pos[1] <=
                                                                    70):
                                                                draw_gukenyura(menu=1)
                                                            else:
                                                                draw_gukenyura()

                                                            pygame.display.flip()
                                                            pygame.event.pump()
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    pygame.quit()
                                                                    # done = done or board.game_over()
                                                                elif event.type == pygame.MOUSEBUTTONUP:
                                                                    tmp_pos = pygame.mouse.get_pos();
                                                                    if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                    70 and
                                                                    tmp_pos[1] >= 30 and tmp_pos[1] <=
                                                                    70):
                                                                        change_state(0)
                                                                        done_gukenyura = True

                                                            clock.tick(60)


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
                                                        while not event.type == pygame.MOUSEBUTTONUP:
                                                            screen.fill(WHITE)
                                                            tmp_pos = pygame.mouse.get_pos();
                                                            if (tmp_pos[0] >= 678 and tmp_pos[0] <=
                                                                    770 and
                                                                    tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                    572):
                                                                draw_gukenyura(default=1)
                                                            else:
                                                                draw_gukenyura()

                                                            pygame.display.flip()
                                                            pygame.event.pump()
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    pygame.quit()
                                                                    # done = done or board.game_over()
                                                                elif event.type == pygame.MOUSEBUTTONUP:
                                                                    tmp_pos = pygame.mouse.get_pos();
                                                                    if (tmp_pos[0] >= 678 and tmp_pos[0] <=
                                                                    770 and
                                                                    tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                    572):
                                                                        clicked = False
                                                                        board.default_player1()
                                                                        maximum = 0
                                                            clock.tick(60)
                                                        # clicked = False
                                                        # board.default_player1()
                                                        # maximum = 0
                                                    elif (data[1] == 18):

                                                        while not event.type == pygame.MOUSEBUTTONUP:
                                                            screen.fill(WHITE)
                                                            tmp_pos = pygame.mouse.get_pos();
                                                            if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                    122 and
                                                                    tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                    572):
                                                                draw_gukenyura(done=1)
                                                            else:
                                                                draw_gukenyura()

                                                            pygame.display.flip()
                                                            pygame.event.pump()
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    pygame.quit()
                                                                    # done = done or board.game_over()
                                                                elif event.type == pygame.MOUSEBUTTONUP:
                                                                    tmp_pos = pygame.mouse.get_pos();
                                                                    if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                            122 and
                                                                            tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                            572):
                                                                        change_state(1)
                                                                        print(online_helper.send_starting_setting(n,board.stringify()))
                                                                        board.default_player2()
                                                                        done_gukenyura = True

                                                            clock.tick(60)

                                                    elif(data[1] == 19):
                                                        while not event.type == pygame.MOUSEBUTTONUP:
                                                            screen.fill(WHITE)
                                                            tmp_pos = pygame.mouse.get_pos()
                                                            if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                    70 and
                                                                    tmp_pos[1] >= 30 and tmp_pos[1] <=
                                                                    70):
                                                                draw_gukenyura(menu=1)
                                                            else:
                                                                draw_gukenyura()

                                                            pygame.display.flip()
                                                            pygame.event.pump()
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    pygame.quit()
                                                                    # done = done or board.game_over()
                                                                elif event.type == pygame.MOUSEBUTTONUP:
                                                                    tmp_pos = pygame.mouse.get_pos();
                                                                    if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                    70 and
                                                                    tmp_pos[1] >= 30 and tmp_pos[1] <=
                                                                    70):
                                                                        change_state(0)
                                                                        done_gukenyura = True

                                                            clock.tick(60)

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

                                    clock.tick(30)
                            elif(data[1] == 17):
                                while not event.type == pygame.MOUSEBUTTONUP:
                                    screen.fill(WHITE)
                                    tmp_pos = pygame.mouse.get_pos();
                                    if (tmp_pos[0] >= 678 and tmp_pos[0] <=
                                            770 and
                                            tmp_pos[1] >= 520 and tmp_pos[1] <=
                                            572):
                                        draw_gukenyura(default=1)
                                    else:
                                        draw_gukenyura()

                                    pygame.display.flip()
                                    pygame.event.pump()
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit
                                            # done = done or board.game_over()
                                        elif event.type == pygame.MOUSEBUTTONUP:
                                            tmp_pos = pygame.mouse.get_pos();
                                            if (tmp_pos[0] >= 678 and tmp_pos[0] <=
                                                    770 and
                                                    tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                    572):
                                                clicked_default = True
                                                board.default_player1()
                                                # maximum = 0
                                    clock.tick(60)
                                # clicked_default = True
                                # board.default_player1()

                            elif (data[1] == 18):
                                while not event.type == pygame.MOUSEBUTTONUP:
                                    screen.fill(WHITE)
                                    tmp_pos = pygame.mouse.get_pos();
                                    if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                            122 and
                                            tmp_pos[1] >= 520 and tmp_pos[1] <=
                                            572):
                                        draw_gukenyura(done =1)
                                    else:
                                        draw_gukenyura()

                                    pygame.display.flip()
                                    pygame.event.pump()
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            # done = done or board.game_over()
                                        elif event.type == pygame.MOUSEBUTTONUP:
                                            tmp_pos = pygame.mouse.get_pos();
                                            if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                    122 and
                                                    tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                    572):
                                                change_state(1)
                                                print(online_helper.send_starting_setting(n, board.stringify()))
                                                board.default_player2()
                                                done_gukenyura = True

                                    clock.tick(60)

                            elif(data[1] == 19):
                                while not event.type == pygame.MOUSEBUTTONUP:
                                    screen.fill(WHITE)
                                    tmp_pos = pygame.mouse.get_pos()
                                    if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                            70 and
                                            tmp_pos[1] >= 30 and tmp_pos[1] <=
                                            70):
                                        draw_gukenyura(menu=1)
                                    else:
                                        draw_gukenyura()

                                    pygame.display.flip()
                                    pygame.event.pump()
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            # done = done or board.game_over()
                                        elif event.type == pygame.MOUSEBUTTONUP:
                                            tmp_pos = pygame.mouse.get_pos();
                                            if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                    70 and
                                                    tmp_pos[1] >= 30 and tmp_pos[1] <=
                                                    70):
                                                change_state(0)
                                                done_gukenyura = True

                                    clock.tick(60)



        clock.tick(60)
    pygame.quit()
    # pygame.quit()
    print ("fin")
    print (board.BOARD)
if __name__ == '__main__':
    main()
