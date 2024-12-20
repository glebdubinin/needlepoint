# banner
print(20*"\n")
print(" |                                                                              |")
print("-O------------------------------------------------------------------------------O-")
print(" |                                                                              |")
print(" |    ███╗   ███╗  █████╗ ████████╗ █████╗ ██╗  ██╗ ██████╗  █████╗ ██╗  ██╗    |")
print(" |    ████╗ ████║ ██╔══██╗╚══██╔══╝██╔══██╗██║  ██║ ██╔══██╗██╔══██╗╚██╗██╔╝    |")
print(" |    ██╔████╔██║ ███████║   ██║   ██║  ╚═╝███████║ ██████╦╝██║  ██║ ╚███╔╝     |")
print(" |    ██║╚██╔╝██║ ██╔══██║   ██║   ██║  ██╗██╔══██║ ██╔══██╗██║  ██║ ██╔██╗     |")
print(" |    ██║ ╚═╝ ██║ ██║  ██║   ██║   ╚█████╔╝██║  ██║ ██████╦╝╚█████╔╝██╔╝╚██╗    |")
print(" |    ╚═╝     ╚═╝ ╚═╝  ╚═╝   ╚═╝    ╚════╝ ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝    |")
print(" |                                                                              |")
print("-O------------------------------------------------------------------------------O-")
print(" |                                                                              |")
print("\n\n\n\n\n")

# imports
import time
import math
import os
import random

# variables
playing = False
debugMode = False # dev mode skipping all the time delays
noPower = False # what dictates when the player realises that there's no power
dirtyWatah = False # does the player know they can't drink from taps
hasWatch = False # does the player have the watch?
hasClothes = False
usermove = "" # placeholder variable for all the input commands
inputValid = False 
location = "pregame" # the variable that dictates the game phase and the room the player is in
locationint = 0
container = "" #the name of the container the player is currently looking in (blank if they're in a room)
room = "playersbedroom" # the name of the room the player's currently in - less precise than location or container

# stats:
turns = 0 # the number of commands the player executed
roomsExplored = []
windowsSecured = 0
gutterProtected = False
easterEggs = 0

locationsVisited = [] # variable that holds all the rooms the player has been to, to ensure that the room description doesn't play every time the player goes there

inventory = []
invcapacity = 1
carrier = "hands"

# //NOTE: items 

playersbedroom = ["!closet!", "!bedside_table!", "closet//clothing", "lamp", "phone", "bedside_table//watch", "bedside_table//keys", "bedroom_door", "window"] # all the items in the players bedroom
livingroom = ["dog", "empty_water_bowl", "locked_sliding_door", "water_bottle"]
diningarea = ["napkins", "water_bottle", "google_home", "window"]
kitchen = ["sink", "hand_towels", "!fridge!", "fridge//water_bottle", "window"]
bathroom = ["toilet", "sink", "movable_shower_head", "towels", "window"]
entryway = ["stool", "flower_vase", "backpack", "front_door"]
parentsbedroom = ["!bedside_table!", "bedside_table//keys", "window"]
garage = ["!shelves!", "shelves//handbook", "shelves//remote", "shelves//keychain"]
backyard = ["garden_hose", "gutter", "locked_sliding_door"]
garden = ["empty_watering_can", "ladder"]
streets = []

doors = [["livingroom", "diningarea"], 
         ["diningarea", "kitchen"], 
         ["diningarea", "bathroom"], 
         ["livingroom", "entryway"], 
         ["entryway", "parentsbedroom"], 
         ["entryway", "garage"],
         ["backyard", "garden"]]


playersbedroomDescription = ["You look around the bedroom you've lived in for as long as you can remember.",
                             "There'a window for you to admire the flames rapidly approaching your house,",
                             "And a desk-full of old schoolwork and revision textbooks your parents insist that you keep for whatever reaosn.",
                             "You take one last longing look at all the plush toys around your pillow,",
                             "The posters on your walls of the comic book heroes you idolised,",
                             "The action figures you collected when you were young,",
                             "And you get back to your mission of saving the house."] # a list of the lines that are used for the description of the room

quickDescriptions = {
    "playersbedroom" : "There's a closet in the corner of the room, and a bedside table."
}

cantBeCarried = ["clothing", "watch", "dog", "google home", "napkins", "towels", "hand_towels", "bedroom_door", "backpack", "sink", "water", "garden_hose", "movable_shower_head", "toilet", "stool", "ladder", "window"]
movable = ["stool", "ladder"]
staticWaterSources = ["sink", "water", "garden_hose", "movable_shower_head"]

