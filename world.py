# Define the world class.
class World():
    def __init__(self):

        # Define the world grid.
        self.worldGrid = [[None for _ in range(100)] for _ in range(100)]
        self.unitSize = 64

        # Define the world objects.
        self.npcs = []
        self.player = None

        
        self.playerPos = [len(self.worldGrid)/2, len(self.worldGrid[0])/2]
