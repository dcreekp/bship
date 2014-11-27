from battleship.config import *
from battleship.players import Human, Computer
from battleship.board import Board, Ship
from battleship.control import Game

bb = Board()
one = Human(bb)
comp = Computer(bb)

check = Game(one, comp)

def test_show_game():

    check.comp.brd.board[(0,0)] = 'K'
    check.comp.brd.board[(4,4)] = '@'

    check.one.brd.board[(3,3)] = 'T'
    check.one.brd.board[(3,4)] = 'T'
    check.one.brd.board[(3,5)] = 'T'
    check.one.brd.board[(3,6)] = 'T'

    #check.show_game()

    check.comp.brd.board[(5,4)] = '@'
    #check.show_game()

    check.comp.brd.board[(6,4)] = '@'
    show_game(one.brd, comp.brd)

def test__example():

    print check._example()

def test__explain():

    check.explain()

def foo():
    ans = raw_input("Y/n??")
    if ans.lower() == 'n':
        print 'done'
    else:
        print 'non problemo'
