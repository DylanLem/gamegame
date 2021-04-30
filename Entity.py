from Constants import *
import numpy
import math

# a list of lists of entities currently in the game.
# set up such that each index of this list is a list of a certain type of entity.
# for example, entities[0] is the list of all circles currently in the game.
# entities[1] could be the list of all rectangles, and so on.
# there may be a cleaner way to do this but whatevs for now >:}
entities = [
    []     # index 0 is for the list of circles
           # more lists to come, but so far we just have circles
]


# this functions tracks down and resolves collisions between all circles currently
# in the game.
# eventually this will be generalized to all entities, not just circles, so that we're
# only checking each entity once. a new function resolve_collision should loop through
# every entity similarly to how this function does it, but while doing so it will check
# the type of each entity, and resolve their collision accordingly. for example, if the
# two entities being checked are circles, resolve it exactly like we've done here. if
# entity 1 is a circle and entity 2 is a rectangle, we'll need to resolve collision
# between a circle and a rectangle.
def resolve_circles_collision():
    circles = get_circles()
    for i in range(len(circles)):               # for every circle, i, in circles
        for j in range(i + 1, len(circles)):    # for every remaining circle, j, starting from i, in circles
            # get the i-th and j-th circles
            c1 = circles[i]
            c2 = circles[j]

            # calculate the x and y distances between c1 and c2
            dx = c2.x - c1.x
            dy = c2.y - c1.y
            # and calculate the distance directly between their two centers
            dist = math.sqrt(pow(dx, 2) + pow(dy, 2))

            # if the distance is less than the sum of their two radii,
            # we have a collision
            if dist < c1.radius + c2.radius:
                # calculate the angle from the line between c1-c2 to the x-axis
                theta = math.asin(abs(dy) / dist)
                # calculate the overlap between c1 and c2
                overlap = (c1.radius + c2.radius) - dist
                overlap_x = (overlap / 2) * math.cos(theta)
                overlap_y = (overlap / 2) * math.sin(theta)

                # move the circles out of each other
                c1.x += overlap_x * -numpy.sign(dx)
                c1.y += overlap_y * -numpy.sign(dy)
                c2.x += overlap_x * numpy.sign(dx)
                c2.y += overlap_y * numpy.sign(dy)


# get the list of all the circles in the game
def get_circles():
    return entities[0]


# create a car object
def create_car(sprite, x, y, accl, fric):
    # create the car
    car = Car(sprite, x, y, accl, fric)
    # add the car to its appropriate list
    get_circles().append(car)
    # return the car
    return car


# remove a car from the game
def delete_car(car):
    # remove car from its entity list
    get_circles().remove(car)
    del car


class Entity:
    def __init__(self, sprite, x, y):
        # the sprite of this entity
        self.sprite = sprite
        # the x and y positions of this entity
        self.x = x
        self.y = y
        # speed and direction (in degrees) that this entity is travelling (0=east)
        self.spd = 0.0
        self.dir = 0.0
        # the horizontal and vertical components of this entity's velocity
        self.hspd = 0.0
        self.vspd = 0.0

    # calculate the signed horizontal and vertical speeds of the entity
    # from its current speed and direction
    def calculate_vel_components(self):
        # do some trig to find the x and y components from the entity's speed and
        # direction (direction is converted to radians here)
        # vspd has its sign flipped because pygame counts y up as objects move down
        # the screen, whereas the cartesian plane counts y up as objects move up.
        self.hspd = self.spd * math.cos(self.dir * (math.pi / 180))
        self.vspd = self.spd * -math.sin(self.dir * (math.pi / 180))

    # move the entity's position by its hspd and vspd
    def move(self):
        # first gotta calculate hspd and vspd
        self.calculate_vel_components()
        # then move the entity
        self.x += self.hspd
        self.y += self.vspd


class Circle(Entity):
    def __init__(self, sprite, x, y, r):
        # call the superclass initializer
        super().__init__(sprite, x, y)
        # radius of this circle
        self.radius = r
        # the velocity vector of this circle
        self.velocity = numpy.array([self.hspd, self.vspd])
        # the position of this circle
        self.pos = numpy.array([self.x, self.y])


#                      ______
#       vroom        /       \
#           _______/          \_____
#          |                        \
#         |     __           __     |
#          ----/  \---------/  \----
#              \__/         \__/
#
# Cars have a circle hitbox so it inherits from the Circle class
class Car(Circle):
    def __init__(self, sprite, x, y, accl, fric):
        # call the superclass initializer
        # (the "radius" of a car is set to its sprite's height divided by 2 here.
        # this is like how big the hitbox of the car is)
        super().__init__(sprite, x, y, sprite.get_height()/2)
        # how quickly this car will accelerate
        self.acceleration = accl
        # the orientation of this car
        self.orientation = 0.0
        # the friction experienced by this car
        self.friction = fric
        # the maximum speed that this car can travel
        self.max_speed = 5.0

    def move(self):
        # first, reduce the cars speed by its friction
        if self.spd - self.friction >= 0:
            self.spd -= self.friction
        else:
            self.spd = 0
        # call move() from the superclass
        super().move()

    def accelerate(self, direction):
        self.velocity += numpy.array([self.acceleration * math.cos(direction) / FPS,
                                      self.acceleration * -math.sin(direction) / FPS])
        self.orientation = ((direction - math.pi / 2) / (2 * math.pi)) * 360

    # turn the car left or right (counter-clockwise or clockwise)
    #   direction - the direction in degrees to turn the car (negative values turn right)
    def turn(self, direction):
        # add the given direction to the car's direction.
        # the amount added is proportional to the car's speed to simulate the effects
        # of a real steering wheel. like, if you steer a car while not moving, you
        # wont actually turn. but you can turn sharper the faster you're going.
        self.dir += direction * (self.spd / self.max_speed)
        # wrap dir back to 0 if greater than 360, or back to 360 if less than 0.
        self.dir = self.dir % 360
        # update the car's sprite
        self.update_sprite_angle()

    # update the sprite of this car to match the direction it is currently facing
    def update_sprite_angle(self):
        if self.dir > 337.5 or self.dir <= 22.5:
            self.sprite = SPR_CAR_EAST
        elif 22.5 < self.dir <= 67.5:
            self.sprite = SPR_CAR_NORTHEAST
        elif 67.5 < self.dir <= 112.5:
            self.sprite = SPR_CAR_NORTH
        elif 112.5 < self.dir <= 157.5:
            self.sprite = SPR_CAR_NORTHWEST
        elif 157.5 < self.dir <= 202.5:
            self.sprite = SPR_CAR_WEST
        elif 202.5 < self.dir <= 247.5:
            self.sprite = SPR_CAR_SOUTHWEST
        elif 247.5 < self.dir <= 295.5:
            self.sprite = SPR_CAR_SOUTH
        elif 295.5 < self.dir <= 337.5:
            self.sprite = SPR_CAR_SOUTHEAST
