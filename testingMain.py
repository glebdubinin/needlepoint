from testingClasses import *

## initialisation; delete later

livingroom = Container(parent = None, children = {}, neighbors={}, name = "livingroom")
bedroom = Container(parent = None, children = {}, neighbors={livingroom}, name = "bedroom")

livingroom.neighbors = {bedroom}

player = Player(location = bedroom)

def getInput(line):
    quote = input(line)
    usermove = []
    placeholder = ""
    for i in range(len(quote)):
        if quote[i] == " ":
            usermove.append(placeholder)
            placeholder = ""
        else:
            placeholder += quote[i]
    return usermove

def getRoomNeighbors(room):
    neighbors = []
    for i in room.children:
        neighbors.append(i)
    for i in room.neighbors:
        neighbors.append(i)
    return neighbors

def main():
    print("executing def main")
    playing = True
    while playing:
        usermove = getInput("What would you like to do next?")
        if usermove[0] == "move":
            for neighbor in getRoomNeighbors(player.location):
                if usermove[1] == neighbor.name:
                    player.location = neighbor
                    print("You have moved to the " + neighbor.name)
        elif usermove[0] == "exit":
            playing = False