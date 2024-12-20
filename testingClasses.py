class Container():
    def __init__(self, parent, neighbors, name):
        self.parent = parent
        self.neighbors = neighbors # neighboring places and rooms that can be entered
        self.items = {}
        self.name = name

class Player():
    def __init__(self, location):
        self.location = location