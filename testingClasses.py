class Container():
    def __init__(self, parent, children, neighbors, name):
        self.parent = parent
        self.children = children
        self.neighbors = neighbors
        self.name = name

class Player():
    def __init__(self, location):
        self.location = location