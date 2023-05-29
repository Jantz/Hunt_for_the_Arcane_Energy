# Using pygame get user input.

# Import modules
import pygame as pg

# Get user input
def get_input(inputs):
    # Keyboard input
    keys = pg.key.get_pressed()
    # Mouse input
    mousePos = pg.mouse.get_pos()
    mouseKeys = pg.mouse.get_pressed()
    clicks = [0,0,0]
    # Check if this is the first time the function is being called.
    if inputs != None:
        # Get mouse click impulse
        clicks[0] = get_rising_edge(inputs, "mouseKeys", 0, mouseKeys[0])
    inputs = {"keys": keys, "mousePos": mousePos, "mouseKeys": mouseKeys, "clicks": clicks}
    return inputs

def player_quit():
    # Detect if the user has quit the game.
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            return False
    return True

# Helper function for getting to get rising edge of a input.
def get_rising_edge(inputs, type, index, subject):
    if not inputs[type][index] and subject:
        return 1
    else:
        return 0