from battleship.players import Human, Computer
from battleship.board import Board
from battleship.engine import *


def test_init():

    game = Engine()

    print(type(game.players))
    print(type(game.players[0]))
    print(type(game.players[1]))
    print(type(game.player))


def test_set():

    game = Engine()

    game.set()


def test_play():

    check.play()


def test_choice():

    eg_ship = choice(check.comp.brd.fleet.values())

    print(eg_ship)


def test_start():

    check.start()


def test_end():

    game = Engine()

    # game.end(game.players[0])

    if game.end():
        print("again")
        return
    print("good game!")
