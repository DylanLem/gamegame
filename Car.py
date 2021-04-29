import circle
import numpy

class Car(Circle):
    friction = 4
    acceleration = 15

    def accelerate(direction, fps):
        velocity += (numpy.array([acceleration * math.cos(direction), acceleration * -math.sin(direction)]) * fps
