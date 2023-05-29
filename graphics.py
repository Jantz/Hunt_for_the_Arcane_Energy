# Import modules
import pygame as pg
import os

# Define colors
black = (0, 0, 0)

# Define fonts
def load_fonts(screenX):
    font128 = pg.font.Font("assets/fonts/cutesyserif.ttf", int(round(screenX/15)))
    font64 = pg.font.Font("assets/fonts/cutesyserif.ttf", int(round(screenX/30)))
    font32 = pg.font.Font("assets/fonts/cutesyserif.ttf", int(round(screenX/60)))
    # Return fonts in a dictionary
    return {"128": font128, "64": font64, "32": font32}

# Function to Initialize pygame
def initalize_pygame(gameName):
    pg.init()
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    pg.display.set_caption(gameName)
    pg.mouse.set_visible(False)
    return screen, screen.get_width(), screen.get_height()

# Function to draw the game
def draw_game(screen, screenX, screenY, worldSurface, npcSurface, playerSurface, uiSurface, dt, font):

    # Clear the screen
    screen.fill(black)

    # Draw the world

    screen.blit(worldSurface, (0, 0))

    # Draw NPCs
    screen.blit(npcSurface, (0, 0))

    # Draw the player
    screen.blit(playerSurface, (0, 0))

    # Draw the UI
    screen.blit(uiSurface, (0, 0))
    draw_cursor(screen, pg.mouse.get_pos())
    display_fps(screen, font, dt)

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

def draw_rect(surface, color, x, y, width, height): # Anchor point is the center of the rectangle
    pg.draw.rect(surface, color, (x-width/2, y-height/2, width, height))

def draw_cursor(surface, mousePos):
    # Draw a circle on the cursor
    pg.draw.circle(surface, (55,255,55), mousePos, 5)

# Function for calculating fps from dt and displaying it on the screen
def display_fps(screen, font, dt):
    fps = int(round(1/dt))
    fps_text = font.render(str(fps), True, pg.Color("coral"))
    screen.blit(fps_text, (16, 16))

# Load player sprites
        
# Load player sprites
def load_player_idle():
    return load_sprites("assets/player/idle")

# Function to blit the player to the player surface.
def blit_player(playerSurface, screenX, screenY, playerObj, sprite):
    if playerObj.isMoving:   # Moving
        playerSurface.blit(sprite[0], (screenX/2 - sprite[0].get_width()/2, screenY/2 - sprite[0].get_height()/2))
        return playerSurface
    if playerObj.isRunning:  # Running
        playerSurface.blit(sprite[0], (screenX/2 - sprite[0].get_width()/2, screenY/2 - sprite[0].get_height()/2))
        return playerSurface
    if not playerObj.isMoving and not playerObj.isRunning:   # Idle
        playerSurface.blit(sprite[0], (screenX/2 - sprite[0].get_width()/2, screenY/2 - sprite[0].get_height()/2))
        # Draw a dot on the player position
        pg.draw.circle(playerSurface, (255,0,0), (screenX/2, screenY/2), 2)
        return playerSurface