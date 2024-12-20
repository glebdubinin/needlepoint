from classes import *
import time
import math
import os
import random

# variable initialisatoin
# dictionary containing sets that are lists of all possible phrasings of a particular command that could be run
commands = {"go" : {"go", "goto", "move", "moveto"},
            "grab" : {"grab", "pickup", "take", "yoink", "snatch", "snag", "grasp", "snatch"},
            "drop" : {"drop", "put down", "leave", "leave behind"},
            "use" : {"use", "apply", "utilise", "check", }}
gameTime = 0

# functions


def checkTime(thingUsed, gameTime):
    print(f"You look at your {thingUsed}.")
    print(f"It's {gameTime}") #find some way to parse time into a more readable, usable form.


def parse(): # take user input and turn it into a list of component words
    usermove = input("What do you do next? ")+" "

    components = []
    word = ""
    # generate a list called "components" that has all the "words" (parts) of the user's last instruction
    for char in usermove:
        if char == " ":
            components.append(word)
            word = ""
        else:
            word += char
    try:
        if components[0] not in commands:
            print("that ain't a command, retard")
    except IndexError:
        pass
    return components


def goto(placefrom, placeto): # moving between rooms
    for neighbor in placefrom.neighbors:
        if placeto == neighbor.name:
            player.room = neighbor

def use(commands):
    # first, check if theres one or two objects being "used" at the moment.
    # then, check if the verb is applicable.
    # if it's not applicable, suggest one that is more uesful for the given object(s)
    # if it is applicable, then call the appropriate object's use function if possible.
    pass

def actOnCommands(components):
    if components[0] in commands["go"]: # goto command
        gameTime += 1
        goto(player.room, components[1])
    elif components[0] in commands["use"]:
        #gameTime is managed within useFunc
        #useFunc(components)
        pass




# initialisation
introRoom = Room(name="bedroom")
introKitchen = Room(name="kitchen")
introRoom.neighbors.add(introKitchen)
introKitchen.neighbors.add(introRoom)
introRoom.objects.add(Object(name = "watch", use=checkTime("watch", gameTime)))

usermove = input("What should we call you?")

player = Player(name=usermove, room=introRoom)

# main game loop

while True:
    result = parse()
    actOnCommands(result)


