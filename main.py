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

### Define main function ###
print("Game launched.")
# Initialize pygame and create the screen.
screen, screenX, screenY = graphics.initalize_pygame(gameName)
worldSurface, npcSurface, playerSurface, uiSurface = graphics.make_surfaces(screenX, screenY)

# Define fonts
font128 = pg.font.Font("assets/fonts/cutesyserif.ttf", int(round(screenX/15)))
font64 = pg.font.Font("assets/fonts/cutesyserif.ttf", int(round(screenX/30)))
font32 = pg.font.Font("assets/fonts/cutesyserif.ttf", int(round(screenX/60)))

#Temporary objects
worldObj = world.World()
playerObj = player.Player()

# Generate the launch screen buttons
launchScreenButtons = ui.generate_launch_screen_buttons(screenX, screenY, font64)

### Main game loop ###
while gameIsRunning:

    # Get user input
    gameIsRunning = input.player_quit()
    userInputs = input.get_input()

    # Check if the game is on the launch screen
    if onLaunchScreen:
        uiSurface = ui.blit_launch_screen(uiSurface, screenX, screenY, font128, launchScreenButtons)
        # Check if the user has clicked a button
        for button in launchScreenButtons:
            gameIsRunning = ui.launch_screen_button_is_clicked(button, userInputs, playerObj)
    else:
        # Calculate delta time
        now = time.time()
        dt = now - lastTime
        lastTime = now
        # On launch, display the launch screen.
        # Update surfaces
        worldSurface = worldObj.blit_world(worldSurface, worldObj.playerPosUnit, screenX, screenY)
        # Draw game
    graphics.draw_game(screen, screenX, screenY, worldSurface, npcSurface, playerSurface, uiSurface)
pg.quit()
print("Main function finished.")