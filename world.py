# Import modules
import graphics
import random, math, noise
import numpy as np

# Define the world class.
class World():
    def __init__(self):

        # Define the world grid.
        self.worldSize = [1024, 1000]
        self.noiseScale = 50
        self.worldGrid = self.generate_game_world(self.worldSize[0], self.worldSize[1], self.noiseScale)
        self.tileWeights = [0.3,0.05,0.15,0.4,0.1]
        self.tileTresholds = [0.15,0.17,0.22,0.35,0.6]
        self.worldGrid = self.transform_to_indexes()
        self.worldOrigin = [0, 0]
        self.unitSize = 64

        # Define the world objects.
        self.npcs = []
        self.player = None

        # Load sprites
        self.sprites = graphics.load_sprites("assets/world")

        self.playerPosUnit = [len(self.worldGrid)/2, len(self.worldGrid[0])/2]

    # Function to blit the visible world to the world surface.
    def blit_world(self, worldSurface, playerPosUnit, screenX, screenY):
        topLeftIndex = [math.floor(playerPosUnit[0]-screenX/(2*self.unitSize)), math.floor(playerPosUnit[1]-screenY/(2*self.unitSize))]
        bottomRightIndex = [math.ceil(playerPosUnit[0]+screenX/(2*self.unitSize)), math.ceil(playerPosUnit[1]+screenY/(2*self.unitSize))]
        # Calculate the fractional offset within the grid cell
        #offset_x = (playerPosUnit[0] - math.floor(playerPosUnit[0])) * self.unitSize
        offset_x = (playerPosUnit[0] - topLeftIndex[0] - (screenX / (2*self.unitSize))) * self.unitSize
        offset_y = (playerPosUnit[1] - topLeftIndex[1] - (screenY / (2*self.unitSize))) * self.unitSize
        for j in range(topLeftIndex[1], bottomRightIndex[1]):
            for i in range(topLeftIndex[0], bottomRightIndex[0]):
                if i >= 0 and i < self.worldSize[0] and j >= 0 and j < self.worldSize[1]:
                    if self.worldGrid[i][j] != None:
                        draw_x = (i - topLeftIndex[0]) * self.unitSize - offset_x
                        draw_y = (j - topLeftIndex[1]) * self.unitSize - offset_y
                        worldSurface.blit(self.sprites[self.worldGrid[i][j]], (draw_x, draw_y))
        return worldSurface
    
    def move_player(self, playerObj, dt):
        return [self.playerPosUnit[0] + playerObj.xDir * dt * playerObj.movementSpeed, self.playerPosUnit[1] + playerObj.yDir * dt * playerObj.movementSpeed]
    
    # Function that takes a probability and changes worldGrid one cell to another type.
    def change_world(self, probability, fromType, toType):
        for i in range(len(self.worldGrid)):
            for j in range(len(self.worldGrid[i])):
                if self.worldGrid[i][j] == fromType and random.random() < probability:
                    self.worldGrid[i][j] = toType
    
    # Generate a world using Perlin noise
    def generate_game_world(self, x, y, scale, seed=0):
        np.random.seed(seed)  # Set the seed for consistent random numbers
        world = np.zeros((x, y))  # Initialize the world as a 2D array of zeros
        for i in range(x):
            for j in range(y):
                # Generate smooth noise values between 0 and 1
                world[i][j] = noise.snoise2(i/scale , j/scale, octaves=8, persistence=0.9, lacunarity=0.3, repeatx=x, repeaty=y)
        return world
    
    def transform_to_indexes(self):
        indexes = np.zeros_like(self.worldGrid, dtype=np.int32)
        for i in range(self.worldGrid.shape[0]):
            for j in range(self.worldGrid.shape[1]):
                cell_value = self.worldGrid[i, j]
                for index, threshold in enumerate(self.tileTresholds):
                    if cell_value < threshold:
                        indexes[i, j] = index
                        break            
        return indexes