"""Engine runs the game flow"""
from random import shuffle, choice, randint
from battleship.players import Human, Computer
from battleship.config import PROMPT
from battleship.ui import show_board, show_game, convert, flip


class Engine(object):
    """contains the Engine methods and has-players"""

    def __init__(self):
        """engine has a list of players"""
        self.players = [Computer(), Human()]

    def start(self):
        """starts the game with some instructions"""
        print(PROMPT['title'])
        print(PROMPT['explain'])

        self._example_setup()

        eg_ship = choice(list(self.players[0].brd.fleet.values()))

        print(self.players[0].brd)

        print(PROMPT['example'].format(eg_ship, convert(eg_ship.pos[0]),
                                        convert(eg_ship.pos[-1])))

        self.players[0].brd.remove_fleet()

        input(PROMPT['ready'])


    def set(self):
        """ set up each player's board, and decides who goes first with flip()"""

        for player in self.players:
            player.set_up()

        if flip():
            self.current_player = self.players[1]
            self.next_player = self.players[0]
        else:
            self.current_player = self.players[0]
            self.next_player = self.players[1]

        input(PROMPT['comprehend'])

    def play(self):
        """ rolls out the turns, determines who wins"""

        turn = 0
        first2go = self.current_player
        
        print(PROMPT['turn_line'].format(turn))
        
        # show the board here

        while True:
            if self.current_player == first2go:
                turn += 1
                print(PROMPT['turn_line'].format(turn))

            point = self.current_player.where2bomb() # "POST request"
            self.next_player.receive_shot(point) # "GET request"


            if self.next_player.sunk == 5:
                return # self.end(self.current_player)

            self.current_player, self.next_player =\
                self.next_player, self.current_player


        input(PROMPT['comprehend']) # can go in Computer class

        show_game(self.one.brd, self.comp.brd) 
            # show game will go in Human class

    def end(self):
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

        fleet = self.players[0].brd.fleet
        fleet_lst = [fleet[ship] for ship in fleet]
        shuffle(fleet_lst)

        for ship in fleet_lst:
            self.players[0].auto_hide_ships(ship, 2)
