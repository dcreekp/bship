from battleship.players import Human, Computer
from battleship.board import Board
from battleship.control import *

bb = Board()
one = Human(bb)
comp = Computer(bb)

check = Game(one, comp)

def test_human_setup():

    check.human_setup()

def test_comp_setup():

    check.comp_setup()

def test_confirm_setup():

    check._confirm_setup()

def test_sameness():

    game = Game(Human(Board()),Computer(Board()))

    assert game.one.brd.board is not game.comp.brd.board
    assert game.one.brd.fleet is not game.comp.brd.fleet

def test_play():

    check.play()

def test_choice():

    eg_ship = choice(check.comp.brd.fleet.values())

    print eg_ship

def test_start():

    check.start()