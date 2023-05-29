# This module is for defining the NPC class and all of its subclasses.

class NPC():
    def __init__(self, health, attack, speed, sprite):
        self.health = health
        self.attack = attack
        self.speed = speed
        self.sprite = sprite