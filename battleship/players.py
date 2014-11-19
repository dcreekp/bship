"""defines what a player can do"""
from random import choice
from battleship.board import Board
from battleship.config import PROMPT, POINT, FLEET
from battleship.ui import to_quit, clean, convert, prompt_coord

class Player(object):
    """defines the methods players can take and has-board"""

    def auto_hide_ships(self, ship, who=0):
        """ computer randomly selects head coord, then using _head2tail() gets
            a set of coords, from the given choice randomly selects a set and
            inputs these coordinates to the Ship's POS
        """
        self.occupied = {key for key in self.brd.board if
                                self.brd.board[key] in FLEET.keys()}

        while True:
            # gets a random coord out of the board
            head = choice(self.brd.board.keys())

            # gets a dict of possible coordinates
            h2t = self._head2tail(ship, head)

            try:
                # gets a random set of coordinates from the h2t dict
                pos = choice(h2t.values())
                break
            except IndexError: # but if the h2t dict has zero possible coords
                continue # will need to pick a new head coord

        # records the coordinate in the ship and board objects
        self.brd.place_ship(ship, pos)

        # what is printed depends on who hides it
        if who == 0:
            print PROMPT['comp_hidden'] % str(ship)
        elif who == 1:
            print PROMPT['player_hidden'] % str(ship)


    def _head2tail(self, ship, head):
        """ given the Ship, its head coord and size, returns a dict
            with each tail as key to the full set of coords for each
            possible ship direction
        """
        diff = 1 # difference between the head and the tail
        h2t_lst = [[head] for i in range(4)] # start with four possible tails

        while diff <= ship.size - 1:
            h2t_lst[0].append((head[0] - diff, head[1])) # tail down
            h2t_lst[1].append((head[0] + diff, head[1])) # tail up
            h2t_lst[2].append((head[0], head[1] + diff)) # tail right
            h2t_lst[3].append((head[0], head[1] - diff)) # tail left
            diff += 1

        # removes h2t if it goes off board
        h2t_lst = [h2t for h2t in h2t_lst if 0 <= h2t[-1][0] < self.brd.rows]
        h2t_lst = [h2t for h2t in h2t_lst if 0 <= h2t[-1][1] < self.brd.cols]

        # to remove h2t if any of its coords overlaps with occupied coord
        # first need list of individual coords in the h2t_lst
        h2t_coord_lst = [coord for h2t in h2t_lst for coord in h2t]
        # iterating over h2t_coord_lst ensures every coord is checked even if
        # an h2t is removed from the h2t_lst
        for coord in h2t_coord_lst:
            if coord in self.occupied:
                for h2t in h2t_lst:
                    if coord in h2t:
                        h2t_lst.remove(h2t)

        # list of the h2t_lst last coord
        tail = [h2t[-1] for h2t in h2t_lst]
        # dict of tail as key to the full set of coords as value
        h2t_dict = dict(zip(tail, h2t_lst))

        return h2t_dict

    def receive_shot(self, new):
        """ takes a new tuple which is the coordinate of where to shoot,
            compares what is at the coordinate on the board and distributes
            action; miss, already shot, hit
        """
        shot = self.brd.board[new]

        if shot == POINT['open']:
            self.brd.record_miss(new)
            print PROMPT['miss']
        elif shot in POINT.values():
            print PROMPT['already_shot']
        elif shot in (key.lower() for key in FLEET):
            print PROMPT['already_sunk']
        elif shot in (FLEET.keys()):
            self._hit(self.brd.fleet[shot], new)
        else:
            pass  # maybe raise error here

    def _hit(self, ship, new):
        """ takes the new coord that needs to be changed to a hit
            checks whether or not this hit sinks the ship and correspondingly
            changes the board and adds to the Ship's hits tally and if need be
            adds to the SUNK tally
        """
        ship.hits += 1

        if ship.hits == ship.size:
            print PROMPT['sunk'] % str(ship)
            self.brd.record_sunk(ship)
            self.sunk += 1
        else:
            print PROMPT['hit'] % str(ship)
            self.brd.record_hit(new)

