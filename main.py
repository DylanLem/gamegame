import pygame
import os.path
import math
import Entity

# load an image of the car
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


# draw the background and all current entities onto the screen
def draw_everything(instances):
    # draw a white background
    WINDOW.fill(WHITE)

    # draw each instance in instances
    for objType in instances:
        for obj in objType:
            sp = pygame.transform.rotate(obj.sprite, obj.orientation)
            WINDOW.blit(sp, (obj.x - obj.sprite.get_width() / 2,
                             obj.y - obj.sprite.get_height() / 2))

    # update the display
    pygame.display.update()


def main():
    # create an instance for a smiley dude and add it to instances
    some_car = Entity.create_car(SPR_SOME_CAR, WIDTH / 2, HEIGHT / 2, 3.0)

    # create anutha car
    another_car = Entity.create_car(SPR_SOME_CAR, 200, 200, 1.0)

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
            some_car.accelerate(math.pi)
        if keys_pressed[pygame.K_RIGHT]:
            some_car.accelerate(0)
        if keys_pressed[pygame.K_UP]:
            some_car.accelerate(math.pi / 2)
        if keys_pressed[pygame.K_DOWN]:
            some_car.accelerate(-math.pi / 2)

        # get the position of the mouse
        mouse_position = pygame.mouse.get_pos()

        # move da car by its velocity vector
        some_car.x += some_car.velocity[0]
        some_car.y += some_car.velocity[1]

        # keep da other car at 200,200
        another_car.x = 200
        another_car.y = 200

        # resolve collision of all circles
        Entity.resolve_circles_collision()

        # draw the contents of the window
        draw_everything(Entity.entities)

    # at this point the while loop condition was broken, so the game ends.


# (python wizardry)
if __name__ == '__main__':
    main()
