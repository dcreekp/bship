"""Engine runs the game flow"""
from random import shuffle, choice
from battleship.players import Human, Computer
from battleship.config import PROMPT
from battleship.ui import show_board, show_game, convert


""" copy of what an engine class actually looks like

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
"""


class Engine(object):
    """contains the Engine methods and has-players"""

    def __init__(self):
        """engine has a list of players"""
        self.players = [Human(), Computer()]
        self.current_player = self.players[0]
        self.next_player = self.players[1]

    def start(self):
        """starts the game with some instructions"""
        print(PROMPT['title'])
        print(PROMPT['explain'])

        self._example_setup()

        eg_ship = choice(list(self.current.brd.fleet.values()))

        print(self.current.brd)

        print(PROMPT['example'].format(eg_ship, convert(eg_ship.pos[0]),
                                        convert(eg_ship.pos[-1])))

        self.current.brd.remove_fleet()

        input(PROMPT['ready'])

    def set(self):
        """ set up each player's board, and decides who goes first"""

        pass



    def play(self):
        """ rolls out the turns, determines who wins"""

        turn = 0

        print(PROMPT['turn_line'].format(turn))
        
        # show the board here

        while turn <= 100:
            turn += 1

            print(PROMPT['turn_line'].format(turn))

            point = self.current_player.attack()
            self.next_player.receive_shot(point)

            self.current_player, self.next_player = 
                    self.next_player, self.current_player


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

    """ need to separate these _bomb_ functions"""


    def _human_bomb_comp(self):
        """ uses pick_coord() to prompt user to select a coordinate to bomb
            and send info to comp.brd, checks whether human has won
        """
        bomb = self.one.pick_coord('where2bomb')
        # Human send to engine

        # engine sends to Computer
        self.comp.receive_shot(bomb)
        if self.comp.sunk == 5:
            return 'human_win'

    def _comp_bomb_human(self):
        """ uses random_pick() for computer to randomly choose a coordinate to
            bomb and send info to one.brd, checks whether computer has won
        """
        bomb = self.comp.random_pick()
        # Computer sends to engine

        # engine sends to human
        self.one.receive_shot(bomb)
        if self.one.sunk == 5:
            return 'comp_win'


    def result(self):

        pass 

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

        fleet = self.current.brd.fleet
        fleet_lst = [fleet[ship] for ship in fleet]
        shuffle(fleet_lst)

        for ship in fleet_lst:
            self.current.auto_hide_ships(ship, 2)
