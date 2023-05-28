# Import modules
import graphics

# Define the player class.
class Player():
    def __init__(self, name="Player_name", playerColor=(255, 255, 255)):

        # Customization
        self.name = name
        self.playerColor = playerColor

        # Stats
        self.health = 100
        self.maxHealth = 100
        self.stamina = 100
        self.maxStamina = 100
        self.energy = 0

        # Levels
        self.charLevel = 1
        self.healthLevel = 1
        self.staminaLevel = 1
        self.defenseLevel = 1
        self.meleeLevel = 1
        self.rangedLevel = 1
        self.magicLevel = 1
        self.agilityLevel = 1
        self.luckLevel = 1

        # Inventory
        self.inventorySize = 10
        self.inventory = [None for _ in range(self.inventorySize)]

        # Equipment
        self.rightHand = None
        self.leftHand = None
        self.head = None
        self.chest = None
        self.legs = None
        self.feet = None

        # States
        self.isAlive = True
        self.isBlocking = False
        self.isAttacking = False
        self.isMoving = False
        self.isRunning = False

        # Load sprites
        self.sprites = graphics.load_sprites("assets/player/idle")