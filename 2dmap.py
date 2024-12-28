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
map = {initialPos.coordinates : initialPos} # locations defined by coords
livingBranches = [initialPos]

neighborPositions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def branchExpander(limit):
    global locations
    global livingBranches
    roomsGenerated = 0
    while roomsGenerated < limit:
        for branch in livingBranches:
            emptyNeighbors = []
            for position in neighborPositions:
                nextLocation = (branch.coordinates[0] + position[0], branch.coordinates[1] + position[1])
                if nextLocation not in map:
                    emptyNeighbors.append((nextLocation, branch, position))
        for neighbor in emptyNeighbors:
            print(f"got one at {neighbor[0]}")
            roomsGenerated +=1
        
branchExpander(50)