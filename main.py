# This is the main file for "Hunt for the Arcane Energy" by Jantz.

### Importing modules ###
import pygame as pg
import time, random, pickle, io
import player, npc, world, ui, input, graphics, audio, saving

### Define classes ###

### Define functions ###

### Define global variables ###
gameName = "Hunt for the Arcane Energy"

# Game state tracking variables
lastTime = time.time()
gameIsRunning = True
onLaunchScreen = True

# Initialize pygame and create the screen.
screen, screenX, screenY = graphics.initalize_pygame(gameName)
emptySurface = pg.Surface((screenX, screenY),pg.SRCALPHA)

# Load fonts
fonts = graphics.load_fonts(screenX)

#Temporary objects
worldObj = world.World()
playerObj = None

# Generate the launch screen buttons
launchScreenButtons = ui.generate_launch_screen_buttons(screenX, screenY, fonts["64"])

# Load player sprites
player_idle = graphics.load_player_idle()

# Intitial values for variables
userInputs = None
dt = 0.01

### Main game loop ###
while gameIsRunning:

    # Get user input
    gameIsRunning = input.player_quit()
    userInputs = input.get_input(userInputs)

    # Generate the empty surfaces
    worldSurface, npcSurface, playerSurface, uiSurface = emptySurface, emptySurface, emptySurface, emptySurface

    # Check if the game is on the launch screen
    if onLaunchScreen:
        uiSurface = ui.blit_launch_screen(uiSurface, screenX, screenY, fonts["128"], launchScreenButtons)
        # Check if the user has clicked a button
        for button in launchScreenButtons:
            gameIsRunning, onLaunchScreen, playerObj = ui.launch_screen_button_is_clicked(button, userInputs, playerObj, onLaunchScreen)
    else:

        # Calculate delta time
        now = time.time()
        dt = now - lastTime
        lastTime = now

        # Update playerObj movement direction based on user input
        playerObj.xDir, playerObj.yDir, playerObj.isMoving, playerObj.isRunning = playerObj.update_movement_direction(userInputs)
        # Update worldObj.playerPosUnit when the player moves
        worldObj.playerPosUnit = worldObj.move_player(playerObj, dt)

        # Update surfaces
        worldSurface = worldObj.blit_world(worldSurface, worldObj.playerPosUnit, screenX, screenY)
        playerSurface = graphics.blit_player(playerSurface, screenX, screenY, playerObj, player_idle)
    # Draw game
    graphics.draw_game(screen, screenX, screenY, worldSurface, npcSurface, playerSurface, uiSurface, dt, fonts["32"])
pg.quit()