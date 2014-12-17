from battleship.config import *
from battleship.players import Human, Computer
from battleship.board import Board, Ship
from battleship.engine import Engine

bb = Board()
one = Human()
comp = Computer()

check = Engine()

def test_show_game():

    check.current_player.brd.board[(0,0)] = 'K'
    check.current_player.brd.board[(4,4)] = '@'

    check.next_player.brd.board[(3,3)] = 'T'
    check.next_player.brd.board[(3,4)] = 'T'
    check.next_player.brd.board[(3,5)] = 'T'
    check.next_player.brd.board[(3,6)] = 'T'

    #check.show_game()

    check.current_player.brd.board[(5,4)] = '@'
    #check.show_game()

    check.current_player.brd.board[(6,4)] = '@'
    show_game(next_player.brd, current_player.brd)

def test__example():

    print(check._example())

def test__explain():

    check.explain()

def foo():
    ans = raw_input("Y/n??")
    if ans.lower() == 'n':
        print('done')
    else:
        print('non problemo')
