'Represents the player and holds its state.'
from pathlib import Path
import json

class Player:
    'Player state'
    path = "sav/player.json"
    name = ""
    data = {}

    def __init__(self):
        player_file = Path(self.path)

        if player_file.is_file():
            with open(self.path) as json_data:
                self.data = json.load(json_data)
        else:
            self.data["name"] = input("Hello, I am Ship. How may I refer to you?\n")

        self.name = self.data["name"]


    def get_greeting(self):
        'Returns opening messages.'
        if self.name == '':
            return ""
        return "Good Morning, " + self.name

    def save(self):
        'Saves player data'
        with open(self.path, 'w') as outfile:
            json.dump(self.data, outfile)
