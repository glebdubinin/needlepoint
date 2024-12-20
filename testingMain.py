from testingClasses import *

## initialisation; delete later

livingroom = Container(parent = None, neighbors={}, name = "livingroom")
bedroom = Container(parent = None, neighbors={livingroom}, name = "bedroom")

livingroom.neighbors = {bedroom}

player = Player(location = bedroom)

commands = {"go" : {"go", "goto", "move", "moveto"},
            "grab" : {"grab", "pickup", "take", "yoink", "snatch", "snag", "grasp", "snatch"},
            "drop" : {"drop", "put down", "leave", "leave behind"},
            "use" : {"use", "apply", "utilise", "check"},
            "exit" : {"exit"},
            "look" : {"look", "seek", "search", "seek", "look", "gaze", "glance", "stare", "peer", "survey", "scan", "peruse"}}

def getInput(line):
    quote = input(line)+" "
    usermove = []
    placeholder = ""
    for i in range(len(quote)):
        if quote[i] == " ":
            usermove.append(placeholder)
            placeholder = ""
        else:
            placeholder += quote[i]
    try:
        commandValid = False
        for command in commands:
            if usermove[0] in commands[command]:
                commandValid = True
        if not commandValid:
            print("that ain't a command, retard")
    except IndexError:
        pass
    return usermove

def getRoomNeighbors(room):
    neighbors = []
    for i in room.neighbors:
        neighbors.append(i)
    return neighbors

def goto(placefrom, placeto):
    if placeto in getRoomNeighbors(placefrom):
        player.location = placeto


def main():
    print("executing def main")
    playing = True
    while playing:
        usermove = getInput("What would you like to do next?  ")
        #print(usermove)
        if usermove[0] in commands["go"]:
            for neighbor in getRoomNeighbors(player.location):
                if usermove[1] == neighbor.name:
                    player.location = neighbor
                    print("You have moved to the " + neighbor.name)
        elif usermove[0] == "exit":
            playing = False
        elif usermove[0] in commands["look"]:
            print(f"You are in the {player.location.name}")
            print("You can go to:")
            for neighbor in getRoomNeighbors(player.location):
                print(f" - {neighbor.name}")
            if player.location.items is not None: 
                print("And you can see:")
                for item in player.location.items:
                    print(f" - {item.name}")
        

main()