from src import board
import numpy as np
import pygame
import os
import time
from ai import artificial_intelligence
from network.network import Network
from network import online_helper

######################
# Define some colors #
######################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

##########################
# Sizes and measurements #
##########################

BEAD = 5
BETWEEN_SLOTS = 5
SLOTS = 40
BOARD_WIDTH = BETWEEN_SLOTS*6+ SLOTS*2 * 4
BOARD_LENGTH = BETWEEN_SLOTS*9+ SLOTS*2 * 8


#######################
# Buttons coordinates #
#######################

back_button = [0,0]
gukenyura_button=[0,0]
start_button=[0,0]
help_button =[0,0]
language_button=[0,0]
language_button_choice_1=[0,0]
language_button_choice_2=[0,0]
vs_computer_button = [0,0]
slider_button = [0,0]


##########
# States #
##########

done = False
Current_state = 0 #menu = 0, game = 1, gameover=2, gukenyura = 3, waiting from menu = 5, waiting from set board = 6
GUKENYURA = 3
MENU = 0
REPLAY = 2
PLAY = 1
HELP = 4
WAITING_FROM_MENU = 5
WAITING_FROM_SET_BOARD = 6

_image_library = {}


config_language = "fr"
languages = ["bi", "en"]
# design = "design_1/"
design = "design_2/"
design_2 = True
# design_2 = False

DATABASE = []

def change_design():
    global design, config_language, dukenyure_button_clicked_path, dukenyure_button_unclicked_path, dukine_button_clicked_path, \
        dukine_button_unclicked_path, ingeneBakina_button_unclicked_path, ingeneBakina_button_clicked_path,\
        default_clicked_path,default_unclicked_path,back_button_unclicked_path,back_button_clicked_path,player1_banner_path,player2_banner_path,\
        selection_flag_path, selection_flag_path_white, selection_flag_path2, selection_flag_path2_white, background_click_path,\
        language_drop_down_button_clicked_path, language_drop_down_button_unclicked_path, language_drop_down_path,waiting_for_player1_banner_path,\
        waiting_for_player2_banner_path,hider_pannel_path,done_path,done_unclicked_path,done_clicked_path,player2_path,\
        menu_gukenyura_button_unclicked_path,menu_gukenyura_button_clicked_path,vs_cpu_button_clicked_path,vs_cpu_button_unclicked_path

    if design == "design_1/":
        design ="design_2/"

    else:
        design = "design_1/"

    waiting_for_player1_banner_path = "assets/buttons/" + design + config_language + "/waiting_for_player1_banner.png"
    waiting_for_player2_banner_path = "assets/buttons/" + design + config_language + "/waiting_for_player2_banner.png"

    ####################
    # play state assets#
    ####################

    player1_banner_path = "assets/buttons/" + design + config_language + "/player1_banner.png"
    player2_banner_path = "assets/buttons/" + design + config_language + "/player2_banner.png"
    back_button_clicked_path = "assets/buttons/" + design + config_language + "/back_button_clicked.png"
    back_button_unclicked_path = "assets/buttons/" + design + config_language + "/back_button_unclicked.png"
    hider_pannel_path = "assets/buttons/" + design + "/hider_white.png"



    ###################
    ###################

    done_path = "assets/buttons/" + design + "/done_button_unclicked.png"
    done_unclicked_path = "assets/buttons/" + design + "/done_button_unclicked.png"
    done_clicked_path = "assets/buttons/" + design + "/done_button_clicked.png"
    default_unclicked_path = "assets/buttons/" + design + config_language + "/default_button_unclicked.png"
    default_clicked_path = "assets/buttons/" + design + config_language + "/default_button_clicked.png"
    menu_gukenyura_button_unclicked_path = "assets/buttons/" + design + "/menu_gukenyura_button_unclicked.png"
    menu_gukenyura_button_clicked_path = "assets/buttons/" + design + "/menu_gukenyura_button_clicked.png"

    ####################
    # Menu State assets#
    ####################

    dukenyure_button_unclicked_path = "assets/buttons/" + design + config_language + "/dukenyure_button_unclicked.png"
    dukenyure_button_clicked_path = "assets/buttons/" + design + config_language + "/dukenyure_button_clicked.png"
    dukine_button_unclicked_path = "assets/buttons/" + design + config_language + "/dukine_button_unclicked.png"
    dukine_button_clicked_path = "assets/buttons/" + design + config_language + "/dukine_button_clicked.png"
    ingeneBakina_button_unclicked_path = "assets/buttons/" + design + config_language + "/ingeneBakina_button_uncliked.png"
    ingeneBakina_button_clicked_path = "assets/buttons/" + design + config_language + "/ingeneBakina_button_cliked.png"
    vs_cpu_button_clicked_path = "assets/buttons/" + design + config_language + "/kinanIMachine_button_clicked.png"
    vs_cpu_button_unclicked_path = "assets/buttons/" + design + config_language + "/kinanIMachine_button_unclicked.png"

    selection_flag_path = "assets/buttons/" + design + "selection_of_flag.png"
    selection_flag_path_white = "assets/buttons/" + design + "selection_of_flag_white.png"
    selection_flag_path2 = "assets/buttons/" + design + "selection_of_flag2.png"
    selection_flag_path2_white = "assets/buttons/" + design + "selection_of_flag2_white.png"
    background_click_path = "assets/buttons/background_click.png"

    language_drop_down_button_clicked_path = "assets/buttons/" + design + "language_drop_down_menu_clicked.png"
    language_drop_down_button_unclicked_path = "assets/buttons/" + design + "language_drop_down_menu_unclicked.png"
    language_drop_down_path = "assets/buttons/" + design + "language_drop_down.png"












