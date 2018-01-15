"""Begins the conversation with Ship."""
from sys import argv
import json
import os
from bin import player

def cls():os.system('cls' if os.name=='nt' else 'clear')

def load_messages():
    """Loads messages"""
    messages = json.load(open("lib/messages.json"))
    return messages

def handle_argv(args):
    for arg in args:
        if arg == "-reset":
            os.remove("sav/player.json")

def init():
    'Prep the game up.'
    cls()
    handle_argv(argv)
    load_messages()

init()
you = player.Player()
cls()
print(you.get_greeting())
you.save()
