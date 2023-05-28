# Import modules
import pygame as pg
import os

# Define colors
black = (0, 0, 0)

# Function to Initialize pygame
def initalize_pygame(screenWidth, screenHeight, gameName):
    pg.init()
    screen = pg.display.set_mode((screenWidth, screenHeight), pg.FULLSCREEN)
    pg.display.set_caption(gameName)
    pg.mouse.set_visible(False)
    return screen

# Function to draw the game
def draw_game(screen, world, NPCs, player, UI):

    # Clear the screen
    screen.fill(black)

    # Draw the world
    screen.pg.blit(world.draw(screen))

    # Draw NPCs
    for npc in world.npcs:

    # Draw the player
    player.draw(screen)

    # Draw the UI


    # Update the screen
    pg.display.update()

# Helper function to load sprites from a directory
def load_sprites(directory):
    sprites = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".png"):
            image_path = os.path.join(directory, file_name)
            sprite = pg.image.load(image_path).convert_alpha()
            sprites.append(sprite)
    return sprites
