"""ship.py contains Ship class"""

class Ship(object):
    """the properties of a ship"""

    def __init__(self, name, sign, size):
        self.name = name
        self.sign = sign
        self.size = size
        self.hits = 0
        self.pos = []

    def __str__(self):
        """ prints like: Y Destroyer(3)"""
        return "%s %s(%d)" % (self.sign, self.name, self.size)

    def empty(self):
        """ empties the POS for a new POS """

        self.pos = []
