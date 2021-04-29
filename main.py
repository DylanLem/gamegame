from Circle import *
import math
import os.path
import random
import pygame
import numpy

# load an image of the smiley dude
SPR_SOME_CAR = pygame.image.load(os.path.join("sprites", "car.png"))
# stretch out the sprite
SPR_SOME_CAR = pygame.transform.scale(SPR_SOME_CAR, (32,64))

# width and height of the game window
WIDTH, HEIGHT = 640, 640
# create the game window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# set the title and icon of the game window
pygame.display.set_caption("Gamegame")
pygame.display.set_icon(SPR_SOME_CAR)

# how many frames per second the game will run at
FPS = 60

# define some colours by their rgb values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_everything(instances):
    # draw a white background
    WINDOW.fill(WHITE)

    # draw each instance in instances
    for instance in instances:
        WINDOW.blit(instance.sprite, (instance.x - instance.sprite.get_width()/2,
                                      instance.y - instance.sprite.get_height()/2))

    # update the display
    pygame.display.update()


def main():
    # a list to hold all the objects that are active in the game
    instances = []

    # create an instance for a smiley dude and add it to instances
    some_car = Circle(WIDTH/2, HEIGHT/2, SPR_SOME_CAR)
    some_car.r = 32
    instances.append(some_car)

    # create a pygame clock (used to limit the game to run at a certain fps)
    clock = pygame.time.Clock()

    # this is the code that will run while the game is running
    run = True
    while run:
        # tick the clock at our specified fps (idk what this actually means tbh,
        # but it works apparently)
        clock.tick(FPS)
        # check if any of the pygame events are of type QUIT and if so, end the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # get an array of the currently pressed keys
        keys_pressed = pygame.key.get_pressed()

        # get the position of the mouse
        mousepos = pygame.mouse.get_pos()

        # snap the dude's position to the mouse
        some_car.x = mousepos[0]
        some_car.y = mousepos[1]

        # draw the contents of the window
        draw_everything(instances)

    # at this point the while loop condition was broken, so the game ends.


# if we're running from this script itself, call the main function
if __name__ == '__main__':
    main()
