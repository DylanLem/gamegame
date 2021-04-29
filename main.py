import math
import os.path
import random
import pygame
import numpy
import Car



# load an image of the smiley dude
SPR_SMILEGUY = pygame.image.load(os.path.join("sprites", "smileguy.png"))
# stretch out the sprite
SPR_SMILEGUY = pygame.transform.scale(SPR_SMILEGUY, (64,64))
# the speed of smile dude
SMILEGUY_SPEED = 2

# width and height of the game window
WIDTH, HEIGHT = 640, 640
# create the game window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# set the title and icon of the game window
pygame.display.set_caption("Lil' Smile Dude")
pygame.display.set_icon(SPR_SMILEGUY)

# how many frames per second the game will run at
FPS = 60

# define some colours by their rgb values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Circle:
    def __init__(self, x, y, sprite):
        # the sprite of this circle
        self.sprite = sprite
        # the colour of this circle
        self.colour = BLACK
        # the x and y positions of the center of this circle
        self.x = x
        self.y = y
        # radius of this circle
        self.r = 0
        # speed that this circle is travelling
        self.spd = 0
        # direction in radians that this circle is travelling (0 = east)
        self.dir = 0
        # the horizontal and vertical speeds of this circle
        self.hspd = 0
        self.vspd = 0
        # the friction experienced by this circle
        self.friction = 0
        # the gravity experienced by this circle
        self.grav = 0


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
    smileguy = Circle(WIDTH/2, HEIGHT/2, SPR_SMILEGUY)
    carguy = Car(WIDTH/2, HEIGHT/2, SPR_SMILEGUY)


    smileguy.r = 32
    instances.append(smileguy)

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

        # space spawns a guy in the center of the screen
        if keys_pressed[pygame.K_SPACE]:
            xoffset = random.randint(-10, 10)
            yoffset = random.randint(-10, 10)
            inst = Circle(WIDTH / 2 + xoffset, HEIGHT / 2 + yoffset, SPR_SMILEGUY)
            inst.r = 32
            instances.append(inst)

        # move the smile dude depending on what key is pressed
        if keys_pressed[pygame.K_RIGHT]:
            carguy.accelerate(0)
        if keys_pressed[pygame.K_UP]:
            carguy.accelerate(-math.PI/2)
        if keys_pressed[pygame.K_LEFT]:
            carguy.accelerate(math.PI)
        if keys_pressed[pygame.K_DOWN]:
            carguy.accelerate(math.PI/2)

        # get the position of the mouse
        mousepos = pygame.mouse.get_pos()

        # snap the dude's position to the mouse
        #smileguy.x = mousepos[0]
        #smileguy.y = mousepos[1]

        # circle collision:
        for i in range(len(instances)):
            for j in range(i+1, len(instances)):
                # get the i-th and j-th circles
                c1 = instances[i]
                c2 = instances[j]

                # calculate the x and y distances between c1 and c2
                dx = c2.x - c1.x
                dy = c2.y - c1.y
                # and calculate the distance directly between their two centers
                dist = math.sqrt(pow(dx,2) + pow(dy,2))

                # if the distance is less than the sum of their two radii,
                # we have a collision
                if dist < c1.r + c2.r:
                    # calculate the angle from the line between c1-c2 to the x-axis
                    theta = math.asin(abs(dy) / dist)
                    # calculate the overlap between c1 and c2
                    overlap = (c1.r + c2.r) - dist
                    overlap_x = (overlap/2) * math.cos(theta)
                    overlap_y = (overlap/2) * math.sin(theta)

                    #
                    c1.x += (overlap_x) * -numpy.sign(dx)
                    c1.y += (overlap_y) * -numpy.sign(dy)
                    c2.x += (overlap_x) * numpy.sign(dx)
                    c2.y += (overlap_y) * numpy.sign(dy)

        # draw the contents of the window
        draw_everything(instances)

    # at this point the while loop condition was broken, so the game ends.


# if we're running from this script itself, call the main function
if __name__ == '__main__':
    main()
