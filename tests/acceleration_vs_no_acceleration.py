import pygame
import os

_image_library = {}
######################
# Define some colors #
######################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size = (900,600)
screen = pygame.display.set_mode(size)

state = False


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image



circle_activated_path = "../assets/buttons/slide_circle_right.png"
slider_deactivated_path = "../assets/buttons/slider_deactivated.png"
hider_pannel_path = "../assets/buttons/design_2/hider_white.png"

def animate_slider(clock):
    time = 0
    destination = 0
    destination2 = 0

    vitesse = 10
    acceleration = 0.0717
    # acceleration = 0

    while(destination < 698 or destination2 < 698):
        screen.blit(pygame.transform.smoothscale(get_image(hider_pannel_path), (750, 40)), (90, 195))
        pygame.draw.rect(screen, BLACK, pygame.Rect(100, 202, 700, 16), 1)

        if destination <= 698:
            destination = int(-0.5 * acceleration * time * time) + int(vitesse * time)
        pygame.draw.rect(screen, GREEN, pygame.Rect(101, 203, destination, 14))
        screen.blit(pygame.transform.smoothscale(get_image(circle_activated_path), (30, 30)), (95+destination, 195))


        screen.blit(pygame.transform.smoothscale(get_image(hider_pannel_path), (750, 40)), (90, 390))
        pygame.draw.rect(screen, BLACK, pygame.Rect(100, 398, 700, 16), 1)
        if (destination2 <= 698):
            destination2 = int(vitesse * time)
        pygame.draw.rect(screen, GREY, pygame.Rect(101, 399, destination2, 14))
        screen.blit(pygame.transform.smoothscale(get_image(circle_activated_path), (30, 30)), (95 + destination2, 391))

        pygame.display.flip()
        clock.tick(60)
        time += 1

def draw():
    screen.fill(WHITE)
    # surface = pygame.display.set_mode((700, 20))
    # screen.blit(pygame.transform.smoothscale(get_image(slider_deactivated_path), (800, 20)), (100, 200))
    pygame.draw.rect(screen, BLACK, pygame.Rect(100,202,700,16),1)
    screen.blit(pygame.transform.smoothscale(get_image(circle_activated_path), (30, 30)), (95, 195))

    pygame.draw.rect(screen, BLACK, pygame.Rect(100, 398,700, 16), 1)
    screen.blit(pygame.transform.smoothscale(get_image(circle_activated_path), (30, 30)), (95, 391))

def main():
    done = False
    clock = pygame.time.Clock()
    moves = 0
    screen.fill(WHITE)

    while (not done):
        position = pygame.mouse.get_pos()
        draw()
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    print (position)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    animate_slider(clock)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
