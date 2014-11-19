import pytest
from battleship.board import Board
from battleship.players import Computer

def test_init():
    
    check = Board(5)

    check.board[(1,1)] = 'X'

    print check.board
    print check.fleet

check = Board()
#check.fleet['S'].POS = [(3,2),(3,3),(3,4)]

def test_place():

    check.place_ship(check.S)
    print check.board

def test_remove():

    check.remove_ship(check.S)
    print check.board

def test_remove_fleet():
    comp = Computer(check)
    ship1 = check.fleet['S']
    ship2 = check.fleet['Y']

    comp.auto_hide_ships(ship1)
    comp.auto_hide_ships(ship2)
    print check
    print ship1.POS, ship2.POS
    check.remove_fleet()
    print check
    assert ship1.POS == []
    assert ship2.POS == []
    print ship1.POS, ship2.POS

def test_board__str__():

    check.board[(0,0)] = 'S'
    check.board[(0,1)] = 'S'
    check.board[(0,2)] = 'S'
    check.board[(6,4)] = '@'

    print '\n'
    print check.__str__(True)
    #print 'ABCDEFGHIJKLMNOPQRST'[:check.rows]
    print '\n'
    print check.__str__()
