from testingClasses import *
from datetime import datetime
import json
import os
import copy
import random

#░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
#░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
#░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
#░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
#░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
#░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
#░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     


locationIDCounter = 0
tempInstanceIDCounter = 0
roomCount = 50

def nextLocID():
    global locationIDCounter
    locationIDCounter += 1
    return locationIDCounter

def nextTempID():
    global tempInstanceIDCounter
    tempInstanceIDCounter += 1
    return tempInstanceIDCounter

livingroom = Container(locID = nextLocID(), neighbors=[], structure="test",  name = "roomtypeA")
bedroom = Container(locID = nextLocID(), neighbors=[], structure="test", name = "roomtypeB")

livingroom.neighbors.append(copy.deepcopy(bedroom.locID))
bedroom.neighbors.append(copy.deepcopy(livingroom.locID))

locations = {livingroom.locID : livingroom, bedroom.locID : bedroom}
#locations = {}

player = Player()
player.location = bedroom.locID

rooms = {}  #  rooms = { "structure name" : { "room name" : { "traits" : "values" , ...} } }
templates = {} # templates = { "structure name" : { "room name" : { "room type" : "id", "neighbors" : ["id", "id"], "name" : "bruh" } } }
items = set()

commands = {"go" : {"go", "goto", "move", "moveto"},
            "grab" : {"grab", "pickup", "take", "yoink", "snatch", "snag", "grasp", "snatch"},
            "drop" : {"drop", "put down", "leave", "leave behind"},
            "use" : {"use", "apply", "utilise", "check"},
            "quit" : {"quit"},
            "look" : {"look", "seek", "search", "seek", "look", "gaze", "glance", "stare", "peer", "survey", "scan", "peruse"},
            "save" : {"save"},
            "load" : {"load"},
            "saves" : {"saves", "savestates"},
            "reload" : {"reload", "reboot", "restart"}}


inventoryCapacity = {"Nothing" : 2,
                     "Pockets" : 5,
                     "Backpack" : 30,
                     "Duffel Bag" : 80}

 
#░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░ 
#░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
#░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
#░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
#░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
#░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  

