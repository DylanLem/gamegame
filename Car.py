import circle
import numpy

class Car(Circle):
    friction = 0f
    acceleration = 0f

    def accelerate(direction, fps):
        velocity += (numpy.array([acceleration * math.cos(direction), acceleration * -math.sin(direction)]) * fps
