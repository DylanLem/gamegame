from Constants import *
import Entity



class Level:

    #we can pull level data from text files to generate the map
    def __init__(self, levelData):

        file = open(levelData, "r")

        #line 1 defines the boundaries of the level
        sizeData = file.readline()

        self.width = int(sizeData.split(",")[0])
        self.height = int(sizeData.split(",")[1])

        #Initializing a list with the correct dimensions
        #Each entry in the list represents a row of tiles
        levelList = [[]]* self.height

        #Iterates through our level file
        i = 0
        for line in file:
            line = line.rstrip("\n")
            levelList[i] = (line.split(","))
            i+= 1


        self.tiles = [[]] * self.height
        #Now we initialize the tiles
        for i in range(len(levelList)):
            self.tiles[i] = []

            for j in range(self.width):
                val = int(levelList[i][j])

                # Builds a tile based on the value
                if(val == 0):
                    t = Entity.Tile(ROAD_TILE, ((j+1) * TILE_SCALE[0]) - TILE_SCALE[0]/2,
                                    ((i+1) * TILE_SCALE[1]) - TILE_SCALE[1]/2)
                    self.tiles[i].append(t)
                elif(val == 1):
                    t = Entity.Tile(WALL_TILE, ((j+1) * TILE_SCALE[0]) - TILE_SCALE[0]/2,
                                    ((i+1) * TILE_SCALE[1]) - TILE_SCALE[1]/2)
                    t.passable = False
                    self.tiles[i].append(t)
                Entity.get_tiles().append(self.tiles[i][j])
        print(len(self.tiles[4]))
