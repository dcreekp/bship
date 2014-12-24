from battleship.players import Human, Computer
from battleship.engine import Engine
from battleship.board import Board
from battleship.game import run


def test_run():

    run()


def test_stuff():

    lst = ['abcd', 'efgh', 'ijkl']

    tp = (0, 0)
    try:
        new_pos = lst[tp[0]][tp[1]]
        print 'Hell yeah!'
    except IndexError:
        print 'wrong! wrong! wrong!'
