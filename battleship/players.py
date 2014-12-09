"""defines what a player can do"""
from abc import ABCMeta, abstractmethod
from random import choice, shuffle
from battleship.board import Board
from battleship.config import PROMPT, POINT, FLEET
from battleship.ui import (to_quit, clean, convert, pick_coord, show_board,
                            show_game)

class Player(metaclass=ABCMeta):
    """defines the methods players can take and has-board"""

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def where2bomb(self):
        pass

    def auto_hide_ships(self, ship, who=0):
        """ computer randomly selects head coord, then using _head2tail() gets
            a dict of coords, from the given choice randomly selects a list and
            returns the ship object and its coords to Board
        """
        self.occupied = set(key for key in self.brd.board if
                                self.brd.board[key] in FLEET.keys())

        while True:
            head = choice(list(self.brd.board.keys()))
            h2t = self._head2tail(ship, head)
            try:
                pos = choice(list(h2t.values()))
                break
            except IndexError: # if the h2t dict has zero possible coords
                continue # will need to pick a new head coord

        self.brd.place_ship(ship, pos)

        if who == 0:
            print(PROMPT['comp_hidden'].format(str(ship)))
        elif who == 1:
            print(PROMPT['player_hidden'].format(str(ship)))


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

        tail = [h2t[-1] for h2t in h2t_lst]
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
            print(PROMPT['miss'])
        elif shot in POINT.values():
            print(PROMPT['already_shot'])
        elif shot in (key.lower() for key in FLEET):
            print(PROMPT['already_sunk'])
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
            print(PROMPT['sunk'].format(str(ship)))
            self.brd.record_sunk(ship)
            self.sunk += 1
        else:
            print(PROMPT['hit'].format(str(ship)))
            self.brd.record_hit(new)

class Human(Player):
    """defines the actions of a human player"""

    def __init__(self):
        """players has-a board"""
        self.brd = Board()
        self.sunk = 0
        self.occupied = set()

    def name(self):
        return "Player 1"

    def setup(self):
        """ prompts the user to set up their board; manually choose which ship
            and hide it with hide_ships(), or automatically hide all
        """
        fleet = self.brd.fleet
        fleet_lst = [fleet[ship] for ship in fleet]
        shuffle(fleet_lst)

        while len(fleet_lst) > 0:
            print(PROMPT['border'])

            show_board(self.brd)

            select = input(PROMPT['which_ship'].format('\n   '.join([str(ship)
                                                        for ship in fleet_lst])))

            if select.lower() == 'a': # automates the hiding process
                for ship in fleet_lst:
                    self.auto_hide_ships(ship, 1)
                self._confirm_setup()
                return

            # for manually hiding the selected ship
            if fleet.get(select.upper()) in fleet_lst:
                check = self.hide_ships(fleet.get(select.upper()))
                if check == True:
                    fleet_lst.remove(fleet.get(select.upper()))
                else:
                    continue
            elif select == '':
                self.hide_ships(fleet_lst.pop(0))
            else:
                print(PROMPT['which_ship_explain'].format(' '.join([str(ship
                                .sign) for ship in fleet_lst])))

        self._confirm_setup()

    def _confirm_setup(self):
        """display the completed board setup for player to confirm or revise"""

        show_board(self.brd)
        check = input(PROMPT['good2go'])

        if check.lower() == 'n' or check.lower() == 'no':
            print(PROMPT['start_again'])
            self.brd.remove_fleet()
            return self.setup()
        else:
            return

    def hide_ships(self, ship):
        """ prompts the user to select head using _pick_coord(), _head2tail() to show possible coords for the tail and _full() to select tail to hide a ship
            sends the ship object and a list of coords to Board
        """
        self.occupied = set(key for key in self.brd.board if
                                        self.brd.board[key] in FLEET.keys())

        attempt = 0
        while attempt <= 3:
            attempt += 1

            print(PROMPT['lets_hide'].format(ship))

            head = pick_coord('hide_head')
            if head in self.occupied:
                print(PROMPT['occupied'])
                continue

            h2t = self._head2tail(ship, head)
            pos = self._full(h2t)
            if pos == None:
                continue

            display_pos = (convert(coord) for coord in pos)
            ans = input(PROMPT['pos_ok?'].format(str(ship),
                                                '  '.join(display_pos)))

            if ans.lower() == 'n' or ans.lower() =='no':
                self.hide_ships(ship)
            else:
                self.brd.place_ship(ship, pos)
                print(PROMPT['player_hidden'].format(str(ship)))
                return True

    def _full(self, h2t):
        """ uses _pick_coord() to prompts user to select the tail coord of the
            ship from the dict returned by _head2tail()
            returns the full set of coords to return to hide_ships() if
            selection is valid
        """
        if len(h2t) == 0:
            print(PROMPT['no_tail'])
            return None

        options = [convert(key) for key in h2t.keys()]

        if len(h2t) == 1:
            ans = input(PROMPT['this_tail_ok'].format('{ ' + options[0] + ' }'))

            if ans.lower() == 'n' or ans.lower() == 'no':
                return None
            else:
                return h2t[convert(options[0])]

        attempt = 0
        while attempt <= 3:
            attempt += 1

            print(PROMPT['tail_option'].format('{ ' + '   '.join(options) + ' }'))
            tail = pick_coord('hide_tail')

            if tail in h2t.keys():
                return h2t[tail]
            elif tail == 'r': # exception if user wants to revise head coord 
                return None
            else:
                continue

        print(PROMPT['wrong_tail'])
        return None


    def where2bomb(self):
        """Human selects a coordinate to bomb"""

        bomb = pick_coord()
        print(PROMPT['player_attack'].format(convert(bomb)))
        return bomb

class Computer(Player):
    """defines the actions of the computer as a player"""

    def __init__(self):
        """players has-a board"""
        self.brd = Board()
        self.sunk = 0
        self.occupied = set()
        self.bombed = set()

    def name(self):
        return "Computer"

    def setup(self):
        """gets computer to hide the ships for game play"""

        fleet = self.brd.fleet
        fleet_lst = [fleet[ship] for ship in fleet]
        shuffle(fleet_lst)

        print(PROMPT['border'])

        for ship in fleet_lst:
            self.auto_hide_ships(ship)

    def where2bomb(self):
        """ Computer selects a coordinate to bomb"""

        bomb = self._random_pick()
        print(PROMPT['comp_attack'].format((convert(bomb))))
        return bomb

    def _random_pick(self):
        """ Computer randomly selects a coordinate out of a list of coord
            tuples that have not yet been bombed
        """

        to_bomb = [coord for coord in self.brd.board.keys() if
                                        coord not in self.bombed]

        bomb = choice(to_bomb)
        self.bombed.add(bomb)

        return bomb
