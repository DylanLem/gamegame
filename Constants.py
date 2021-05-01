import pygame
import os.path

# initialize pygame's font stuff
pygame.font.init()
# initialize pygame's sound stuff
pygame.mixer.init()

# set a medium sized font
FONT_MEDIUM = pygame.font.SysFont('Calibri', 20)

# load some car sprites
SPR_CAR_EAST      = pygame.image.load(os.path.join("sprites", "car_east.png"))
SPR_CAR_NORTHEAST = pygame.image.load(os.path.join("sprites", "car_northeast.png"))
SPR_CAR_NORTH     = pygame.image.load(os.path.join("sprites", "car_north.png"))
SPR_CAR_NORTHWEST = pygame.transform.flip(pygame.image.load(os.path.join("sprites",
                                          "car_northeast.png")), True, False)
SPR_CAR_WEST      = pygame.transform.flip(pygame.image.load(os.path.join("sprites",
                                          "car_east.png")), True, False)
SPR_CAR_SOUTHWEST = pygame.transform.flip(pygame.image.load(os.path.join("sprites",
                                          "car_southeast.png")), True, False)
SPR_CAR_SOUTH     = pygame.image.load(os.path.join("sprites", "car_south.png"))
SPR_CAR_SOUTHEAST = pygame.image.load(os.path.join("sprites", "car_southeast.png"))

# stretch out the above sprites
SPR_CAR_EAST      = pygame.transform.scale2x(SPR_CAR_EAST)
SPR_CAR_NORTHEAST = pygame.transform.scale2x(SPR_CAR_NORTHEAST)
SPR_CAR_NORTH     = pygame.transform.scale2x(SPR_CAR_NORTH)
SPR_CAR_NORTHWEST = pygame.transform.scale2x(SPR_CAR_NORTHWEST)
SPR_CAR_WEST      = pygame.transform.scale2x(SPR_CAR_WEST)
SPR_CAR_SOUTHWEST = pygame.transform.scale2x(SPR_CAR_SOUTHWEST)
SPR_CAR_SOUTH     = pygame.transform.scale2x(SPR_CAR_SOUTH)
SPR_CAR_SOUTHEAST = pygame.transform.scale2x(SPR_CAR_SOUTHEAST)

# load an image of a car
SPR_SOME_CAR = pygame.image.load(os.path.join("sprites", "car.png"))
# stretch out the sprite
SPR_SOME_CAR = pygame.transform.scale(SPR_SOME_CAR, (32, 64))

# Tile sprites
ROAD_TILE = pygame.image.load(os.path.join("sprites", "road.png"))
WALL_TILE = pygame.image.load(os.path.join("sprites", "wall.png"))

TILE_SCALE = (64,64)

ROAD_TILE = pygame.transform.scale(ROAD_TILE, TILE_SCALE)
WALL_TILE = pygame.transform.scale(WALL_TILE, TILE_SCALE)

# LEVEL DATA
LEVEL0 = "Levels/level0.txt"


# width and height of the game window
WIDTH, HEIGHT = 640, 640
# create the game window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# set the title and icon of the game window
pygame.display.set_caption("Gamegame")
pygame.display.set_icon(SPR_SOME_CAR)

# how many frames per second the game will run at
FPS = 60

# define some colours by their rgb values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
