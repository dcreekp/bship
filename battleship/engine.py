"""Engine runs the game flow"""
from random import shuffle, choice
from battleship.players import Human, Computer
from battleship.config import PROMPT
from battleship.ui import show_board, show_game, convert


class Engine(object):
    """contains the Engine methods and has-players"""

    def __init__(self):
        """engine has player one and player comp"""
        self.one = Human()
        self.comp = Computer()

    def start(self):
        """starts the game with some instructions"""
        print(PROMPT['title'])
        print(PROMPT['explain'])

        self._example_setup()

        eg_ship = choice(list(self.comp.brd.fleet.values()))

        print(self.comp.brd)

        print(PROMPT['example'].format(eg_ship, convert(eg_ship.pos[0]),
                                        convert(eg_ship.pos[-1])))

        self.comp.brd.remove_fleet()

        input(PROMPT['ready'])

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
            input(PROMPT['comprehend'])

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
            input(PROMPT['comprehend'])
            
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
