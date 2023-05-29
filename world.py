# Import modules
import graphics

# Define the world class.
class World():
    def __init__(self):

        # Define the world grid.
        self.worldSize = [100, 100]
        self.worldGrid = [[1 for _ in range(self.worldSize[0])] for _ in range(self.worldSize[1])]
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
        topLeftIndex = [round(playerPosUnit[0] - screenX/(2*self.unitSize)), round(playerPosUnit[1] - screenY/(2*self.unitSize))]
        bottomRightIndex = [round(playerPosUnit[0] + screenX/(2*self.unitSize)), round(playerPosUnit[1] + screenY/(2*self.unitSize))]
        for j in range(int(topLeftIndex[1]), int(bottomRightIndex[1])):
            for i in range(int(topLeftIndex[0]), int(bottomRightIndex[0])):
                if i >= 0 and i < len(self.worldGrid) and j >= 0 and j < len(self.worldGrid[0]):
                    if self.worldGrid[i][j] != None:
                        worldSurface.blit(self.sprites[0], ((i - topLeftIndex[0])*self.unitSize, (j - topLeftIndex[1])*self.unitSize))
                        #self.worldGrid[i][j]
        return worldSurface