commands = {"go" : {"go", "goto", "move", "moveto"},
            "grab" : {"grab", "pickup", "take", "yoink", "snatch", "snag", "grasp", "snatch"},
            "drop" : {"drop", "put down", "leave", "leave behind"},
            "use" : {"use", "apply", "utilise", "check"},
            "exit" : {"exit"},
            "look" : {"look", "seek", "search", "seek", "look", "gaze", "glance", "stare", "peer", "survey", "scan", "peruse"}}


inventoryCapacity = {"Nothing" : 2,
                     "Pockets" : 5,
                     "Backpack" : 30,
                     "Duffel Bag" : 80}


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

def goto(placeto, player):
    for neighbor in getRoomNeighbors(player.location):
        if placeto == neighbor.name:
            player.location = neighbor
            print(f"You went to the {neighbor.name}")
            return True
    return False

def getFreeInvCapacity(player):
    totalCapacity = inventoryCapacity[player.inventoryExpander]
    for item in player.inventory:
        totalCapacity -= item.space
    return totalCapacity