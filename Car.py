import circle


class Car(Circle):
    friction = 0f
    acceleration = 0f

    def move(direction, fps):
        #Takes in direction angle and FPS;
        normal_x = math.cos(direction)
        normal_y = math.sin(direction)    

        velocity += (acceleration * (1/60))
