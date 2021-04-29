import Circle
import numpy
import math

class Car(Circle.Circle):

    acceleration = 60.0

    def __init__(self,x,y,sprite):
        super(Car, self).__init__(x,y,sprite)

    def accelerate(self,direction, fps):
        self.velocity += numpy.array([self.acceleration * math.cos(direction) /fps, self.acceleration * -math.sin(direction) / fps])
