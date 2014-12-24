"""board.py contains Board class and Ship class"""
from battleship.ship import Ship
from battleship.config import POINT


class Board(object):
    """has-a board dict and has-a fleet of Ship()s"""

    def __init__(self, rows=10, cols=10):
        """ creates a new board dataset: tuple as key dictionary
            with each coord as open/miss/occupied/hit/sunk status O X K @ k
            number of row/column maximum of 10 otherwise players.pick_pos will
            not work. initialises a fleet of ships
        """
        self.attack = {}
        self.defend = {}
        self.rows = rows
        self.cols = cols

        for row in range(rows):
            for col in range(cols):
                self.attack[(col, row)] = POINT['open']
                self.defend[(col, row)] = POINT['open']

        self.fleet = {
            'K': Ship('AircraftCarrier', 'K', 5),
            'T': Ship('Battleship', 'T', 4),
            'S': Ship('Submarine', 'S', 3),
            'Y': Ship('Destroyer', 'Y', 3),
            'P': Ship('PatrolBoat', 'P', 2)
            }

    def __str__(self, hide=False):
        """ converts board dict tuple as key into a list of list to display
            It will or will not display ships depending on the second parameter
        """
        str_attack = []  # will become a list containing att_row lists
        str_defend = []

        # the column reference row is being made first
        att_row = []
        def_row = []
        for col in 'ABCDEFGHIJ'[:self.cols]:
            att_row.append('  {}'.format(col))
            def_row.append('  {}'.format(col))
        att_row.insert(0, '+')
        def_row.insert(0, '+')

        # the col_ref row is appended to the str_board list
        str_attack.append('\t{}'.format(''.join(att_row)))
        str_defend.append('\t{}'.format(''.join(def_row)))

        # the dict will be organised into lists
        for row in range(self.rows):
            att_row = []
            def_row = []
            # for every col in the row the corresponding dict value is appended
            for col in range(self.cols):
                att_row.append(' {} '.format(self.attack[(col, row)]))
                def_row.append(' {} '.format(self.defend[(col, row)]))
            # appends each att_row along with each row's reference
            str_attack.append('\t{} {}'.format(row, ''.join(att_row)))
            str_defend.append('\t{} {}'.format(row, ''.join(def_row)))
        # inserts \n in between each item in str_board to print each
        # att_row on a new line
        return "\t*ATTACK\n" + '\n'.join(str_attack) + "\n\t*DEFEND\n" +\
            '\n'.join(str_defend)

    def place_ship(self, ship, pos):
        """ record the ship's pos and place a ship on the board
            ie. change O to S or P etc.
        """
        ship.pos = pos
        for coord in ship.pos:
            self.defend[coord] = ship.sign

    def remove_ship(self, ship):
        """ remove a ship ie. change K or T etc. back to O and
            delete the ship's pos
        """
        for coord in ship.pos:
            self.defend[coord] = POINT['open']
        ship.pos = []

    def remove_fleet(self):
        """ to remove a fleet of ships from the board and deletes
            each Ship's pos
        """
        for ship in self.fleet:
            self.remove_ship(self.fleet[ship])

    def record_defend_miss(self, coord):
        """changes the point representation of the coord to a miss"""

        self.defend[coord] = POINT['miss']

    def record_defend_hit(self, coord):
        """changes the point representation of the coord to a hit"""

        self.defend[coord] = POINT['hit']

    def record_defend_sunk(self, ship):
        """changes the point representation of the list of coords to a sunk"""

        for coord in ship.pos:
            self.defend[coord] = ship.sign.lower()

    def record_attack(self, coord, point):
        """ changes the point rep of the attacking board to point argument"""

        self.attack[coord] = point

    def record_attack_sunk(self, ship):
        """changes the point rep of attacking board to a sunk"""

        for coord in ship.pos:
            self.attack[coord] = ship.sign.lower()
