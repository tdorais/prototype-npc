"""Begins the conversation with Ship."""
import json
import os
from bin import player

def load_messages():
    """Loads messages"""
    messages = json.load(open("lib/messages.json"))
    return messages

def cls():os.system('cls' if os.name=='nt' else 'clear')

cls()
you = player.Player()
cls()
print(you.get_greeting())
you.save()
