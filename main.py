# This is the main file for "Hunt for the Arcane Energy" by Jantz.

### Importing modules ###
import pygame as pg
import time, random, pickle, io
import player, npc, world, ui, input, graphics, audio, saving

### Define classes ###

### Define functions ###

### Define global variables ###
gameIsRunning = True
screenX = pg.display.Info().current_w
screenY = pg.display.Info().current_h
gameName = "Hunt for the Arcane Energy"
onLaunchScreen = True


### Define main function ###
def main():
    print("Game launched.")
    screen = graphics.initalize_pygame(screenX, screenY, gameName)
    while gameIsRunning:
        # On launch, display the launch screen.
        if onLaunchScreen:
            ui.launch_screen()
        graphics.draw(screen, player, world)
        graphics.draw_game(screen,)
    print("Main function finished.")

### Run main function ###
main()