# Import modules
import pygame as pg
import os

# Define colors
black = (0, 0, 0)

# Function to Initialize pygame
def initalize_pygame(gameName):
    pg.init()
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    pg.display.set_caption(gameName)
    pg.mouse.set_visible(False)
    return screen, screen.get_width(), screen.get_height()

# Function to draw the game
def draw_game(screen, screenX, screenY, worldSurface, npcSurface, playerSurface, uiSurface):

    # Clear the screen
    screen.fill(black)

    # Draw the world

    screen.blit(worldSurface, (0, 0))

    # Draw NPCs
    screen.blit(npcSurface, (0, 0))

    # Draw the player
    screen.blit(playerSurface, (screenX/2, screenY/2))

    # Draw the UI
    screen.blit(uiSurface, (0, 0))
    draw_cursor(screen, pg.mouse.get_pos())
    # Update the screen
    pg.display.update()

def make_surfaces(screenX, screenY):
    worldSurface = pg.Surface((screenX, screenY),pg.SRCALPHA)
    npcSurface = pg.Surface((screenX, screenY),pg.SRCALPHA)
    playerSurface = pg.Surface((screenX, screenY),pg.SRCALPHA)
    uiSurface = pg.Surface((screenX, screenY),pg.SRCALPHA)
    return worldSurface, npcSurface, playerSurface, uiSurface

# Helper function to load sprites from a directory
def load_sprites(directory):
    sprites = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".png"):
            image_path = os.path.join(directory, file_name)
            sprite = pg.image.load(image_path).convert_alpha()
            sprites.append(sprite)
    return sprites

def draw_rect(surface, color, x, y, width, height):
    pg.draw.rect(surface, color, (x-width/2, y-height/2, width, height))

def draw_cursor(surface, mousePos):
    # Draw a circle on the cursor
    pg.draw.circle(surface, (55,255,55), mousePos, 5)