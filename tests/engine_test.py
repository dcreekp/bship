from battleship.players import Human, Computer
from battleship.board import Board
from battleship.engine import *

def test_init():

    game = Engine()

    print(type(game.players))
    print(type(game.current_player))
    print(type(game.next_player))

def test_play():

    check.play()

def test_choice():

    eg_ship = choice(check.comp.brd.fleet.values())

    print(eg_ship)

def test_start():

    check.start()