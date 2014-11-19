import pytest
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

def test_to_quit():

    to_quit()

def test__clean():

    assert check._clean('A1') == 'A1'
    assert check._clean('B.2') == 'B2'
    assert check._clean('c,3') == 'C3'
    assert check._clean('      d4     ') == 'D4'
    assert check._clean('e      5') == 'E5'
    assert check._clean('(a1)') == None
    assert check._clean('gg5') == None
    assert check._clean('5d') == None

def test_convert():

    assert convert('J9') == (9,9)
    assert convert((0,0)) == 'A0'
    assert convert((6,3)) == 'G3'
    assert convert((0,3)) == 'A3'
    
    #with pytest.raises(KeyError):
    assert convert('S3') == None
