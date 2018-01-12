"""Begins the conversation with Ship."""
import json
import os
from bin import player

def cls():os.system('cls' if os.name=='nt' else 'clear')

def load_messages():
    """Loads messages"""
    messages = json.load(open("lib/messages.json"))
    return messages

def init():
    'Prep the game up.'
    cls()
    os.makedirs("sav", exist_ok=True)
    load_messages()

init()
you = player.Player()
cls()
print(you.get_greeting())
you.save()
