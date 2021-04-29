import Circle
import numpy
import math

class Car(Circle.Circle):

    acceleration = 12.0
    orientation = 0.0
    def __init__(self,x,y,sprite):
        super(Car, self).__init__(x,y,sprite)

    def accelerate(self,direction, fps):
        self.velocity += numpy.array([self.acceleration * math.cos(direction) /fps, self.acceleration * -math.sin(direction) / fps])
        if(self.velocity[0] != 0):
            self.orientation = math.atan(self.velocity[1]/self.velocity[0])