#######################
# Online gaming assets#
#######################

# online_game = True
online_game = False
online_player_id = 0

waiting_for_player1_banner_path = "assets/buttons/"+design+config_language+"/waiting_for_player1_banner.png"
waiting_for_player2_banner_path = "assets/buttons/"+design+config_language+"/waiting_for_player2_banner.png"


######################
# Vs Computer assets #
######################

# vs_computer = True
vs_computer = False


####################
# play state assets#
####################

player1_banner_path = "assets/buttons/"+design+config_language+"/player1_banner.png"
player2_banner_path = "assets/buttons/"+design+config_language+"/player2_banner.png"
back_button_clicked_path = "assets/buttons/"+design+config_language+"/back_button_clicked.png"
back_button_unclicked_path = "assets/buttons/"+design+config_language+"/back_button_unclicked.png"
hider_pannel_path = "assets/buttons/"+design+"/hider_white.png"


###################
# game-over assets#
###################

menu_path = "assets/buttons/menu_button.png"
restart_path = "assets/buttons/restart_button.png"

###################
###################

done_path = "assets/buttons/"+design+"/done_button_unclicked.png"
done_unclicked_path = "assets/buttons/"+design+"/done_button_unclicked.png"
done_clicked_path = "assets/buttons/"+design+"/done_button_clicked.png"
default_path="assets/buttons/"+design+"/bi/default_button_unclicked.png"
default_unclicked_path = "assets/buttons/"+design+config_language+"/default_button_unclicked.png"
default_clicked_path = "assets/buttons/"+design+config_language+"/default_button_clicked.png"
menu_gukenyura_button_unclicked_path = "assets/buttons/"+design+"/menu_gukenyura_button_unclicked.png"
menu_gukenyura_button_clicked_path = "assets/buttons/"+design+"/menu_gukenyura_button_clicked.png"


####################
# Menu State assets#
####################


dukenyure_button_unclicked_path = "assets/buttons/"+design+config_language+"/dukenyure_button_unclicked.png"
dukenyure_button_clicked_path = "assets/buttons/"+design+config_language+"/dukenyure_button_clicked.png"
# dukenyure_button_clicked_path = "assets/buttons/"+design+config_language+"/dukenyure_button_clicked.png"
dukine_button_unclicked_path = "assets/buttons/"+design+config_language+"/dukine_button_unclicked.png"
dukine_button_clicked_path = "assets/buttons/"+design+config_language+"/dukine_button_clicked.png"
ingeneBakina_button_unclicked_path = "assets/buttons/"+design+config_language+"/ingeneBakina_button_uncliked.png"
ingeneBakina_button_clicked_path = "assets/buttons/"+design+config_language+"/ingeneBakina_button_cliked.png"
vs_cpu_button_clicked_path="assets/buttons/"+design+config_language+"/kinanIMachine_button_clicked.png"
vs_cpu_button_unclicked_path="assets/buttons/"+design+config_language+"/kinanIMachine_button_unclicked.png"
slider_activated_path = "assets/buttons/slider_activated.png"
circle_activated_path = "assets/buttons/slide_circle_right.png"
slider_deactivated_path = "assets/buttons/slider_deactivated.png"
circle_deactivated_path = "assets/buttons/slide_circle_left.png"

##################
# language assets#
##################

bi_flag_path = "assets/buttons/flag_bi.png"
fr_flag_path = "assets/buttons/flag_fr.png"
en_flag_path = "assets/buttons/flag_en.png"

def get_flag_path(flag):
    if(flag == "bi" ):
        return bi_flag_path
    elif(flag == "fr"):
        return fr_flag_path
    else:
        return en_flag_path

language_drop_down_button_clicked_path = "assets/buttons/"+design+"language_drop_down_menu_clicked.png"
language_drop_down_button_unclicked_path = "assets/buttons/"+design+"language_drop_down_menu_unclicked.png"
language_drop_down_path = "assets/buttons/"+design+"language_drop_down.png"

def animate_slider(clock):
    time = 0
    destination = 0

    vitesse = 0.5
    acceleration = 0.04

    if vs_computer:

        while(destination < 21):
            screen.blit(pygame.transform.smoothscale(get_image(hider_pannel_path), (50, 30)), (375, 30))
            screen.blit(pygame.transform.smoothscale(get_image(slider_activated_path), (50, 20)), (375, 35))
            destination = int(-0.5 * acceleration * time * time) + int(vitesse * time) + destination
            screen.blit(pygame.transform.smoothscale(get_image(circle_activated_path), (30, 30)), (395 - destination, 30))

            pygame.display.flip()
            clock.tick(60)
            time += 1

    else:
        while (destination < 21):
            screen.blit(pygame.transform.smoothscale(get_image(hider_pannel_path), (50, 30)), (375, 30))
            screen.blit(pygame.transform.smoothscale(get_image(slider_deactivated_path), (50, 20)), (375, 35))
            destination = int(-0.5 * acceleration * time * time) + (vitesse * time) + destination
            screen.blit(pygame.transform.smoothscale(get_image(circle_deactivated_path), (30, 30)),
                        (375 + destination, 30))

            pygame.display.flip()
            clock.tick(60)
            time += 1


