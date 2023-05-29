# Import modules
import pygame as pg

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
        self.fistDamage = 1

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

        # Movement
        self.xDir = 0
        self.yDir = 0
        self.movementSpeed = 1
    
    def update_movement_direction(self, userInputs):
        self.xDir = 0
        self.yDir = 0
        if userInputs["keys"][pg.K_w]:
            self.yDir -= 1
        if userInputs["keys"][pg.K_s]:
            self.yDir += 1
        if userInputs["keys"][pg.K_a]:
            self.xDir -= 1
        if userInputs["keys"][pg.K_d]:
            self.xDir += 1
        if self.xDir != 0 or self.yDir != 0:
            self.isMoving = True
        else:
            self.isMoving = False
        # Print movement direction
        #print(self.xDir, self.yDir)
        return self.xDir, self.yDir, self.isMoving, self.isRunning