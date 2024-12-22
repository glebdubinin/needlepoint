import json

makingRooms = True
makingStructures = True
roomValid = False
inputValid = False
gamedata = {
    "locations" : {},
    "items" : {}
}

def checkInput(query):
    certain = None
    while certain != "y":
        result = input(query)
        certain = input("Are you sure? (y/n)").lower().strip()
    return result

while makingStructures:

    emptyRoom = {
        "neighbours" : None,
        "undeadMin" : None,
        "undeadMax" : None
    }

    roomName = None
    roomNeighbours = None
    undeadMin = None
    undeadMax = None

    roomStructure = input("Next structure to create: ('None' to exit) ")
    if roomStructure == "None":
        makingRooms = False
        makingStructures = False
    else:
        gamedata["locations"][roomStructure] = {}

    while makingRooms:
        
        if roomName is None:
            print(" === Creating a new room === ")
            roomName = input("Room name: ")
        else:
            print(f" === Editing {roomName} === ")
        if roomNeighbours is None:
            roomNeighbours = checkInput("Room neighbours: ") + " "
        #if undeadMin is None:
        #    roomNeighbours = checkInput("Room neighbours: ")
        #if roomNeighbours is None:
        #    roomNeighbours = checkInput("Room neighbours: ")

        roomNeighboursList = []
        placeholder = ""
        for char in roomNeighbours:
            if char == " ":
                roomNeighboursList.append(placeholder)
                print(f"placeholder: {placeholder}")
                print(f"gamedata locations roomstructure: {gamedata['locations'][roomStructure]}")
                if placeholder not in gamedata["locations"][roomStructure]:
                    gamedata["locations"][roomStructure][placeholder] = emptyRoom

                placeholder = ""
            else:
                placeholder += char

        print("\nTo recap:")
        print(f"room structure: {roomStructure}")
        print(f"room name: {roomName}")
        print(f"room neighbours: {roomNeighboursList}")

        valid = checkInput("Sound right? (y/n)").lower().strip()
        if valid == "y":
            roomConf = True
        else:
            print("What's wrong? ")
            print("(1) roomName")
            print("(2) roomNeighbours")
            validInputs = {"1", "2"}
            while not inputValid:
                varToChange = input("What do you need changed? ")
                if varToChange in validInputs:
                    inputValid = True
            if varToChange == "1":
                roomName = None
            elif varToChange == "2":
                roomNeighbours = None
        
        if roomConf:
            gamedata["locations"][roomStructure][roomName] = {
                "name" : roomName,
                "neighbours" : roomNeighboursList
            }
        
        usermove = input("Want to make another room? (y/n) ").lower().strip()
        if usermove == "n":
            usermove = input(f"Are you done with {roomStructure}? (y/n) ").lower().strip()
            if usermove == "y":
                makingRooms = False
            else:
                print("Rooms created so far: ")
                for room in gamedata["locations"][roomStructure]:
                    roomObj = gamedata['locations'][roomStructure][room]
                    #print(roomObj)
                    print(f" - {room}, neighbours: {roomObj['neighbours']}")
                usermove = input("Edit one? ")
                if usermove in gamedata["locations"][roomStructure]:
                    roomName = usermove
                    roomNeighbours = None
        else:
            roomName = None
            roomNeighbours = None

with open("gamedatanew.json", "w+") as f:
    json.dump(gamedata, f, indent=2)

