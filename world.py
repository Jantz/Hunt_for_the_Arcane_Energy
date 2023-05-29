# Import modules
import graphics
import random, math

# Define the world class.
class World():
    def __init__(self):

        # Define the world grid.
        self.worldSize = [100, 100]
        self.worldGrid = [[0 for _ in range(self.worldSize[0])] for _ in range(self.worldSize[1])]
        self.change_world(0.8,0,1)
        self.worldOrigin = [0, 0]
        self.unitSize = 64

        # Define the world objects.
        self.npcs = []
        self.player = None

        # Load sprites
        self.sprites = graphics.load_sprites("assets/world")

        self.playerPosUnit = [len(self.worldGrid)/2, len(self.worldGrid[0])/2]
    
    ''''
    # Function to blit the visible world to the world surface.
    def blit_world(self, worldSurface, playerPosUnit, screenX, screenY):
        topLeftIndex = [round(playerPosUnit[0] - screenX/(2*self.unitSize)), round(playerPosUnit[1] - screenY/(2*self.unitSize))]
        bottomRightIndex = [round(playerPosUnit[0] + screenX/(2*self.unitSize)), round(playerPosUnit[1] + screenY/(2*self.unitSize))]
        offsetX = playerPosUnit[0] - (topLeftIndex[0] + 0.5)
        offsetY = playerPosUnit[1] - (topLeftIndex[1] + 0.5)
        for j in range(int(topLeftIndex[1]), int(bottomRightIndex[1])):
            for i in range(int(topLeftIndex[0]), int(bottomRightIndex[0])):
                if i >= 0 and i < self.worldSize[0] and j >= 0 and j < self.worldSize[1]:
                    if self.worldGrid[i][j] != None:
                        worldSurface.blit(self.sprites[self.worldGrid[i][j]], ((i - topLeftIndex[0])*self.unitSize, (j - topLeftIndex[1])*self.unitSize))
                        #self.worldGrid[i][j]
        return worldSurface
    '''
    # Function to blit the visible world to the world surface.
    def blit_world(self, worldSurface, playerPosUnit, screenX, screenY):
        topLeftIndex = [int(playerPosUnit[0] - screenX / (2 * self.unitSize)), int(playerPosUnit[1] - screenY / (2 * self.unitSize))]
        bottomRightIndex = [int(playerPosUnit[0] + screenX / (2 * self.unitSize)), int(playerPosUnit[1] + screenY / (2 * self.unitSize))]
        # Calculate the fractional offset within the grid cell
        offset_x = (playerPosUnit[0] - math.floor(playerPosUnit[0])) * self.unitSize
        offset_y = (playerPosUnit[1] - math.floor(playerPosUnit[1])) * self.unitSize
        for j in range(topLeftIndex[1], bottomRightIndex[1] + 1):
            for i in range(topLeftIndex[0], bottomRightIndex[0] + 1):
                if i >= 0 and i < self.worldSize[0] and j >= 0 and j < self.worldSize[1]:
                    if self.worldGrid[i][j] != None:
                        draw_x = (i - topLeftIndex[0]) * self.unitSize - offset_x
                        draw_y = (j - topLeftIndex[1]) * self.unitSize - offset_y
                        worldSurface.blit(self.sprites[self.worldGrid[i][j]], (draw_x, draw_y))

        print(playerPosUnit[0], offset_x, playerPosUnit[1], offset_y)
        return worldSurface

    
    def move_player(self, playerObj, dt):
        return [self.playerPosUnit[0] + playerObj.xDir * dt * playerObj.movementSpeed, self.playerPosUnit[1] + playerObj.yDir * dt * playerObj.movementSpeed]
    
    # Function that takes a probability and changes worldGrid one cell to another type.
    def change_world(self, probability, fromType, toType):
        for i in range(len(self.worldGrid)):
            for j in range(len(self.worldGrid[i])):
                if self.worldGrid[i][j] == fromType and random.random() < probability:
                    self.worldGrid[i][j] = toType