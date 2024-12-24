from testingClasses import *
from datetime import date, datetime
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
roomCount = 50

def nextLocID():
    global locationIDCounter
    locationIDCounter += 1
    return locationIDCounter

livingroom = Container(locID = nextLocID(), neighbors=[], structure="house",  name = "livingroom")
bedroom = Container(locID = nextLocID(), neighbors=[], structure="house", name = "bedroom")

livingroom.neighbors.append(copy.deepcopy(bedroom.locID))
bedroom.neighbors.append(copy.deepcopy(livingroom.locID))

locations = {livingroom.locID : livingroom, bedroom.locID : bedroom}

player = Player()
player.location = bedroom.locID

rooms = set()
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
        neighbors.append(id)
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
                            "name" : locations[location].name} for location in locations
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
    for structure in gamedata["structures"]:
            for building in gamedata["structures"][structure]:
                newLoc = gamedata["structures"][structure][building]
                print(f"building: {building}")
                newLocObj = ContainerFormat(neighbors = newLoc["neighbors"],
                                        structure=structure,
                                        isExit=newLoc["isExit"],
                                        undeadRange=(newLoc["undeadmin"], newLoc["undeadmax"]),
                                        items=newLoc["items"],
                                        name=building)
                print(f"neighbors   : {newLoc['neighbors']}")
                print(f"structure   : {structure}")
                print(f"isExit      : {newLoc['isExit']}")
                print(f"undeadRange : {newLocObj.undeadRange}")
                print(f"items       : {newLoc['items']}")
                print(f"name        : {building}")
                #print(dir(newLocObj))
                rooms.add(newLocObj)
    

    #YET TO CREATE ITEM IMPORTS

def generateWorld(seed):
    random.seed(seed)
    global locations
    global rooms
    roomsList = list(rooms)
    global player
    global items # YET TO ADD
    global roomCount
    randomRoom = random.choice(roomsList)
    print(f"randomRoom : {randomRoom}")
    initialRoom = Container(locID = nextLocID(),
                            neighbors = [],
                            structure = randomRoom.structure,
                            name = randomRoom.name)
    player.location = initialRoom.locID
    locations[initialRoom.locID] = initialRoom
    finalisedLocations = set()
    mutableLocations = [initialRoom]
    while len(locations) < roomCount:
        for loc in mutableLocations:
            if len(locations) < roomCount:
                print(f"roomCount : {roomCount}")
                print(f"len(locations) : {len(locations)}")
                possibleRooms = copy.deepcopy(rooms)

                for room in rooms: # remove all unsuitable room types
                    if room.name == loc.name: # remove rooms of the same type
                        try:
                            possibleRooms.remove(room)
                        except KeyError:
                            pass

                    for neighbour in loc.neighbors: # or of the neighbour's type
                        #print(f"neighbour : {neighbour}")
                        if room.name == locations[neighbour].name:
                            try:
                                possibleRooms.remove(room)
                            except KeyError:
                                pass

                if len(possibleRooms) != 0:

                    numToGen = random.randint(1, len(possibleRooms))

                    possibleRoomsList = list(possibleRooms)

                    for i in range(numToGen):

                        newRoomType = random.choice(possibleRoomsList)
                        newLoc = Container(locID = nextLocID(),
                                        neighbors=[loc.locID],
                                        structure=newRoomType.structure,
                                        isExit = newRoomType.isExit,
                                        undeadCount = random.randint(newRoomType.undeadRange[0], newRoomType.undeadRange[1]),
                                        name = newRoomType.name)
                        locations[newLoc.locID] = newLoc
                        mutableLocations.append(newLoc)
                        loc.neighbors.append(newLoc.locID)

                #print(f"newMutableLocations : {mutableLocations}")
                #print(f"loc                 : {loc}")
                mutableLocations.remove(loc)
                finalisedLocations.add(loc)


            

                
            
        

        
        







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
        usermove = getInput("What would you like to do next?  ")
        #print(usermove)

        if usermove[0] in commands["go"]:
            goto(placeto=usermove[1], player=player)
            #for neighbor in getRoomNeighbors(player.location):
            #    if usermove[1] == neighbor.name:
            #        player.location = neighbor
            #        print("You have moved to the " + neighbor.name)

        elif usermove[0] in commands["quit"]:
            playing = False

        elif usermove[0] in commands["look"]:
            print(locations)
            print(f"You are in the {locations[player.location].name}")
            #print(f"locations: {locations}")
            print("You can go to:")
            for neighbor in getRoomNeighborIDs(player.location):
                #print(f"neighbor : {neighbor}")
                #print(f"player.location : {player.location}")
                print(f" - {locations[neighbor].name}")
            if locations[player.location].items is not {}: 
                print("And you can see:")
                for item in locations[player.location].items:
                    print(f" - {item.name}")

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