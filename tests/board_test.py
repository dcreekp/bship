import pytest
from battleship.board import Board
from battleship.players import Computer

def test_init():
    
    check = Board(5)

    check.board[(1,1)] = 'X'

    print(check.board)
    print(check.fleet)

check = Board()


def test_place():

    pos = [(3,2),(3,3),(3,4)]
    check.place_ship(check.fleet['S'], pos)
    print(check)

def test_remove():

    check.remove_ship(check.fleet['S'])
    print(check)

def test_remove_fleet():
    comp = Computer()
    ship1 = check.fleet['S']
    ship2 = check.fleet['Y']

    comp.auto_hide_ships(ship1)
    comp.auto_hide_ships(ship2)
    #print(check)
    print(ship1.pos, ship2.pos)
    check.remove_fleet()
    #print(check)
    assert ship1.pos == []
    assert ship2.pos == []
    print(ship1.pos, ship2.pos)

def test_board__str__():

    check.board[(0,0)] = 'S'
    check.board[(0,1)] = 'S'
    check.board[(0,2)] = 'S'
    check.board[(6,4)] = '@'

    print('\n')
    print(check.__str__(True))
    #print('ABCDEFGHIJKLMNOPQRST'[:check.rows])
    print('\n')
    print(check)
