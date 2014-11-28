from battleship.players import Human, Computer
from battleship.board import Board
from battleship.engine import *

bb = Board()
one = Human()
comp = Computer()



def test_sameness():

    game = Engine(Human(Board()),Computer(Board()))

    assert game.one.brd.board is not game.comp.brd.board
    assert game.one.brd.fleet is not game.comp.brd.fleet

def test_play():

    check.play()

def test_choice():

    eg_ship = choice(check.comp.brd.fleet.values())

    print(eg_ship)

def test_start():

    check.start()