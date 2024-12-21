class Container():
    def __init__(self, parent, neighbors, name):
        self.locID = None
        self.parent = parent
        self.neighbors = neighbors # neighboring places and rooms that can be entered
        self.items = {}
        self.name = name

class Player():
    def __init__(self):
        self.name = ""
        self.location = None
        self.inventory = {}
        self.inventoryExpander = None # the object that defines the player's current inventory capacity

class Object():
    def __init__(self, name):
        self.name = name
        self.space = None