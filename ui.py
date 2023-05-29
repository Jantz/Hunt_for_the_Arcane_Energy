# This file contains all the functions that are used to display the game's UI.
import graphics, saving, player

class rectButton():
    def __init__(self, x, y, width, height, font, text="Button_Text", color=(55,55,55), textColor=(255,255,255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.renderedText = font.render(self.text, True, textColor)
        self.color = color
        self.textColor = textColor


# Generate launch screen buttons.
def generate_launch_screen_buttons(screenX, screenY, font):
    launchScreenButtons = []
    launchScreenButtons.append(rectButton(screenX/2, 11/16*screenY, screenX/4, screenY/8, font, "New Game", (55,55,55), (255,255,255)))
    if saving.save_exists():
        launchScreenButtons.append(rectButton(screenX/2, screenY/2, screenX/4, screenY/8, font, "Load Game", (55,55,55), (255,255,255)))
    launchScreenButtons.append(rectButton(screenX/2, 14/16*screenY, screenX/4, screenY/8, font, "Quit Game", (55,55,55), (255,255,255)))
    return launchScreenButtons


# Lauch screen for the game.
def blit_launch_screen(uiSurface, screenX, screenY, font128, launchScreenButtons):
    uiSurface.blit(font128.render("Hunt for the Arcane Energy", True, (255,255,255)), (screenX/2 - font128.size("Hunt for the Arcane Energy")[0]/2, screenY/8))
    for button in launchScreenButtons:
        # Draw a rectangle with pygame.draw.rect()
        graphics.draw_rect(uiSurface, button.color, button.x, button.y, button.width, button.height)
        # Blit the text
        uiSurface.blit(button.renderedText, (button.x - button.renderedText.get_width()/2, button.y - button.renderedText.get_height()/2))
    return uiSurface

def launch_screen_button_is_clicked(button, inputs, playerObj, onLaunchScreen):
    if inputs["clicks"][0] and inputs["mousePos"][0] > button.x - button.width/2 and inputs["mousePos"][0] < button.x + button.width/2 and inputs["mousePos"][1] > button.y-button.height/2 and inputs["mousePos"][1] < button.y + button.height/2:
        if button.text == "New Game":
            playerObj = player.Player()
            saving.create_save_file(playerObj.name, playerObj)
            print("New game started.")
        if button.text == "Load Game":
            playerObj = saving.load_save_file()
            print("Game loaded.")
        if button.text == "Quit Game":
            print("Game quit.")
            return False, True, playerObj
        else:
            return True, False, playerObj
    else:
        return True, onLaunchScreen, playerObj