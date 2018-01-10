"""Begins the conversation with Ship."""
from pathlib import Path
import json

def load_messages():
    """Loads messages"""
    messages = json.load(open("lib/messages.json"))
    return messages

def load_player():
    """Loads player data."""
    player_file = Path("sav/player.json")

    if not player_file.is_file():
        name = input("Hello, I am Ship. How may I refer to you?\n")

    print("Good Morning, " + name)
    return

load_player()
