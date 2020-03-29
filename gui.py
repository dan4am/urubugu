import board
import threading
import pygame
import os
import math


_image_library = {}

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
def get_img(beads):
    path = getpath(beads)
    return get_image(path)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BEAD = 5
BETWEEN_SLOTS = 5
SLOTS = 40
BOARD_WIDTH = BETWEEN_SLOTS*6+ SLOTS*2 * 4
BOARD_LENGTH = BETWEEN_SLOTS*9+ SLOTS*2 * 8

# def Draw_board():



pygame.init()

# Set the width and height of the screen [width, height]
size = (800,600)
screen = pygame.display.set_mode(size)
circle_filled=pygame.Surface(size)

def draw_frame():
    pygame.draw.line(screen, BLACK, [54, 122], [54, 478], 1)
    pygame.draw.line(screen, BLACK, [744, 122], [744, 478], 1)
    pygame.draw.line(screen, BLACK, [54, 122], [743, 122], 1)
    pygame.draw.line(screen, BLACK, [54, 478], [743, 478], 1)
    pygame.draw.line(screen, WHITE, [57, 300], [742, 300], 8)
    pygame.draw.line(screen, BLACK, [54, 300], [743, 300], 2)

def hole_to_coordinates(line, row):
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
            pygame.draw.circle(screen, WHITE, hole_to_coordinates(line, row), SLOTS-5)
            if(not board.BOARD[line][row] == 0):
                screen.blit(get_img(board.BOARD[line][row]),  (hole_to_coordinates(line, row)[0]-65,hole_to_coordinates(line, row)[1]-68))
                pygame.draw.circle(screen, WHITE, hole_to_coordinates(line, row), SLOTS-2,1)


# def gui_hread():

pygame.display.set_caption("My Game")
def main():
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    place =[(800-BOARD_LENGTH) / 2 , (600 - BOARD_WIDTH) / 2, BOARD_LENGTH, BOARD_WIDTH]
    screen.fill(WHITE)
    draw_frame()
    draw_slots()
    board.player(2)
    while not done:


        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                place = [57 , 125, BOARD_LENGTH, BOARD_WIDTH]

        # screen.fill(WHITE)
        # draw_frame()
        # draw_slots()
        # --- Game logic should go here
        # board.player(2)
        if (board.player_one):
            slot = int(input("player one choose slot between 1 and 16 : "))
            result = board.beads(slot)
            while (result == 0):
                slot = int(input("player one choose another slot between 1 and 16 that one is empty : "))
                result = board.beads(slot)
            board.play(slot)
            board.player(2)
        else:
            slot = int(input("player two choose slot between 1 and 16 : "))
            result = board.beads(slot)
            while (result == 0):
                slot = int(input("player twoo choose another slot between 1 and 16 that one is empty : "))
                result = board.beads(slot)
            board.play(slot)
            board.player(1)
        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)

        # --- Drawing code should go here
        pygame.draw.rect(screen, BLACK, place)
        # pygame.draw.rect(screen, BLACK, place)

        draw_frame()
        draw_slots()
        # screen.blit(get_image('compressed_pictures/30_beads.png'), (20, 20))
        # pygame.draw.line(screen, BLACK, [54, 122], [54, 478], 1)
        # pygame.draw.line(screen, BLACK, [744, 122], [744, 478], 1)
        # pygame.draw.line(screen, BLACK, [54, 122], [743, 122], 1)
        # pygame.draw.line(screen, BLACK, [54, 478], [743, 478], 1)
        # pygame.draw.line(screen, WHITE, [57, 300], [742, 300], 10)
        # pygame.draw.line(screen, BLACK, [57, 300], [742, 300], 2)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)
        # getpath(60)

    # Close the window and quit.
    pygame.quit()
if __name__ == '__main__':
    main()
