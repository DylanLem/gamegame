import Circle
import numpy
import math


class Car(Circle.Circle):
    acceleration = 1.0
    orientation = 0.0

    def __init__(self,x,y,sprite):
        super(Car, self).__init__(x,y,sprite)

    def accelerate(self,direction, fps):
<<<<<<< HEAD
        self.velocity += numpy.array([self.acceleration * math.cos(direction) /fps, self.acceleration * -math.sin(direction) / fps])

        s
=======
        self.velocity += numpy.array([self.acceleration * math.cos(direction) / fps,
                                      self.acceleration * -math.sin(direction) / fps])
>>>>>>> 6b0a918be5e5fa9403741cfbea423ff690c05618
        self.orientation = ((direction - math.pi/2)/(2*math.pi)) * 360
