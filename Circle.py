import numpy
import math

# a list of all Circle objects in the game
circles = []


# circle collision:
def resolve_collision():
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
            if dist < c1.r + c2.r:
                # calculate the angle from the line between c1-c2 to the x-axis
                theta = math.asin(abs(dy) / dist)
                # calculate the overlap between c1 and c2
                overlap = (c1.r + c2.r) - dist
                overlap_x = (overlap / 2) * math.cos(theta)
                overlap_y = (overlap / 2) * math.sin(theta)

                # move the circles out of each other
                c1.x += overlap_x * -numpy.sign(dx)
                c1.y += overlap_y * -numpy.sign(dy)
                c2.x += overlap_x * numpy.sign(dx)
                c2.y += overlap_y * numpy.sign(dy)


class Circle:
    def __init__(self, x, y, sprite):
        # the sprite of this circle
        self.sprite = sprite
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
        self.hspd = 0.0
        self.vspd = 0.0
        # the velocity vector of this circle
        self.velocity = numpy.array([self.hspd, self.vspd])
