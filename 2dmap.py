from testingClasses import *
import random

# GLOBAL RULE: (X, Y)

locationIDCounter = 0

def nextLocID():
    global locationIDCounter
    locationIDCounter += 1
    return locationIDCounter


initialPos = Container(locID = nextLocID(), neighbors = [], structure = "default", name="initial", coordinates = (0, 0))

player = Player()
player.location = initialPos.locID

locations = {initialPos.locID : initialPos} # locations defined by locIDs
map = {initialPos.coordinates : initialPos.locID} # locIDs defined by coords
livingBranches = [initialPos]

neighborPositions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
neighborDirections = ["north", "east", "south", "west"]

def findNeighborsForPos(pos):
    emptyNeighbors = []
    for position in neighborPositions:
        nextLocation = (pos.coordinates[0] + position[0], pos.coordinates[1] + position[1])
        if nextLocation not in map:
            emptyNeighbors.append((nextLocation, pos, position)) # append all potential new neighbors to emptyNeighbors
    return emptyNeighbors

def branchExpander(limit):
    global locations
    global livingBranches
    roomsGenerated = 0
    counter = 0
    while roomsGenerated < limit:
        counter += 1

        emptyNeighbors = []
        for branch in livingBranches: # find all potential new places for future neighbors
            emptyNeighbors.extend(findNeighborsForPos(branch))

        for neighbor in emptyNeighbors: # go through and figure out which ones are viable
            nextLocation = neighbor[0]
            branch = neighbor[1]
            branchDir = neighbor[2]
            if neighbor[0] not in map:
                #print(f"got one at {neighbor[0]}")
                roomsGenerated +=1
                #print(f"neighbor : {neighbor}")
                coordDiff = (nextLocation[0] - branch.coordinates[0], nextLocation[1] - branch.coordinates[1])
                #print(f"coordDiff: {coordDiff}")
                #print(f"branchDir : {branchDir}")
                if coordDiff != branchDir:
                    print("\n\n\n###############\nFAILED THIS TIME\n#################\n\n\n")
                    exit()

                # use branchDir rather than coordDiff, considering they appear equal

                
                    


branchExpander(50)