allWaterSources = ["sink", "water", "garden_hose", "movable_shower_head", "toilet", "water_bottle", "flower_vase"]

cloth = ["napkin", "hand_towel", "towel"]
wetCloth = ["wet_napkin", "wet_hand_towel", "wet_towel"]
waterContainers = ["empty_water_bottle", "empty_water_bowl", "empty_vase", "empty_watering_can"] # add hands
cleanWaterSources = ["water_bottle", "flower_vase"]
crafting = []

containerExceptions = ["shelves"]
house = [playersbedroom, livingroom, diningarea, kitchen, bathroom, entryway, parentsbedroom, garage, backyard, garden, streets]
housestr = ["playersbedroom", "livingroom", "diningarea", "kitchen", "bathroom", "entryway", "parentsbedroom", "garage", "backyard", "garden", "streets"]
# house array: 
# 0: player's bedroom
# 1: living room
# 2: diningarea
# 3: kitchen
# 4: bathroom
# 5: entryway
# 6: parentsbedroom
# 7: garage
# 8: backyard
# 9: garden
# 10: streets


# functions

def wait(delay, debugMode):
    if not(debugMode):
        time.sleep(delay)

def tellTheTime(time):
    pass

def printDescription(room, debugMode): # called when reading out the description of a room when it's entered for the first time or the "observe" command is used.
    for i in range(len(room)):
        print(room[i])

        #█▀█ █▀▀ █▀▄▀█ █▀█ █ █ █▀▀   █▀▄▀█ █▀▀
        #█▀▄ ██▄ █ ▀ █ █▄█ ▀▄▀ ██▄   █ ▀ █ ██▄
        if 1==2:
            wait(math.ceil(len(room[i]) / 35), debugMode)


# functions for specific items:


def usephone(noPower):
    if noPower:
        print("You already know there's no power, your phone doesn't work")
    else:
        input("You double tap on your phone screen")
        print("nothing.")
        input("you press the power button.")
        print("nothing.")
        input("You hold down the power button for a few seconds")
        print("1...")
        wait(1, debugMode)
        print("2...")
        wait(1, debugMode)
        print("3...")
        wait(3, debugMode)
        print("\n\n█████████████████████")
        print("███░              ███")
        print("███░              █████")
        print("███░              ███")
        print("█████████████████████\n\n")
        wait(2, debugMode)
        input("The power cut out overnight.")
    return True
# goes through the arrays of messages for the designated room line by line, prints one, and waits for a certain amount of time
# dependant on the length of the previous message before going to the next line.


def look(source=""):
    if location == room: #not in a container
        if source!="movement": #they manually used the look command
            print("\nYou're currently in the "+room)
            
        if sum(not '/' in h for h in house[locationint]) > 0: #there's a nonzero amount of objects / containers that are visible in the room
            print("You find:")

            for i in range(len(house[locationint])): # for every object in the room the player's in
                item = house[locationint][i]
                if not '/' in item:
                    print(" - "+item)
        else:
            print("You don't find anything.")

    else: #in a container
        if source!="movement":
            print("\nYou're currently in the "+room+", looking inside the "+container) # if the player's looking inside a container
        if sum(container+"//" in h for h in house[locationint]) > 0:
            print("You find: ")

            for i in range(len(house[locationint])):
                item = house[locationint][i]
                if container+"//" in item:
                    print(" - "+item.replace(container+"//", ""))
        else:
            print("You don't find anything")
    
    #print adjacent rooms
    if room == location:
        nearbyrooms = []

        for i in range(len(doors)):
            if location == doors[i][0]:
                nearbyrooms.append(doors[i][1])
            elif location == doors[i][1]:
                nearbyrooms.append(doors[i][0]) 

        print("\nFrom here, you can travel to:")
        for i in range(len(nearbyrooms)):
            print(" - "+nearbyrooms[i])
    



# pre-game intro section


#█▀█ █▀▀ █▀▄▀█ █▀█ █ █ █▀▀   █▀▄▀█ █▀▀
#█▀▄ ██▄ █ ▀ █ █▄█ ▀▄▀ ██▄   █ ▀ █ ██▄

# wait(2, debugMode)

