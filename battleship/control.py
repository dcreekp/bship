"""controls the game flow"""
from random import shuffle, choice
from battleship.config import PROMPT
from battleship.ui import show_board, show_game, convert


class Game(object):
    """contains the Game methods and has-players"""

    def __init__(self, one, comp):
        """game has player one and player comp"""
        self.one = one
        self.comp = comp

    def start(self):
        """starts the game with some instructions"""
        print(PROMPT['title'])
        print(PROMPT['explain'])

        self._example_setup()

        eg_ship = choice(list(self.comp.brd.fleet.values()))

        print(self.comp.brd)

        print(PROMPT['example'].format(eg_ship, convert(eg_ship.pos[0]),\
                                        convert(eg_ship.pos[-1])))

        self.comp.brd.remove_fleet()

        input(PROMPT['ready'])

    def human_setup(self):
        """ prompts the user to set up their board; manually choose which ship
            and hide it with hide_ships(), or automatically hide all
        """
        # dict of all ship's for player's board
        fleet = self.one.brd.fleet
        # list of ship objects left to hide
        fleet_lst = [fleet[ship] for ship in fleet]
        shuffle(fleet_lst)


        while len(fleet_lst) > 0:
            print(PROMPT['border'])

            # displays the current board
            show_board(self.one.brd)

            # prompts user to select a ship to hide or autohide the rest
            select = input(PROMPT['which_ship'].format('\n   '.join([str(ship)\
                                                        for ship in fleet_lst])))

            if select.lower() == 'a': # automates the hiding process
                for ship in fleet_lst:
                    self.one.auto_hide_ships(ship, 1)
                self._confirm_setup()
                return

            # for manually hiding the selected ship
            if fleet.get(select.upper()) in fleet_lst:
                check = self.one.hide_ships(fleet.get(select.upper()))
                if check == True:
                    # only removes if ship was hidden successfully
                    fleet_lst.remove(fleet.get(select.upper()))
                else: # if hide_ships() returns None start again
                    continue
            # in case user just types <Enter> will pop off first in fleet_lst
            elif select == '':
                self.one.hide_ships(fleet_lst.pop(0))
            # in case user selects a ship already hidden
            elif fleet.get(select.upper()) not in fleet_lst and \
                        select.upper() in 'KTSYP':
                print(PROMPT['already_hidden'].format(str(fleet.get(select.upper()))))
            else:
                print(PROMPT['which_ship_explain'])

        self._confirm_setup()

    def _confirm_setup(self):
        """display the completed board setup for player to confirm or revise"""

        show_board(self.one.brd)
        check = input(PROMPT['good2go'])

        if check == '':
            return
        elif check[0].lower() == 'n':
            print(PROMPT['start_again'])
            self.one.brd.remove_fleet()
            return self.human_setup()
        else:
            return

    def comp_setup(self):
        """gets computer to hide the ships for game play"""

        # a dict for all the ships on comp's board
        fleet = self.comp.brd.fleet
        # list of ship objects left to hide
        fleet_lst = [fleet[ship] for ship in fleet]
        shuffle(fleet_lst)

        print(PROMPT['border'])

        for ship in fleet_lst:
            self.comp.auto_hide_ships(ship)

    def play_comp_first(self):
        """ rolls out the turns; comp guess first, player second
            and then display
        """

        turn = 0

        print(PROMPT['turn_line'].format(turn))
        show_game(self.one.brd, self.comp.brd)

        while turn <= 100:
            turn += 1

            print(PROMPT['turn_line'].format(turn))

            if self._comp_bomb_human() == 'comp_win':
                return 'comp_win'
            if self._human_bomb_comp() == 'human_win':
                return 'human_win'

            show_game(self.one.brd, self.comp.brd)


    def play_human_first(self):
        """ rolls out the turns; player guess first, comp second
            and then display
        """

        turn = 0

        print(PROMPT['turn_line'].format(turn))
        show_game(self.one.brd, self.comp.brd)

        while turn <= 100:
            turn += 1

            print(PROMPT['turn_line'].format(turn))

            if self._human_bomb_comp() == 'human_win':
                return 'human_win'
            if self._comp_bomb_human() == 'comp_win':
                return 'comp_win'

            show_game(self.one.brd, self.comp.brd)

    def _human_bomb_comp(self):
        """ uses pick_coord() to prompt user to select a coordinate to bomb
            and send info to comp.brd, checks whether human has won
        """
        bomb = self.one.pick_coord('where2bomb')
        self.comp.receive_shot(bomb)
        if self.comp.sunk == 5:
            return 'human_win'

    def _comp_bomb_human(self):
        """ uses random_pick() for computer to randomly choose a coordinate to
            bomb and send info to one.brd, checks whether computer has won
        """
        bomb = self.comp.random_pick()
        self.one.receive_shot(bomb)
        if self.one.sunk == 5:
            return 'comp_win'

        input(PROMPT['comprehend'])

    def human_win(self):
        """ end game with human win"""

        print(PROMPT['result'])
        show_game(self.one.brd, self.comp.brd)
        print(PROMPT['one_wins'])

    def comp_win(self):
        """ end game with computer win"""

        print(PROMPT['result'])
        show_game(self.one.brd, self.comp.brd)
        print(PROMPT['comp_wins'])

    def _example_setup(self):
        """ setup to show an example of the board and game """

        # a dict for all the ships on comp's board
        fleet = self.comp.brd.fleet
        # list of ship objects left to hide
        fleet_lst = [fleet[ship] for ship in fleet]
        shuffle(fleet_lst)

        for ship in fleet_lst:
            self.comp.auto_hide_ships(ship, 2)