def initData(dataFile="gamedata"):
    try:
        with open(f"{dataFile}.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("No such game data exists. ")

def clear_screen():
    os.system('clear')

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

def getRoomNeighborIDs(roomID): #takes the id of a given room, returns a list of all the neighboring room ids
    neighbors = []
    for id in locations[roomID].neighbors:
        neighbors.append(int(id))
    #print(f"neighbors : {neighbors}")
    return neighbors


    neighbors = []
    for i in room.neighbors:
        neighbors.append(i)
    return neighbors

def goto(placeto, player): # take the id of the place that the player would like to go to, and the current player object. modify them accordingly if possible.
    #print(f"placeto: {placeto}")
    for neighbor in getRoomNeighborIDs(player.location):
        #print(f"neighbor: {neighbor}")
        if placeto == locations[neighbor].name:
            player.location = neighbor
            print(f"You went to the {locations[neighbor].name} ")
            return True
    print("You can't go there. ")
    return False

def getFreeInvCapacity(player):
    totalCapacity = inventoryCapacity[player.inventoryExpander]
    for item in player.inventory:
        totalCapacity -= item.space
    return totalCapacity

def lookAround(player, callType):
    global locations
    if callType == "direct":
        print(f"You are in the {locations[player.location].name}")
    print("\nYou can go to:")
    for neighbor in getRoomNeighborIDs(player.location):
        print(f" - {locations[neighbor].name}")
    if locations[player.location].items is not {}: 
        print("And you can see:")
        for item in locations[player.location].items:
            print(f" - {item.name}")

def saveGame(player, locations, usermove):
    now = datetime.now() #getting save date and time
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    gamedata = {
        "player" : {
            "lastSaved" : dt_string,
            "name" : player.name,
            "location" : str(player.location),
            "inventory" : player.inventory,
            "inventoryExpander" : player.inventoryExpander
        },
        "world" : {
            str(location) : {"locID" : location,
                            "neighbors" : locations[location].neighbors,
                            "items" : locations[location].items,
                            "structure" : locations[location].structure,
                            "name" : locations[location].name,
                            "isExit" : locations[location].isExit} for location in locations
        }
    }

    try:
        os.mkdir("saves")
    except FileExistsError:
        pass
    if len(usermove) == 1:
        with open(f"saves/savestate.json", "w+") as f:
            json.dump(gamedata, f, indent=2)
    else:
        with open(f"saves/savestate{usermove[1]}.json", "w+") as f:
            json.dump(gamedata, f, indent=2)

def loadGame(filename = ""):
    try:
        with open(f"saves/savestate{filename}.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("That save doesn't exist. ")

def importData(gamedata):
    global rooms
    global templates
    for structure in gamedata["structures"]:
        rooms[structure] = {}
        try:
            for room in gamedata["structures"][structure]["rooms"]:
                newRoom = gamedata["structures"][structure]["rooms"][room]
                newRoomObj = ContainerFormat(structure=structure,
                                        isExit=newRoom["isExit"],
                                        undeadRange=(newRoom["undeadmin"], newRoom["undeadmax"]),
                                        items=newRoom["items"],
                                        name=room)
                rooms[structure][newRoomObj.name] = newRoomObj

            templates[structure] = {}
            for template in gamedata["structures"][structure]["templates"]:
                newTemplate = gamedata["structures"][structure]["templates"][template]
                #print(f"newTemplate : {newTemplate}")

                templates[structure][template] = newTemplate
        except KeyError:
            pass


    #YET TO CREATE ITEM IMPORTS

def updateRoomLinks(locations):
    for locA in locations:
        for locB in locations: # for every combination of two possible locations,
            locationA = locations[locA]
            locationB = locations[locB]
            if locationA.instanceID == locationB.instanceID: # if they're from the same instance of a template,

                if locationB.templateID in locationA.intendedNeighbors: # and they're meant to be neighbors
                    #print(f"{locationA.locID} connected to {locationB.locID}")
                    if locationB.locID not in locationA.neighbors:
                        locationA.neighbors.append(locationB.locID)   # connect them.
                    if locationA.locID not in locationB.neighbors:
                        locationB.neighbors.append(locationA.locID)   # symmetrically.



def generateWorld(seed):
    random.seed(seed)
    global locations
    global rooms
    global player
    global items # YET TO ADD
    global templates

    while len(locations) < 50:
        randomStruct = random.choice(list(templates))
        randomTemplateObj = templates[randomStruct][random.choice(list(templates[randomStruct]))]

        currentTemplateID = nextTempID()
        for room in randomTemplateObj:
            roomName = randomTemplateObj[room]["name" if "name" in randomTemplateObj[room] else "type"]
            roomType = randomTemplateObj[room]["type"]
            newRoom = Container(locID = nextLocID(),
                                templateID = room,
                                instanceID = currentTemplateID,
                                neighbors=[],
                                isExit = rooms[randomStruct][roomType].isExit,
                                intendedNeighbors = randomTemplateObj[room]["neighbors"],
                                structure = randomStruct,
                                name = roomName)
            
            if rooms[randomStruct][roomType].isExit:
                exitRoom = newRoom.locID

            locations[newRoom.locID] = newRoom

        # identify the exitRoom of the last created template,
        # search through a list of all outside locations,
            # if empty make a new one
            # if no current streets have available non-designated street connections, make a new one
            # find a viable street and connect it to there.

    player.location = locations[random.choice(list(locations))].locID
    

    updateRoomLinks(locations)
    



#░▒▓██████████████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░  
#░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 


def main():
    ### initialisation
    global initRunBefore
    if not initRunBefore:

        #FIND GAMEDATA.JSON FILE
        initRunBefore = True
        gamedata = initData()

        #FORMATTING IMPORTED DATA
        importData(gamedata)
        
        generateWorld(random.randint(1, 1000))


    #print("executing def main")
    playing = True
    while playing:
        usermove = getInput("\n\nWhat would you like to do next?  ")
        clear_screen()
        print()
        #print(usermove)

        if usermove[0] in commands["go"]:
            goto(placeto=usermove[1], player=player)
            lookAround(player, "movement")
            
        elif usermove[0] in commands["quit"]:
            playing = False

        elif usermove[0] in commands["look"]:
            lookAround(player, "direct")

        elif usermove[0] in commands["grab"]:
            for item in locations[player.location].items:
                if usermove[1] == item.name:
                    if item.space <= getFreeInvCapacity(player):
                        player.inventory.append(item)
                        player.location.items.remove(item)
                        print(f"You picked up {item.name}")
        
        elif usermove[0] == "save":
            saveGame(player, locations, usermove)
            
        elif usermove[0] in commands["saves"]:
            print("all savestates:")
            files = os.listdir("saves/")
            for file in files:
                #
                # learn to read jsons, then get the "last saved" date and use it below
                #
                properFilename = file.replace('savestate', '').replace('.json', '')
                gamestate = loadGame(properFilename)
                if properFilename == "":
                    print(f" - untitled save from {gamestate['player']['lastSaved']}") #DATE AND TIME
                else:
                    print(f" - \"{properFilename}\" from {gamestate['player']['lastSaved']}") #DATE AND TIME

        elif usermove[0] in commands["load"]:
            if len(usermove) == 2:
                gamestate = loadGame(usermove[1])
            else:
                gamestate = loadGame()
            #print(gamestate)
            player.name = gamestate["player"]["name"]
            player.location = int(gamestate["player"]["location"])
            player.inventory = gamestate["player"]["inventory"]
            player.inventoryExpander = gamestate["player"]["inventoryExpander"]

            locations.clear()

            for location in gamestate["world"]:
                newLoc = Container(locID = int(location), 
                                   neighbors = gamestate["world"][location]["neighbors"], 
                                   structure = gamestate["world"][location]["structure"],
                                   name = gamestate["world"][location]["name"])
                newLoc.items = gamestate["world"][location]["items"]
                locations[int(location)] = newLoc

            if len(usermove) == 2:
                print(f"loaded save \"{usermove[1]}\"")
            else:
                print(f"loaded untitled save")
                
initRunBefore = False                

main()