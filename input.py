# Using pygame get user input.

# Import modules
import pygame as pg

# Get user input
def get_input():
    # Keyboard input
    keys = pg.key.get_pressed()
    # Mouse input
    mousePos = pg.mouse.get_pos()
    clicks = pg.mouse.get_pressed()
    inputs = {"keys": keys, "mousePos": mousePos, "clicks": clicks}
    return inputs

def player_quit():
    # Detect if the user has quit the game.
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            return False
    return True