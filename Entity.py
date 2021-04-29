import main
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
    for i in range(len(circles)):               # for every circle i in circles
        for j in range(i + 1, len(circles)):    # for every remaining circle j in circle
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
def create_car(sprite, x, y, accl):
    # create the car
    car = Car(sprite, x, y, accl)
    # add the car to its appropriate list
    get_circles().append(car)
    # return the car
    return car


# *** ABSTRACT OBJECTS LIKE SHAPES N WHATNOT ***

class Circle:
    def __init__(self, sprite, x, y, r):
        # the sprite of this circle
        self.sprite = sprite
        # the x and y positions of the center of this circle
        self.x = x
        self.y = y
        # radius of this circle
        self.radius = r
        # speed that this circle is travelling
        self.spd = 0.0
        # direction in radians that this circle is travelling (0 = east)
        self.dir = 0.0
        # the horizontal and vertical speeds of this circle
        self.hspd = 0.0
        self.vspd = 0.0
        # the velocity vector of this circle
        self.velocity = numpy.array([self.hspd, self.vspd])
        # the position of this circle
        self.pos = numpy.array([self.x, self.y])


# *** ACTUAL OBJECTS LIKE CARS AND STUFF ***

class Car(Circle):
    def __init__(self, sprite, x, y, accl):
        super().__init__(sprite, x, y, sprite.get_height()/2)
        self.acceleration = accl
        self.orientation = 0.0

    def accelerate(self, direction):
        self.velocity += numpy.array([self.acceleration * math.cos(direction) / main.FPS,
                                      self.acceleration * -math.sin(direction) / main.FPS])
        self.orientation = ((direction - math.pi / 2) / (2 * math.pi)) * 360