class Human(Player):
    """defines the actions of a human player"""

    def __init__(self):
        """players has-a board"""
        self.brd = Board()
        self.sunk = 0 # count of how many ships have been sunk
        self.occupied = set() # list of occupied coordinates   

    def hide_ships(self, ship):
        """ prompts the user to select head using pick_coord() and tail using
            _full() to hide a ship, and using _head2tail() to show possible
            coords to hide a ship
            inputs these coordinates to the Ship's POS
        """
        # list of currently occupied coords renewed here, used with pick_coord
        self.occupied = {key for key in self.brd.board if
                                        self.brd.board[key] in FLEET.keys()}

        attempt = 0
        while attempt <= 3:
            attempt += 1

            print PROMPT['lets_hide'] % ship

            # asks for coordinate of head of ship, returns None if invalid
            head = self.pick_coord('hide_head')
            if head == None:
                continue

            # dict of possible tails given the ship and head coord
            h2t = self._head2tail(ship, head)

            # asks for the coordinate of the tail of the ship to get coords of
            # whole ship, returns None if invalid
            pos = self._full(h2t)
            if pos == None:
                continue

            display_pos = (convert(coord) for coord in pos)

            # checks whether user is ok to input ship with these coords
            ans = raw_input(PROMPT['pos_ok?'] % (str(ship),
                                                '  '.join(display_pos)))

            if ans == '': # when user just presses <Enter> record the pos
                self.brd.place_ship(ship, pos)
                print PROMPT['player_hidden'] % str(ship)
                return True
            # if user is not ok; start again with hiding the ship
            elif ans[0].lower() == 'n':
                attempt = 0
                continue
            else: # otherwise record the pos
                self.brd.place_ship(ship, pos)
                print PROMPT['player_hidden'] % str(ship)
                return True

    def _full(self, h2t):
        """ uses pick_coord() to prompt user to select the tail coord of the
            ship from a predetermined dict already invoked by _head2tail()
            returns the full set of coords for the ship if selection is valid
        """

        # if there are no possible tails for the ship, needs new head coord
        if len(h2t) == 0:
            print PROMPT['no_tail']
            return None

        # the tail list for user prompt
        options = [convert(key) for key in h2t.keys()]

        # in case there is only one possible tail coord
        if len(h2t) == 1:
            ans = raw_input(PROMPT['this_tail_ok'] % options[0])
            if ans == '':
                return h2t.values()[0]
            elif ans[0].lower() == 'n':
                return None # goes back to hide_ships()
            else:
                return h2t.values()[0]

        # in case there are multiple tail coords to choose from
        attempt = 0
        while attempt <= 3:
            attempt += 1

            print PROMPT['tail_option'] % '\t'.join(options)
            tail = self.pick_coord('hide_tail')

            # valid selection will return the coords of the full ship
            if tail in h2t.keys():
                return h2t[tail]
            # the special key to relocate the head coord
            elif tail == 'r':
                return None
            else:
                continue

        # after 3 failed attempts, return None to go back to hide_ships
        print PROMPT['wrong_tail']
        return None


    def pick_coord(self, ask):
        """ uses prompt_coord() for user input
            returns valid coord entry with appropriate prompt
        """
        attempt = 0
        while True:
            attempt += 1
            if attempt > 5:
                attempt = to_quit()
                continue

            new = prompt_coord(ask)
            if new:
                break

        if ask == 'hide_head' and new[0] in self.occupied:
            # new coord rejected for hiding if it overlaps
            print PROMPT['occupied']
            return None
        if ask == 'where2bomb':
            print PROMPT['player_attack'] % new[1]

        return new[0]


class Computer(Player):
    """defines the actions of the computer as a player"""

    def __init__(self):
        """players has-a board"""
        self.brd = Board()
        self.sunk = 0 # count of how many ships have been sunk
        self.occupied = set() # set of occupied coordinates
        self.bombed = set() # set of bombed coordinates

    def random_pick(self):
        """ computer randomly selects a coordinate to bomb out of a list of
            coord tuples that have not yet been bombed
        """
        # list of coords yet to be bombed
        to_bomb = [coord for coord in self.brd.board.keys() if
                                        coord not in self.bombed]

        bomb = choice(to_bomb) # randomly picks a coord from the list
        self.bombed.add(bomb) # adds that coord to the bombed set

        print PROMPT['comp_attack'] % (convert(bomb))
        return bomb
