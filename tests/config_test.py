from battleship.config import *
from battleship.players import Human, Computer
from battleship.board import Board, Ship
from battleship.engine import Engine

bb = Board()
one = Human()
comp = Computer()

check = Engine()


def test__example():

    print(check._example())


def test__explain():

    check.explain()


def test_foo():
    ans = raw_input("Y/n??")
    if ans.lower() == 'n':
        print('done')
    else:
        print('non problemo')


def test_prompt():

    print('')
    print(PROMPT['hide_tail'])
