from Constants import *
import Entity


# create an instance for a test car
test_car = Entity.create_car(SPR_CAR_EAST, WIDTH/2, HEIGHT/2, 0.1, 0.05)


# draw everything that is to be displayed on the screen
def draw_everything(instances):
    # draw a white background
    WINDOW.fill(WHITE)

    # draw each instance in instances
    for objType in instances:
        for obj in objType:
            WINDOW.blit(obj.sprite, (obj.x - obj.sprite.get_width() / 2,
                                     obj.y - obj.sprite.get_height() / 2))

    # create some info text to display
    text = [
        FONT_MEDIUM.render("accl: " + str(test_car.acceleration), False, BLACK),
        FONT_MEDIUM.render("dir: " + str(test_car.dir), False, BLACK),
        FONT_MEDIUM.render("spd: " + str(test_car.spd), False, BLACK)
    ]

    # draw all the info
    i = 0
    for t in text:
        WINDOW.blit(t, (10, 10 + 20 * i))
        i += 1

    # update the display
    pygame.display.update()


def main():
    # create some random car
    another_car = Entity.create_car(SPR_CAR_NORTHEAST, 200, 200, 1.0, 0.2)

    # create a pygame clock (used to limit the game to run at a certain fps)
    clock = pygame.time.Clock()

    # this is the code that will run while the game is running
    run = True
    while run:
        # tick the clock at our specified fps (idk what this actually means tbh,
        # but it works apparently)
        clock.tick(FPS)
        # loop through the pygame event queue
        for event in pygame.event.get():
            # end the game if the queue gets a "quit" event
            # (i believe this happens when the user clicks the X on the game window,
            # among other things im assuming but thats the only one i know rn)
            if event.type == pygame.QUIT:
                run = False

            # delete another_car on backspace (just testing key presses)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    Entity.delete_car(another_car)

        # get an array of the currently pressed keys
        keys_pressed = pygame.key.get_pressed()

        # turn the car with the arrow keys
        if keys_pressed[pygame.K_LEFT]:
            test_car.turn(3)
        if keys_pressed[pygame.K_RIGHT]:
            test_car.turn(-3)

        # accelerate the car with spacebar
        if keys_pressed[pygame.K_SPACE]:
            test_car.spd += test_car.acceleration

        # hit the brakes with shift (using negative acceleration to brake for now,
        # but at some point there will be a property of cars that determines how
        # good they are at braking)
        if keys_pressed[pygame.K_LSHIFT]:
            test_car.spd -= 3 * test_car.acceleration

        # move da car
        # (move() should really be called for every Entity on every game step,
        # but for now we just have the 1 car so this works)
        test_car.move()

        # resolve collision of all circles
        Entity.resolve_circles_collision()

        # draw the contents of the window
        # (passing in the reference to some_car because we want to display some
        # of its info onto the screen)
        draw_everything(Entity.entities)

    # at this point the while loop condition was broken, so the game ends.


# (python wizardry)
if __name__ == '__main__':
    main()
