class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room


class Room():
    def __init__(self, name):
        self.name = name
        self.neighbors = set()
        self.objects = set()

        """
            short description is used for when you're re-entering a room that's been visited before
            long description is for new space discoveries
            long desc is stored as an array to allow for the description to be stretched over several lines
        """

        self.shortDescription = ""
        self.longDescription = []

class Object():
    def __init__(self, name, use):
        self.name = name
        rarity = ""
        type = ""
        usesRemaining = 0
        use = None # variable that holds the function that will later refer to how the objcet is used
        howUsedPhrasing = ""

        """ 
            potential properties:
            rarity: "common", "uncommon", "rare", "epic", "legendary"
            type: "healing", "food", "clothing", "weapon"
            usesRemaining: integer value for how many times an object can be "used"
            usePhrasing: the words that describe how an object is used
        """

class Container():
    def __init__(self):
        self.objects = []
