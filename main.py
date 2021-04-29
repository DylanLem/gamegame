import pygame
import os.path
import math
import Entity

# initialize pygame's font stuff
pygame.font.init()
# initialize pygame's sound stuff
pygame.mixer.init()

# set some medium sized font
FONT_MEDIUM = pygame.font.SysFont('Calibri', 20)

# load some car sprites
SPR_CAR_EAST      = pygame.image.load(os.path.join("sprites", "car_east.png"))
SPR_CAR_NORTHEAST = pygame.image.load(os.path.join("sprites", "car_northeast.png"))
SPR_CAR_NORTH     = pygame.image.load(os.path.join("sprites", "car_north.png"))
SPR_CAR_NORTHWEST = pygame.transform.flip(pygame.image.load(os.path.join("sprites",
                                          "car_northeast.png")), True, False)
SPR_CAR_WEST      = pygame.transform.flip(pygame.image.load(os.path.join("sprites",
                                          "car_east.png")), True, False)
SPR_CAR_SOUTHWEST = pygame.transform.flip(pygame.image.load(os.path.join("sprites",
                                          "car_southeast.png")), True, False)
SPR_CAR_SOUTH     = pygame.image.load(os.path.join("sprites", "car_south.png"))
SPR_CAR_SOUTHEAST = pygame.image.load(os.path.join("sprites", "car_southeast.png"))

# stretch out the above sprites
SPR_CAR_EAST      = pygame.transform.scale2x(SPR_CAR_EAST)
SPR_CAR_NORTHEAST = pygame.transform.scale2x(SPR_CAR_NORTHEAST)
SPR_CAR_NORTH     = pygame.transform.scale2x(SPR_CAR_NORTH)
SPR_CAR_NORTHWEST = pygame.transform.scale2x(SPR_CAR_NORTHWEST)
SPR_CAR_WEST      = pygame.transform.scale2x(SPR_CAR_WEST)
SPR_CAR_SOUTHWEST = pygame.transform.scale2x(SPR_CAR_SOUTHWEST)
SPR_CAR_SOUTH     = pygame.transform.scale2x(SPR_CAR_SOUTH)
SPR_CAR_SOUTHEAST = pygame.transform.scale2x(SPR_CAR_SOUTHEAST)

# load an image of a car
SPR_SOME_CAR = pygame.image.load(os.path.join("sprites", "car.png"))
# stretch out the sprite
SPR_SOME_CAR = pygame.transform.scale(SPR_SOME_CAR, (32, 64))

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


# draw everything that is to be displayed on the screen
def draw_everything(instances, somecar):
    # draw a white background
    WINDOW.fill(WHITE)

    # draw each instance in instances
    for objType in instances:
        for obj in objType:
            #obj.sprite = pygame.transform.rotate(obj.sprite, obj.dir)
            WINDOW.blit(obj.sprite, (obj.x - obj.sprite.get_width() / 2,
                                     obj.y - obj.sprite.get_height() / 2))

    # create some info to display
    text = []
    text.append(FONT_MEDIUM.render("accl: " + str(somecar.acceleration),
                                   False, BLACK))
    text.append(FONT_MEDIUM.render("dir: " + str(somecar.dir), False, BLACK))

    # draw all the info
    i = 0
    for t in text:
        WINDOW.blit(t, (10, 10 + 20 * i))
        i += 1

    # update the display
    pygame.display.update()


def main():
    # create an instance for a smiley dude and add it to instances
    some_car = Entity.create_car(SPR_CAR_EAST, WIDTH / 2, HEIGHT / 2, 3.0)

    # create anutha car
    another_car = Entity.create_car(SPR_CAR_NORTHEAST, 200, 200, 1.0)

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

        # accelerate some car by the arrow keys
        if keys_pressed[pygame.K_LEFT]:
            some_car.turn(3)
        if keys_pressed[pygame.K_RIGHT]:
            some_car.turn(-3)

        if keys_pressed[pygame.K_SPACE]:
            some_car.accelerate(some_car.dir)

        # get the position of the mouse
        mouse_position = pygame.mouse.get_pos()

        # move da car
        # (move() should really be called for every Circle on every game step,
        # but for now we just have the 1 car)
        some_car.move()

        # keep da other car at 200,200
        another_car.x = 200
        another_car.y = 200

        # resolve collision of all circles
        Entity.resolve_circles_collision()

        # draw the contents of the window
        # (passing in the reference to some_car because we want to display some
        # of its info onto the screen)
        draw_everything(Entity.entities, some_car)

    # at this point the while loop condition was broken, so the game ends.


# (python wizardry)
if __name__ == '__main__':
    main()
