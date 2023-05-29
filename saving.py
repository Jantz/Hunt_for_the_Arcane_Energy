# Handle save file creation and loading.

# Import modules
import os, pickle, time

# Check if at least one save file exists.
def save_exists():
    for file_name in os.listdir("savedata"):
        if file_name.endswith(".pickle"):
            return True
    return False

# Create a new save file with the player's name and current time.
def create_save_file(player_name, data):
    save_file = open("savedata/" + player_name + "_" + time.strftime("%Y%m%d-%H%M%S") + ".pickle", "wb")
    pickle.dump(data, save_file)
    save_file.close()

# Load a random save file.
def load_save_file():
    for file_name in os.listdir("savedata"):
        if file_name.endswith(".pickle"):
            save_file = open("savedata/" + file_name, "rb")
            player = pickle.load(save_file)
            save_file.close()
            return player
    return None