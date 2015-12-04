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
        return "{} {}({})".format(self.sign, self.name, self.size)