def animate_drop_down_button(clock):
    time = 0
    destination = 0


    # vitesse = 3
    vitesse = 0.9
    # acceleration = 0.528
    acceleration = 0.08
    # acceleration = 0.0
    screen.blit(get_image(background_click_path), (0, 0))
    while (not destination >= 70):

        destination = int(-0.5 * acceleration * time * time) + int(vitesse * time) + destination
        screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_path),
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

        path = "assets/buttons/design_2/masquer scroll down.png"
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


selection_flag_path = "assets/buttons/"+design+"selection_of_flag.png"
selection_flag_path_white = "assets/buttons/"+design+"selection_of_flag_white.png"
selection_flag_path2 = "assets/buttons/"+design+"selection_of_flag2.png"
selection_flag_path2_white = "assets/buttons/"+design+"selection_of_flag2_white.png"
background_click_path = "assets/buttons/background_click.png"


def getpath(beads):
    result ="assets/beads_pictures/"+str(beads)+"_beads.png"
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



pygame.init()

# Set the width and height of the screen [width, height]
size = (800,600)
screen = pygame.display.set_mode(size)
circle_filled = pygame.Surface(size)
place =[int((800-BOARD_LENGTH) / 2 ), int((600 - BOARD_WIDTH) / 2), BOARD_LENGTH, BOARD_WIDTH]

def change_language(language):
    global config_language, dukenyure_button_clicked_path, dukenyure_button_unclicked_path, dukine_button_clicked_path, \
        dukine_button_unclicked_path, ingeneBakina_button_unclicked_path, ingeneBakina_button_clicked_path,\
        default_clicked_path,default_unclicked_path,back_button_unclicked_path,back_button_clicked_path,player1_banner_path,player2_banner_path\
        ,vs_cpu_button_clicked_path,vs_cpu_button_unclicked_path
    if language == languages[0]:
        languages[0] = config_language
        config_language = language
    else:
        languages[1] = config_language
        config_language = language

    dukenyure_button_unclicked_path = "assets/buttons/"+design+"/"+ language +"/dukenyure_button_unclicked.png"
    dukenyure_button_clicked_path="assets/buttons/"+design+"/"+ language +"/dukenyure_button_clicked.png"
    dukine_button_unclicked_path="assets/buttons/"+design+"/"+ language +"/dukine_button_unclicked.png"
    dukine_button_clicked_path = "assets/buttons/"+design+"/"+ language +"/dukine_button_clicked.png"
    ingeneBakina_button_clicked_path="assets/buttons/"+design+"/"+ language +"/ingeneBakina_button_cliked.png"
    ingeneBakina_button_unclicked_path="assets/buttons/"+design+"/"+ language +"/ingeneBakina_button_uncliked.png"
    default_clicked_path = "assets/buttons/"+design+"/"+ language +"/default_button_clicked.png"
    default_unclicked_path = "assets/buttons/"+design+"/"+ language +"/default_button_unclicked.png"
    back_button_unclicked_path = "assets/buttons/"+design+"/"+ language +"/back_button_unclicked.png"
    back_button_clicked_path = "assets/buttons/"+design+"/"+ language +"/back_button_clicked.png"
    player1_banner_path="assets/buttons/"+design+"/"+ language +"/player1_banner.png"
    player2_banner_path="assets/buttons/"+design+"/"+ language +"/player2_banner.png"
    vs_cpu_button_clicked_path = "assets/buttons/" + design + config_language + "/kinanIMachine_button_clicked.png"
    vs_cpu_button_unclicked_path = "assets/buttons/" + design + config_language + "/kinanIMachine_button_unclicked.png"


def change_state(state):
    global Current_state
    Current_state = state

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
    myfont = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 11)
    for line in range (len(board.BOARD)):
        for row in range (len(board.BOARD[0])):
            # circle_filled=pygame.Surface(size)
            pygame.draw.circle(screen, GREY, board_coordinates_to_screen_coordinates(line, row), SLOTS - 5)
            pygame.draw.circle(screen, WHITE, board_coordinates_to_screen_coordinates(line, row), SLOTS - 2, 1)# à revoir
            # font_obj = pygame.font.SysFont('FreeSans.ttf', 15)
            font_obj = myfont
            text_surface_obj = font_obj.render(" " + str(board.BOARD[line][row]), False, BLACK, GREY)
            text_rect_obj = text_surface_obj.get_rect()
            x = board_coordinates_to_screen_coordinates(line, row)[0] + 38
            y=board_coordinates_to_screen_coordinates(line, row)[1] - 30
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


