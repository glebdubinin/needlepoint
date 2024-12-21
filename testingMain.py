from testingClasses import *
from testingFunctions import *
from datetime import date

## initialisation; delete later

livingroom = Container(parent = None, neighbors={}, name = "livingroom")
bedroom = Container(parent = None, neighbors={livingroom}, name = "bedroom")

livingroom.neighbors = {bedroom}

player = Player()
player.location = bedroom

def main():
    print("executing def main")
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

        elif usermove[0] in commands["exit"]:
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

        elif usermove[0] in commands["grab"]:
            for item in player.location.items:
                if usermove[1] == item.name:
                    if item.space <= getFreeInvCapacity(player):
                        player.inventory.append(item)
                        player.location.items.remove(item)
                        print(f"You picked up {item.name}")
        
        elif usermove[0] == "save":
            gamedata = {
                "player" : {
                    "lastSaved" : str(date.today()),
                    "name" : player.name,
                    "location" : str(player.location)
                }
            }
            pass

main()