while(not(playing)): # intro menu
      
    print(" [P] Play the game")
    print(" [H] How to play")
    print(" [A] Actual Bushfire Survival Info")
    print(" [X] Quit")

    usermove = input("What would you like to do?   ").lower()
    print("\n\n\n")
    if usermove == "p": #initialisation

        location = "initialising"
        playing = True
        print("fyi: a lot of the information in this game will be presented with timers, and some will need you to press enter to progress.")
        print("if nothing's happening for a while, you're either reading faster than I thought you would, or you just gotta hit enter.")
        input("(hit enter to progress (this warning won't appear all the time))")
        input("\n\n\nhave fun!\n\n")
        print(15*"\n\n")

    elif usermove == "h":
        # explain all the commands
        pass

    elif usermove == "a":
        # actual bushfire information sources
        pass

    elif usermove == "x":
        print("gochu. cya!")
        quit()

    elif usermove == "pp":
        # dev shortcut to skip the long asf intro cutscene when testing
        print("ok dev")
        location = "playersbedroom"
        debugMode = True
        playing = True

    else: 
        print("didn't catch that.")
        print("to select what you want to do, type the letter in square brackets")
        print("next to the option you want to choose.\n")
    
### the game.

while(playing):
 

    #█▀█ █▀▀ █▀▄▀█ █▀█ █ █ █▀▀   █▀▄▀█ █▀▀
    #█▀▄ ██▄ █ ▀ █ █▄█ ▀▄▀ ██▄   █ ▀ █ ██▄

    if location == "initialising" and 1==2:  # <- remove the 1==2
        # initialisation text that just describes the scene the first time the player's going thru it
        input("\nYou wake up in your room")
        input("It's in the middle of your school holidays, so you aren't stressed about getting up immediately.")
        input("Besides, your parents aren't gonna be home for another 2 days, so there's not gonna be anyone nagging you for sleeping in.")
        input("After a while of tossing and turning, your sheets start to turn chilly and you aren't particularly comfy.")
        input("You get up, and pull the blinds open.")
        input("Your stomach drops.")
        input("The warnings came true.")
        input("You're not prepared.")
        input("The bushes, trees and all the forest around the house you've lived your life in are alight.")
        input("And they're headed straight for you.")
        print("\n\n")

        location = "playersbedroom"
    elif location == "initialising":
        location = "playersbedroom"
    if location == "playersbedroom":
        if "playersbedroom" not in locationsVisited:
            printDescription(playersbedroomDescription, debugMode)
            print("\n\nYou curse yourself for your sleepiness and look around your room at everything you can use")
            print("You see a !closet! in the corner of the room, a [lamp] and your [phone] on your !bedside_table!.")
            locationsVisited.append("playersbedroom")
        if usermove.startswith("use"):
            usermove.replace("use ", "")

    usermove = input("\n\n\nWhat would you like to do?   ").lower()
    turns += 1

    # input processing 


    if usermove.startswith("use "):  # //NOTE: use command
        commWorked = False

        usermove = usermove.replace("use ", "")
        usermove = usermove.strip()
        if ' ' in usermove:
            things = usermove.split(' ')
            # interactions between two objects
            #spacereached = False
            #things = ["", ""]
            #for i in range(len(usermove)):
            #    if spacereached:
            #        things[1] += usermove[i]
            #    else:
            #        if usermove[i] == ' ':
            #            spacereached = True
            #        else:
            #            things[0] += usermove[i]
            # add automated crafting recipes in here

            for i in range(2):
                if things[i] in cloth and things[i] in inventory:
                    if things[i-1] in allWaterSources:
                        if things[i-1] in staticWaterSources:
                            if things[i-1] in house[locationint]:
                                print("You soak the "+things[i]+" with water from the "+things[i-1])
                                inventory.remove(things[i])
                                inventory.append("wet_"+things[i])
                                commWorked = True
                        elif things[i-1] in cleanWaterSources:
                            if things[i-1] in inventory: ## the water source is in the player's inventory
                                print("You soak the "+things[i]+" with water from the "+things[i-1])
                                inventory.remove(things[i])
                                inventory.append("wet_"+things[i])
                                inventory.remove(things[i-1])
                                inventory.append("empty_"+things[i-1])
                                commWorked = True
                            elif things[i-1] in house[locationint]: ## the water source is in the same room as the player
                                print("You soak the "+things[i]+" with water from the "+things[i-1])
                                inventory.remove(things[i])
                                inventory.append("wet_"+things[i])
                                house[locationint].remove(things[i-1])
                                house[locationint].append("empty_"+things[i-1])
                                commWorked = True
                            elif container+"//"+things[i-1] in house[locationint]: ## the water source is in the same container as the player
                                print("You soak the "+things[i]+" with water from the "+things[i-1])
                                inventory.remove(things[i])
                                inventory.append("wet_"+things[i])
                                house[locationint].remove(container+"//"+things[i-1])
                                house[locationint].append(container+"//empty_"+things[i-1])
                                commWorked = True
                        # is the water source 
                        
            for i in range(2): 
                if things[i] in waterContainers and things[i-1] in staticWaterSources:
                    if things[i] in inventory and things[i-1] in house[locationint]:
                        print("You refill the "+things[i].replace("_", " ")+" with water from the "+things[i-1].replace("_", " "))
                        inventory.remove(things[i])
                        inventory.append(things[i].replace("empty_", ""))
                        commWorked = True

            # custom crafting recipes:
            if "keys" in things and "bedroom_door" in things:
                if "bedroom_door" in house[locationint] and "keys" in inventory:
                    print("You unlock the door to your room.")
                    print("You can now head to the livingroom")
                    inventory.remove("keys")
                    playersbedroom.remove("bedroom_door")
                    doors.append(["playersbedroom", "livingroom"])
                    commWorked = True

            if "keys" in things and "locked_sliding_door" in things:
                if "locked_sliding_door" in house[locationint] and "keys" in inventory:
                    print("You unlock the sliding door between the backyard and the livingroom")
                    inventory.remove("keys")
                    livingroom.remove("locked_sliding_door")
                    backyard.remove("locked_sliding_door")
                    doors.append(["livingroom", "backyard"])
                    commWorked = True
            
            for i in range(2):
                if things[i] in cloth and things[i-1] == "gutter":
                    if "gutter" in house[locationint] and things[i] in inventory:
                        if "ladder" in house[locationint]:
                            print("You get up on the ladder and clog the gutter with a "+things[i])
                            inventory.remove(things[i])
                            backyard.remove("gutter")
                            backyard.append("clogged_gutter")
                            commWorked = True

            if "clogged_gutter" in things and "garden_hose" in things:
                if "clogged_gutter" in house[locationint] and "garden_hose" in house[locationint]:
                    print("You use the garden hose to fill the gutter with water")
                    backyard.remove("clogged_gutter")
                    backyard.append("flooded_gutter")
                    commWorked = True
                    gutterProtected = True
            
            if "keychain" in things and "front_door" in things:
                if "keychain" in inventory and "front_door" in house[locationint]:
                    print("You unlock the front door.")
                    doors.append("streets", house[locationint])
                    house[locationint].remove("frontdoor")
                    commWorked = True
                elif "keychain" in inventory and container+"//front_door" in house[locationint]:
                    print("You unlock the front door.")
                    doors.append(["streets", housestr[locationint]+"//"+container])
                    house[locationint].remove(container+"//front_door")
                    commWorked = True

            for i in range(2):
                if things[i] in wetCloth and (things[i-1] == "window" or things[i-1] == "front_door"):
                    if things[i-1] in house[locationint] and things[i] in inventory:
                        if things[i-1] == "window":
                            print("You hang up the "+things[i].replace("_", " ")+" over the window to protect it.")
                            inventory.remove(things[i])
                            house[locationint].remove("window")
                            house[locationint].append("protected_window")
                            commWorked = True
                            windowsSecured += 1
                        elif things[i-1] == "front_door":
                            print("You stuff the"+things[i].replace("_", " ")+"in the gap between the floor and the bottom of the door.")
                            inventory.remove(things[i])
                            house[locationint].remove("front_door")
                            house[locationint].append("protected_front_door")
                            commWorked = True

        else:
            if usermove in inventory: # is the item in the player's inventory?
                if usermove == "phone":
                    noPower = usephone(noPower)
                    commWorked = True
                if usermove == "remote":
                    print("You press a button on the remote, and the back garage door opens.")
                    print("You can now go to the backyard from the garage")
                    doors.append(["garage", "backyard"])
                    commWorked = True
                if usermove == "dog":
                    print("ಠಿ_ಠ")
                    easterEggs += 1
                    commWorked = True
                if usermove == "handbook":
                    print("hey, this isn't ready!")
                    easterEggs += 1
            else:
                if usermove in house[locationint]: # is the item in the room that the player's currently in?

                    if usermove == "lamp": # player's bedroom lamp
                        commWorked = True
                        if noPower:
                            print("You already know there's no power, it doesn't turn on.")
                        else:
                            print("you flick on the lamp. ")
                            wait(1, debugMode)
                            print("it doesn't turn on. ")
                            wait(0.5, debugMode)
                            print("you toggle the switch a couple more times, before settling with the fact that there's no power.")

                    if usermove == "phone":
                        noPower = usephone(noPower)
                        commWorked = True

                    if usermove == "watch":
                        print("you slide the watch straps around your wrist.")
                        commWorked = True

                    if usermove in staticWaterSources:
                        if not(dirtyWatah):
                            print("You try using the "+usermove+".")
                            print("There is some water that runs, but it's way too filthy for you to drink safely.")
                            print("You might be able to use it to protect the house, but definitely not to drink.")
                            dirtyWatah = True
                        else:
                            print("The water's nowhere near clean enough to drink.")
                            print("You can only use it to protect the house.")
                        commWorked = True

                elif container+"//"+usermove in house[locationint]:
                    if usermove == "watch":
                        print("you slide the watch on your wrist or whatever")
                        commWorked = True
        if not(commWorked):
            print("you can't do that")


    elif usermove.startswith("open "): # //NOTE: open command
        commWorked = False
        usermove = usermove.replace("open ", "")
        #if usermove in (house[locationint]).split('/', 1)[0]:
        #    container = usermove
        #    location = room+"//"+usermove
        for i in range(len(house[locationint])):
            if "!"+usermove+"!" == house[locationint][i]:
                if usermove not in containerExceptions:
                    container = usermove
                    location = room+"//"+usermove
                    print("You look inside the "+usermove)
                    look("movement")
                    commWorked = True
                    if usermove == "closet":
                        if hasClothes:
                            print("You're already wearing some clothing.")
                elif usermove in containerExceptions:
                    if usermove == "shelves":
                        if "stool" in house[locationint] or "ladder" in house[locationint]:
                            container = usermove
                            location = room+"//"+usermove
                            print("You step up on the stool and look at the top shelf")
                            look("movement")
                            commWorked = True
                        else:
                            print("You can't reach that high, you need something to stand on.")
        if not(commWorked):
            print("you can't do that")
                        

    elif usermove.startswith("grab "): # //NOTE: grab command
        commWorked = False

        usermove = usermove.replace("grab ", "")

        if usermove.replace("s", "") in cloth:
            usermove = usermove.replace("s", "") + "s"

        if usermove in house[locationint] or container+"//"+usermove in house[locationint]: # if the item is in the room or container the player is in
            if "//" not in usermove:
                if usermove == "clothing":
                    print("You replace your summer PJs with something better for the occasion.")
                    wait(1.5, debugMode)
                    print("You get some shorts and a shirt, both made from cotton.")
                    wait(1.5, debugMode)
                    print("You find that you have some extra pockets because of your shorts.")
                    wait(1.5, debugMode)
                    carrier = "pockets"
                    invcapacity = 3
                    hasClothes = True

                elif usermove == "backpack":
                    print("You grab the backpack that you used to use for school")
                    wait(1.5, debugMode)
                    print("You turn it over to empty it of all the random stuff you carry")
                    wait(1.5, debugMode)
                    print("And sling it around your back, with some extra space to carry things.")
                    carrier = "backpack"
                    invcapacity = 5

                elif usermove == "dog":
                    print("The dog is too heavy for you to carry anywhere.")
                    wait(1.5, debugMode)
                    print("You're too small to carry it outside it's cage,")
                    wait(1.5, debugMode)
                    print("And you can only take the cage five paces before having to rest.")

                elif usermove == "front_door":
                    print("that's actually pretty funny, I'll allow that")

                if len(inventory)-1 < invcapacity:

                    if usermove not in cantBeCarried:
                        inventory.append(usermove) #add the item to the players inventory

                    if usermove.replace("s", "") not in cloth:
                        if usermove in house[locationint]: #remove the item from the room
                            house[locationint].remove(usermove)
                        elif container+"//"+usermove in house[locationint]:
                            house[locationint].remove(container+"//"+usermove)

                    if usermove == "watch":
                        print("You slide the watch onto your wrist") 
                        hasWatch = True

                    elif usermove.replace("s", "") in cloth:
                        print("You grab one "+usermove.replace("s", "")+" from the stack.")
                        inventory.append(usermove.replace("s", ""))

                    else:
                        if not(usermove in cantBeCarried):
                            if carrier == "hands":
                                print("You take the "+usermove+". ")
                            else:
                                print("You put the "+usermove+" in your "+carrier+". ")
                else:
                    print("You're carrying too much to take the "+usermove+". ")
            else:
                print("What do you think you're trying to do? ") #if the player tries to take something that's in a container when they haven't opened it
        else:
            print("I couldn't find a "+usermove+" anywhere nearby. ") 


    elif usermove.startswith("drop "): # //NOTE: drop command
        usermove = usermove.replace("drop ", "")
        if usermove in inventory:
            if container == "":
                house[locationint].append(usermove)
                print("You drop the "+usermove)
            else:
                house[locationint].append(container+"//"+usermove)
                print("You drop the "+usermove+" inside the "+container)
            inventory.remove(usermove)
        else:
            print("You aren't carrying a "+usermove+". ")

    elif usermove.startswith("goto ") or usermove.startswith("move "): # //NOTE: move command
        moved = False
        usermove = usermove.replace("goto ", "")
        usermove = usermove.replace("move ", "")
        for i in range(len(doors)):
            if location in doors[i] and usermove in doors[i]:
                room = usermove
                location = room
                locationint = housestr.index(usermove)
                if not(moved):
                    print("You walk to the "+room)
                    look("movement")
                moved = True
                if room not in roomsExplored:
                    roomsExplored.append(room)
                if room == "streets":
                    for j in range(len(doors)):
                        if doors[j][0] == "streets" and doors[j][1] != "entryway":
                            easterEggs += 1
                            playing = False
                            print("Congratulations! You finished the game, with ending:")
                            print("How did we get here?")
                        elif doors[j][0] == "streets" and doors[j][1] == "entryway":
                            playing = False
                            print("Congratulations!")
                            print("You managed to get through the entire game!")
        if room != usermove:
            print("You can't move to the" +usermove+ " from the "+room)
        elif not(moved):
            print("you can't do that")
            
    elif usermove.startswith("drag "):
        commWorked = False
        usermove = usermove.replace("drag ", "")
        things = usermove.split(' ')
        #for i in range(len(usermove)):
        #    if spacereached:
        #        things[1] += usermove[i]
        #    else:
        #        if usermove[i] == ' ':
        #            spacereached = True
        #        else:
        #            things[0] += usermove[i]
                    
        nearbyrooms = []
        for i in range(len(doors)):
            if location == doors[i][0]:
                nearbyrooms.append(doors[i][1])
            elif location == doors[i][1]:
                nearbyrooms.append(doors[i][0]) 

        if things[0] in movable:
            if things[1] in nearbyrooms:
                house[locationint].remove(things[0])
                room = things[1]
                location = things[1]
                locationint = housestr.index(things[1])
                house[locationint].append(things[0])
                commWorked = True
                print("You drag the "+things[0]+" to the "+things[1])
                look("movement")
        if not(commWorked):
            print("you can't do that")
                


    elif usermove.startswith("look"):
        look()

    elif usermove == "close": # // NOTE: nonspecific commands
        container = ""
        location = room
        look("movement")

        
    elif usermove == "whereami" or usermove == "where" or usermove == "location" or usermove == "loc":
        if container != "":
            print("You are currently at "+room+", looking inside the "+container)
        else:
            print("You are currently at "+room) #fix this to display better versions of the location names


    elif usermove == "inv" or usermove == "inventory":
        if len(inventory) > 0:
            print("At the moment, you're carrying: ")
            for i in range(len(inventory)):
                print(inventory[i-1])
        else:
            print("You're not carrying anything")

    elif usermove.startswith("x"):
        print("gochu. cya!")
        quit()

    elif usermove == "pee yourself":
        print("You pee yourself.")
        easterEggs += 1

    else:

        placeholder = ""  # what happens if the command is not recognized
        spaceSeen = False
        usermove += " "
        for i in range(len(usermove)):
            if not(spaceSeen) and usermove[i] != ' ':
                placeholder += usermove[i]
            else:
                spaceSeen = True
        print("sorry, I don't recognize the command \""+placeholder+"\".")

print("\n\n\nPost Game Stats:")
print("Rooms Explored: "+str(roomsExplored))
print("Moves taken: "+str(turns))
print("Windows Secured: "+str(windowsSecured)+"/4")
if gutterProtected:
    print("Gutter Protected: Yes")
else:
    print("Gutter Protected: No")