def draw_gukenyura(default = None, done = None, menu = None, waiting = None):
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, place)
    draw_frame()
    draw_slots()

    if (default):
        draw_gukenyura_buttons(default=1)
    elif (done):
        draw_gukenyura_buttons(done=1)
    elif (menu):
        draw_gukenyura_buttons(menu=1)
    else:
        draw_gukenyura_buttons()

    if (waiting):
        screen.blit(get_image(background_click_path), (0, 0))
        global online_player_id
        if (online_player_id == 2):
            screen.blit(get_image(waiting_for_player1_banner_path), (65, 223))
        else:
            screen.blit( get_image(waiting_for_player2_banner_path), (65, 223))
        pygame.display.flip()


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
            font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 8)
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

        font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 10)
        text_surface_obj = font_obj.render(" " + " CLEAR   BEADS ", True, BLACK, GREY)
        text_rect_obj.center = (tmp_position[0] + 22, tmp_position[1] + 16 * 11 + 4)
        screen.blit(text_surface_obj, text_rect_obj)

        pygame.display.flip()
    else:
        screen.fill(WHITE)
        draw_gukenyura_buttons()
        pygame.draw.rect(screen, BLACK, place)
        draw_frame()
        draw_slots()
        pygame.display.flip()



def draw_menu(vs_cpu = None,play = None, set = None, lang = None, help = None, waiting = None):
    global gukenyura_button, start_button,vs_computer_button,help_button, language_button, online_player_id,slider_button

    if( not design_2): #if design_2 is False, the menu will use a normal button for v-s computer
        screen.fill(WHITE)

        if (vs_cpu):
            screen.blit(pygame.transform.smoothscale(get_image(vs_cpu_button_clicked_path), (350, 69)), (225, 155))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(vs_cpu_button_unclicked_path), (350, 69)), (225, 155))
        vs_computer_button = [225, 155]

        if(play):
            screen.blit(pygame.transform.smoothscale(get_image(dukine_button_clicked_path), (350,69)), (225, 235))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(dukine_button_unclicked_path), (350,69)), (225, 235))
        start_button = [225,235]

        if(set):
            screen.blit(pygame.transform.smoothscale(get_image(dukenyure_button_clicked_path), (350,69)), (225, 315))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(dukenyure_button_unclicked_path), (350, 69)), (225, 315))
        gukenyura_button = [225, 315]

        if(help):
            screen.blit(pygame.transform.smoothscale(get_image(ingeneBakina_button_clicked_path),(350,69)), (225, 395))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(ingeneBakina_button_unclicked_path), (350, 69)), (225, 395))
        global help_button
        help_button = [225, 395]

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

        language_button = [50, 30]
        screen.blit(pygame.transform.smoothscale(get_image(get_flag_path(config_language)), (38,25)), (56,35))
        # pygame.transform.smoothscale(get_image(getpath(self.intoke)), (105, 161))

        if (waiting):
            screen.blit(get_image(background_click_path), (0, 0))
            # print(online_player_id)
            if (online_player_id == 2):
                # print("waiting for player 1")
                # screen.blit(pygame.transform.smoothscale(get_image(waiting_for_player1_banner_path), (310, 63)), (447, 485))
                screen.blit(get_image(waiting_for_player1_banner_path), (65, 223))
            else:
                # print("waiting for player 2")
                # screen.blit(pygame.transform.smoothscale(get_image(waiting_for_player2_banner_path), (310, 63)), (47, 55))
                screen.blit( get_image(waiting_for_player2_banner_path), (65, 223))
            pygame.display.flip()

    else:  #if design_2 is True, the menu will use a sliding button for v-s computer.
        screen.fill(WHITE)
        font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 14)
        text_surface_obj = font_obj.render(" " + " PvP ", True, BLACK, WHITE)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (290 , 45)
        screen.blit(text_surface_obj, text_rect_obj)

        text_surface_obj = font_obj.render(" " + " PvCPU ", True, BLACK, WHITE)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (500, 45)
        screen.blit(text_surface_obj, text_rect_obj)
        if (vs_computer):
            screen.blit(pygame.transform.smoothscale(get_image(slider_activated_path), (50, 20)), (375,35))
            screen.blit(pygame.transform.smoothscale(get_image(circle_activated_path), (30, 30)), (395, 30))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(slider_deactivated_path), (50, 20)), (375,35))
            screen.blit(pygame.transform.smoothscale(get_image(circle_deactivated_path), (30, 30)), (375, 30))
        slider_button = [375, 30]

        if (play):
            screen.blit(pygame.transform.smoothscale(get_image(dukine_button_clicked_path), (350, 69)), (225, 185))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(dukine_button_unclicked_path), (350, 69)), (225, 185))
        start_button = [225, 185]

        if (set):
            screen.blit(pygame.transform.smoothscale(get_image(dukenyure_button_clicked_path), (350, 69)), (225, 265))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(dukenyure_button_unclicked_path), (350, 69)), (225, 265))
        gukenyura_button = [225, 265]

        if (help):
            screen.blit(pygame.transform.smoothscale(get_image(ingeneBakina_button_clicked_path), (350, 69)),
                        (225, 345))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(ingeneBakina_button_unclicked_path), (350, 69)),
                        (225, 345))
        help_button = [225, 345]

        if (lang == 2):
            screen.blit(get_image(background_click_path), (0, 0))
            screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_path), (75, 105)), (50, 30))
            screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_button_clicked_path), (75, 35)),
                        (50, 30))

            for i in range(2):
                if (not languages[i] == config_language):
                    screen.blit(pygame.transform.smoothscale(get_image(get_flag_path(languages[i])), (38, 25)),
                                (56, 68 + i * 35))
        elif (lang == 1):
            screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_button_clicked_path), (75, 35)),
                        (50, 30))
        else:
            screen.blit(pygame.transform.smoothscale(get_image(language_drop_down_button_unclicked_path), (75, 35)),
                        (50, 30))

        language_button = [50, 30]
        screen.blit(pygame.transform.smoothscale(get_image(get_flag_path(config_language)), (38, 25)), (56, 35))
        # pygame.transform.smoothscale(get_image(getpath(self.intoke)), (105, 161))

        if (waiting):
            screen.blit(get_image(background_click_path), (0, 0))

            # print(online_player_id)
            if (online_player_id == 2):
                # print("waiting for player 1")
                # screen.blit(pygame.transform.smoothscale(get_image(waiting_for_player1_banner_path), (310, 63)), (447, 485))
                screen.blit(get_image(waiting_for_player1_banner_path), (65, 223))
            else:
                # print("waiting for player 2")
                # screen.blit(pygame.transform.smoothscale(get_image(waiting_for_player2_banner_path), (310, 63)), (47, 55))
                screen.blit(get_image(waiting_for_player2_banner_path), (65, 223))
            pygame.display.flip()



    pygame.display.flip()


