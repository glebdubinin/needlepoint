class Container(): # the object used to create actual containers (rooms) in the game
    def __init__(self, locID, neighbors, structure, name, undeadCount=0, isExit=False, items={}):
        self.locID = locID
        self.neighbors = neighbors # neighboring places and rooms that can be entered
        self.structure = structure # string label for what building / structure category the container belongs do
        self.isExit = isExit
        self.undeadCount = undeadCount
        self.items = items
        self.name = name

class ContainerFormat(): # the object used to create templates of potential rooms that could be made
    def __init__(self, neighbors, structure, name, undeadRange=(0, 0), isExit=False, items={}):
        self.neighbors = neighbors # potential neighbours
        self.structure = structure # string label for what building / structure category the container belongs do
        self.isExit = isExit # whether or not the room could be used as an exit from the building
        self.undeadRange = undeadRange # must be corrected from two variables into one when importing
        self.items = items # potential items that the room could hold
        self.name = name

class Player():
    def __init__(self):
        self.name = ""
        self.location = None # ID of the player's location container
        self.inventory = {}
        self.inventoryExpander = None # the object that defines the player's current inventory capacity

class Object():
    def __init__(self, name):
        self.name = name
        self.space = None