def game_coordinates_to_data(x, y):
    result =[0,0]
    if(Current_state == MENU):
        if (x >= start_button[0] and x <= start_button[0] + 350 and y >= start_button[1] and y <= start_button[1] + 69  ):
            return [4,0]
        elif (x >= gukenyura_button[0] and x <= gukenyura_button[0] + 350 and y >= gukenyura_button[1] and y <= gukenyura_button[1] + 69  ):
            return [5,0]

        elif (x >= language_button[0] and x <= language_button[0] + 74 and y >= language_button[1] and y <= language_button[1] + 35  ):
            return [20,0]
        # (74, 35)
        elif (x >= help_button[0] and x <= help_button[0] + 350 and y >= help_button[1] and y <= help_button[1] + 69  ):
            return [21,0]
        elif (x >= vs_computer_button[0] and x <= vs_computer_button[0] + 350 and y >= vs_computer_button[1] and y <=
              vs_computer_button[1] + 69):
            if(not design_2):
                return [22,0]
            else:
                return [0,0]
        elif (x >= slider_button[0] and x <= slider_button[0] + 50 and y >= slider_button[1] and y <=
              slider_button[1] + 30):
            if ( design_2):
                return [23, 0]
            else:
                return [0, 0]


        else:
            return[0,0]

    elif(Current_state == GUKENYURA):
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
    elif(Current_state == REPLAY):
        if(y > 210 and y <= 390 and x > 150 and x <= 350):
            return[6,0]
        elif(y > 210 and y <= 390 and x > 460 and x <= 640):
            return [7,0]
        else : return[0,0]
    elif(Current_state == PLAY):
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
            board.add_bead(remainder)
            draw()
            temp_hole = (remainder )
            # print(BOARD)

            # gui.draw_frame()
        if(temp_hole>8):
            result2 = board.hole_correspondance(temp_hole)
            row2_crsp = result2[1]
            row1_crsp = result2[0]

            if(board.player_one) :
                board.player(2)
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
                    board.take_beads(row1_crsp, beads_row1)
                    draw()
                if (not board.beads(row2_crsp) == 0):
                    time.sleep(0.5)
                    board.take_beads(row2_crsp, beads_row2)
                    draw()

                if (not board.player_one):
                    board.player(1)
                else:
                    board.player(2)
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



def waiting_banner():
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()

    if (board.current_player == 2):
        print("waiting for player 1" )
        screen.blit(pygame.transform.smoothscale(get_image(waiting_for_player1_banner_path), (310, 63)), (447, 485))
    else :
        print("waiting for player 2")
        screen.blit(pygame.transform.smoothscale(get_image(waiting_for_player2_banner_path), (310, 63)), (47, 55))
    pygame.display.flip()




pygame.display.set_caption("URUBUGU")
pygame.display.set_icon(get_image("assets/game.png"))










def main():

    global done, online_player_id,design,vs_computer, design_2
    clock = pygame.time.Clock()


    if online_game:
        n = Network()
        online_player_id = n.player_number

        ######Preparing the online game###############

        if (online_player_id):
            online_player_id = int (online_player_id[-1])
            # board.player(int(online_player_id))
            print("online player_id =" + str (online_player_id))
            pygame.display.set_caption("URUBUGU + player" +str(online_player_id) )















    # -------- Main Program Loop -----------
    clicked_default = False
    while ( (not done)):

        if(Current_state == PLAY):
            draw()
            if (online_game):
                if board.current_player == 2:
                    result = online_helper.decode_reply(online_helper.get_other_player_move(n))
                    if result == "waiting":
                        print(result)
                    else:
                        play(int(result))
                        board.player(1)
                        board.current_player = 1
                        if (board.game_over()):
                            time.sleep(0.5)
                            change_state(REPLAY)
            if (vs_computer and not board.game_over()):
                time.sleep(0.5)
                hole_to_play = artificial_intelligence.hole_to_play_medium()
                beads = board.beads(hole_to_play)
                if (not board.player_one and (not beads == 0)):
                    play(hole_to_play)
                    board.player(1)
                    board.current_player = 1
                    if (board.game_over()):
                        time.sleep(0.5)
                        change_state(2)
                else:
                    # something to prevent the other player to play
                    pass
        elif(Current_state == MENU):
            if(not design_2 and vs_computer):
                vs_computer = False
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
                elif (x >= vs_computer_button[0] and x <=vs_computer_button[0] + 350 and y >= vs_computer_button[1] and y <=
                  vs_computer_button[1] + 69):
                    draw_menu(vs_cpu=1)
                else:
                    draw_menu()
            else:
                draw_menu()
        elif(Current_state == GUKENYURA) :
            if(clicked_default == False):
                board.choose_board(board.BOARD_gukenyura)
            draw_gukenyura()
            # clicked_default = False
        elif(Current_state == WAITING_FROM_MENU):
            draw_menu(waiting = 1)
            reply = online_helper.decode_reply(online_helper.get_starting_setting(n))
            if (not reply == "waiting"):
                result2 = online_helper.string_to_list(reply)
                board.player(2)
                for i in range(len(result2)):
                    board.add_beads(i + 1, result2[i])
                if online_player_id == 1:
                    board.player(1)
                    board.current_player = 1
                else:
                    board.player(2)
                    board.current_player = 2
                change_state(PLAY)

        elif(Current_state == WAITING_FROM_SET_BOARD):
            draw_gukenyura(waiting=1)
            reply = online_helper.decode_reply(online_helper.get_starting_setting(n))
            if (not reply == "waiting"):
                result2 = online_helper.string_to_list(reply)
                board.player(2)
                for i in range(len(result2)):
                    board.add_beads(i + 1, result2[i])
                if online_player_id == 1:
                    board.player(1)
                    board.current_player = 1
                else:
                    board.player(2)
                    board.current_player = 2
                change_state(PLAY)

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
                    data = game_coordinates_to_data(position[0], int(position[1]))
                    print(data)
                    if(not data[0] == 0):
                        clicked_button = data[0]
                        # player = board.current_player
                        hole = data[1]

                        if (clicked_button == 1):
                            beads = board.beads(hole)
                            if(board.player_one and(not beads == 0)):
                                if (online_game):
                                    print(online_helper.send_my_move(n, str(hole)))
                                play(hole)
                                board.player(2)
                                board.current_player = 2
                                if(board.game_over()):
                                    time.sleep(0.5)
                                    change_state(REPLAY)
                            else:
                                # something to prevent the other player to play
                                pass


                        elif(clicked_button == 2 and (not vs_computer) and (not online_game)):
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
                        elif(clicked_button == 3): # play state back button clicked
                            while not event.type == pygame.MOUSEBUTTONUP:
                                tmp_pos = pygame.mouse.get_pos()
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
                                            # board.back(board.back_Board)
                                            change_state(MENU)


                        elif(clicked_button == 4): # menu state click on Dukine (Play) button
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos()
                                if (tmp_pos[0] >= start_button[0] and tmp_pos[0] <= start_button[0] + 350 and
                                        tmp_pos[1] >= start_button[1] and tmp_pos[1] <= start_button[1] + 69):
                                    draw_menu(play=1)
                                else:
                                    draw_menu()

                                pygame.display.flip()
                                pygame.event.pump()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        # done = done or board.game_over()
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        tmp_pos = pygame.mouse.get_pos()
                                        if (tmp_pos[0] >= start_button[0] and tmp_pos[0] <= start_button[0] + 350 and tmp_pos[1] >= start_button[
                                            1] and tmp_pos[1] <= start_button[1] + 69):
                                            board.choose_board(board.BOARD_DEFAULT_P1)
                                            if online_game:
                                                print(online_helper.send_starting_setting(n, board.stringify()))
                                                reply = online_helper.decode_reply(
                                                    online_helper.get_starting_setting(n))
                                                print(reply)
                                                if (reply == "waiting"):
                                                    change_state(WAITING_FROM_MENU)
                                                    # draw_menu(waiting=1)
                                                    # reply = online_helper.decode_reply(
                                                    #     online_helper.get_starting_setting(n))


                                                else:
                                                    result2 = online_helper.string_to_list(reply)
                                                    board.player(2)
                                                    for i in range (len (result2)):
                                                        board.add_beads(i + 1, result2[i])
                                                    if online_player_id == 1:
                                                        board.player(1)
                                                        board.current_player = 1
                                                    else:
                                                        board.player(2)
                                                        board.current_player = 2
                                                    change_state(PLAY)

                                            else:
                                                board.choose_board(board.BOARD_DEFAULT)
                                                change_state(PLAY)
                                clock.tick(60)

                        elif(clicked_button == 5):#menu state click on dukenyure (setting up board) button
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos()
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
                                        tmp_pos = pygame.mouse.get_pos()
                                        if (tmp_pos[0] >= gukenyura_button[0] and tmp_pos[0] <= gukenyura_button[0] + 350 and
                                                tmp_pos[1] >= gukenyura_button[1] and tmp_pos[1] <= gukenyura_button[1] + 69):
                                            change_state(3)
                                            board.player(1)
                                            draw_gukenyura_buttons()
                                clock.tick(40)

                        elif (clicked_button == 20): #Menu state language menu drop down clicked
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos()
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

                        elif (clicked_button == 21):
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos()
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
                                        tmp_pos = pygame.mouse.get_pos()
                                        if (tmp_pos[0] >= help_button[0] and tmp_pos[0] <= help_button[0] + 350 and
                                        tmp_pos[1] >= help_button[1] and tmp_pos[1] <= help_button[1] + 69):
                                            pass

                                clock.tick(40)
                        elif (clicked_button == 22):
                            while not event.type == pygame.MOUSEBUTTONUP:
                                screen.fill(WHITE)
                                tmp_pos = pygame.mouse.get_pos()
                                if (tmp_pos[0] >= vs_computer_button[0] and tmp_pos[0] <= vs_computer_button[0] + 350 and
                                        tmp_pos[1] >= vs_computer_button[1] and tmp_pos[1] <= vs_computer_button[1] + 69):
                                    draw_menu(vs_cpu=1)
                                else:
                                    draw_menu()

                                pygame.display.flip()
                                pygame.event.pump()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        done = True
                                        # done = done or board.game_over()
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        tmp_pos = pygame.mouse.get_pos()
                                        if (tmp_pos[0] >= vs_computer_button[0] and tmp_pos[0] <= vs_computer_button[0] + 350 and
                                        tmp_pos[1] >= vs_computer_button[1] and tmp_pos[1] <= vs_computer_button[1] + 69):
                                            vs_computer = True
                                            board.choose_board(board.BOARD_DEFAULT)
                                            change_state(1)
                                            # pass

                                clock.tick(40)
                            clock.tick(60)
                        elif(clicked_button == 23):
                            animate_slider(clock)
                            vs_computer = not vs_computer
                            print(vs_computer)


                        elif (clicked_button == 6):
                            change_state(0)
                        elif (clicked_button == 7):
                            change_state(1)
                            board.BOARD = np.copy(board.BOARD_DEFAULT)

                        elif (clicked_button == 8):
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
                                    tmp_data = game_coordinates_to_data(tmp_position[0],
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
                                                    data = game_coordinates_to_data(position[0], int(position[1]))
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
                                                            tmp_pos = pygame.mouse.get_pos()
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
                                                                    tmp_pos = pygame.mouse.get_pos()
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
                                                            tmp_pos = pygame.mouse.get_pos()
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
                                                                    tmp_pos = pygame.mouse.get_pos()
                                                                    if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                            122 and
                                                                            tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                                            572):

                                                                        if online_game: #online game handler

                                                                            print(online_helper.send_starting_setting(n, board.stringify()))
                                                                            reply = online_helper.decode_reply(
                                                                                online_helper.get_starting_setting(n))
                                                                            print(reply)
                                                                            if (reply == "waiting"):
                                                                                change_state(WAITING_FROM_SET_BOARD)
                                                                            else:
                                                                                result2 = online_helper.string_to_list(
                                                                                    reply)
                                                                                board.player(2)
                                                                                for i in range(len(result2)):
                                                                                    board.add_beads(i + 1, result2[i])
                                                                                if online_player_id == 1:
                                                                                    board.player(1)
                                                                                    board.current_player = 1
                                                                                else:
                                                                                    board.player(2)
                                                                                    board.current_player = 2
                                                                                change_state(PLAY)
                                                                        else:
                                                                            change_state(1)
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
                                                                    tmp_pos = pygame.mouse.get_pos()
                                                                    if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                                    70 and
                                                                    tmp_pos[1] >= 30 and tmp_pos[1] <=
                                                                    70):
                                                                        change_state(0)
                                                                        done_gukenyura = True

                                                            clock.tick(60)


                                                else:
                                                    position = pygame.mouse.get_pos()
                                                    data = game_coordinates_to_data(position[0], int(position[1]))
                                                    if (data[1] >=1 and data[1]<=16):##if the player clicks outside the buttons to chose the number of beads
                                                        if (not( (position[0] >= tmp_position[0] and position[0] <= tmp_position[
                                                            0] + 85) and (position[1] > tmp_position[1] and position[1]<= tmp_position[1] + 175+13))):
                                                            clicked = True
                                                            tmp_position[0] = position[0]
                                                            tmp_position[1] = position[1]
                                                            print(position)
                                                            print(data)
                                                        else:
                                                            clicked = False
                                                            number_of_beads = 0
                                                            temp =   position[1] - tmp_position[1] # temp helps us to retrieve how many beads the palyer clicked on based on the y axis

                                                            if temp >= 0 and temp <= 175 : #beads buttons
                                                                temp = int (temp /11) + 1
                                                                temp_x = position[0]- tmp_position[0]
                                                                temp_x = int(temp_x / 42) + 1
                                                                if temp_x == 1 : number_of_beads = temp
                                                                elif temp_x == 2 : number_of_beads = temp + 16
                                                            else:# the clear beads button
                                                                number_of_beads = 0
                                                                print ("ici on vide le trou")

                                                            print(maximum)
                                                            tmp_data = game_coordinates_to_data(tmp_position[0],
                                                                                                int(tmp_position[1]))
                                                            beads_to_take = board.beads(tmp_data[1])
                                                            tmp_max = maximum - (number_of_beads - beads_to_take)
                                                            # maximum = maximum - (number_of_beads - beads_to_take)
                                                            print(tmp_max)
                                                            if (tmp_max >= 0 and tmp_max <= 32):
                                                                maximum = tmp_max
                                                                board.take_beads(tmp_data[1], beads_to_take)
                                                                # for i in range(1, number_of_beads + 1):
                                                                board.add_beads(tmp_data[1], number_of_beads)
                                                            print(position)
                                                            data = game_coordinates_to_data(position[0], int(position[1]))
                                                            print(data)


                                                    else:# if the wanted number of beads is printed out of the board zone in the white empty zone or on the other buttons
                                                        clicked = False
                                                        if (((position[0] > tmp_position[0] and position[0] <=
                                                                  tmp_position[
                                                                      0] + 85) and (
                                                                         position[1] > tmp_position[1] and position[
                                                                     1] <= tmp_position[1] + 175+15))):
                                                            number_of_beads = 0
                                                            temp = position[1] - tmp_position[1]
                                                            if temp >= 0 and temp <= 175:  # beads buttons
                                                                temp = int(temp / 11) + 1
                                                                temp_x = position[0] - tmp_position[0]
                                                                temp_x = int(temp_x / 42) + 1
                                                                if temp_x == 1:
                                                                    number_of_beads = temp
                                                                elif temp_x == 2:
                                                                    number_of_beads = temp + 16
                                                            else:  # the clear beads button
                                                                number_of_beads = 0
                                                                # print("ici on vide le trou")

                                                            tmp_data = game_coordinates_to_data(tmp_position[0],
                                                                                                int(tmp_position[1]))
                                                            beads_to_take = board.beads(tmp_data[1])
                                                            tmp_max = maximum - (number_of_beads - beads_to_take)
                                                            # maximum = maximum - (number_of_beads - beads_to_take)
                                                            print(tmp_max)
                                                            if tmp_max >= 0 and tmp_max <= 32:
                                                                maximum = tmp_max
                                                                board.take_beads(tmp_data[1], beads_to_take)
                                                                board.add_beads(tmp_data[1], number_of_beads)
                                                            print(position)
                                                            data = game_coordinates_to_data(position[0], int(position[1]))
                                                            print(data)

                                    clock.tick(60)
                            elif(data[1] == 17):
                                while not event.type == pygame.MOUSEBUTTONUP:
                                    screen.fill(WHITE)
                                    tmp_pos = pygame.mouse.get_pos()
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
                                            tmp_pos = pygame.mouse.get_pos()
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
                                    tmp_pos = pygame.mouse.get_pos()
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
                                            tmp_pos = pygame.mouse.get_pos()
                                            if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                    122 and
                                                    tmp_pos[1] >= 520 and tmp_pos[1] <=
                                                    572):
                                                if online_game:  # online game handler

                                                    print(online_helper.send_starting_setting(n, board.stringify()))
                                                    reply = online_helper.decode_reply(
                                                        online_helper.get_starting_setting(n))
                                                    print(reply)
                                                    if (reply == "waiting"):
                                                        change_state(WAITING_FROM_SET_BOARD)

                                                    else:
                                                        result2 = online_helper.string_to_list(
                                                            reply)
                                                        board.player(2)
                                                        for i in range(len(result2)):
                                                            board.add_beads(i + 1, result2[i])
                                                        if online_player_id == 1:
                                                            board.player(1)
                                                            board.current_player = 1
                                                        else:
                                                            board.player(2)
                                                            board.current_player = 2
                                                        change_state(PLAY)
                                                else:
                                                    change_state(1)
                                                    board.default_player2()
                                                done_gukenyura = True

                                    clock.tick(60)

                            elif(data[1] == 19): # menu button clicked from the gukenyura (set up board) state
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
                                            tmp_pos = pygame.mouse.get_pos()
                                            if (tmp_pos[0] >= 30 and tmp_pos[0] <=
                                                    70 and
                                                    tmp_pos[1] >= 30 and tmp_pos[1] <=
                                                    70):
                                                change_state(0)
                                                done_gukenyura = True

                                    clock.tick(60)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    change_design()
                elif event.key == pygame.K_p:
                    design_2 = not design_2



        clock.tick(60)
    pygame.quit()
    # pygame.quit()
    print ("fin")
    print (board.BOARD)

if __name__ == '__main__':
    main()
