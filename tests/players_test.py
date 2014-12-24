import pytest
from random import choice
from battleship.players import Human, Computer
from battleship.board import Board
from battleship.ship import Ship

one = Human()
comp = Computer()


def test_human_set_up():

    one.set_up()


def test_comp_set_up():

    comp.set_up()


def test_confirm_setup():

    one._confirm_setup()


def test__init():

    b2 = Board()
    check = Human(b2)


def test_pick_coord():

    print(check.pick_coord('where2bomb'))
    print(check.pick_coord('hide_head'))
    print(check.pick_coord('hide_tail'))

    # checked for 4f and h8: both failed


def test__head2tail():
    '''
    head = (1,1)
    ship = check.brd.S # size is 3
    head2 = (5,5)
    ship2 = check.brd.K # size is 5
    print(check._head2tail(ship, head))
    print(check._head2tail(ship2, head2))
    head3 = (8,7)
    ship3 = check.brd.K
    print(check._head2tail(ship3, head3))
    '''
    head4 = (5, 5)
    ship4 = check.brd.fleet['T']
    check.occupied = [(5, 2), (5, 8), (8, 5), (2, 5)]
    # check.occupied = [(5, 2), (8, 5)]
    # check.occupied = [(5, 2), (2, 5)]
    # check.occupied = [(5, 2), (5, 8)]
    # check.occupied = [(5, 8), (8, 5)]
    # check.occupied = [(5, 8), (2, 5)]
    # check.occupied = [(8, 5), (2, 5)]
    check.occupied = [(5, 2), (5, 8), (8, 5)]
    check.occupied = [(5, 2), (5, 8), (8, 5), (7, 5)]
    dd = check._head2tail(ship4, head4)
    for key in dd:
        print(key, dd[key])


def test__full():

    bb.board[(1, 0)] = 'K'
    head = (0, 0)
    ship = check.brd.fleet['S']  # size is 3
    h2t = check._head2tail(ship, head)

    # print(check._full(h2t) # should show 2 tail options)

    print(check._full(h2t))  # should show 1 tail option)


def test__full_one():

    h2t = {(3, 3): [(4, 3), (3, 3)]}

    one._full(h2t)


def test_auto_hide_ships():

    ship = check.brd.fleet['K']
    ship2 = check.brd.fleet['S']
    ship3 = check.brd.fleet['T']

    check.auto_hide_ships(ship)
    check.auto_hide_ships(ship2)
    check.auto_hide_ships(ship3)


comp = Computer()
comp2 = Computer()
comp3 = comp2


def test_sameness():

    assert comp.brd is not check.brd
    assert comp.brd != check.brd
    assert comp.brd is not comp2.brd
    assert comp.brd != comp2.brd
    assert comp2.brd is comp3.brd
    assert comp2.brd == comp3.brd

    comp3.brd.board[(5, 5)] = 'X'
    print("comp2.brd \n", comp2.brd)
    print("comp3.brd\n", comp3.brd)

    assert comp2.brd is comp3.brd
    assert comp2.brd == comp3.brd


def test_hide_ships():

    ship = comp.brd.fleet['Y']
    ship2 = comp.brd.fleet['S']
    ship3 = comp.brd.fleet['T']

    comp.hide_ships(ship)
    print(ship.POS)
    comp.hide_ships(ship2)
    print(ship2.POS)
    comp.hide_ships(ship3)
    print(ship3.POS)


def test_randchoice():

    lst = [1, 6, 34, 42, 9]

    h = choice(lst)
    print(h)

    coord = choice(comp.brd.board.keys())
    print(coord)

    with pytest.raises(IndexError):
        empty = []
        choice(empty)


def test_random_pick():

    for i in range(5):
        i = comp.random_pick()
        print(i)
        print(comp.bombed)


def test__hit():

    comp._hit(comp.brd.fleet['P'], (0, 0))
    print(comp.brd)

    comp._hit(comp.brd.fleet['P'], (0, 1))

    print(comp.brd)


def test_receive_shot():

    check.brd.defend[(0, 0)] = 'x'
    check.brd.defend[(1, 1)] = '@'
    check.brd.defend[(2, 2)] = 'k'
    check.brd.defend[(2, 3)] = 't'
    check.brd.defend[(3, 3)] = '.'
    check.brd.defend[(4, 4)] = 'K'

    print(check.brd)

    check.receive_shot((0, 0))
    assert check.brd.defend[(0, 0)] == 'x'
    check.receive_shot((2, 2))
    assert check.brd.defend[(2, 2)] == 'k'
    check.receive_shot((3, 3))
    assert check.brd.defend[(3, 3)] == "x"
    check.receive_shot((4, 4))
    assert check.brd.defend[(4, 4)] == "@"


def test_record_shot():

    P = Ship('Patrol Boat', 'P', 2)

    P.pos = [(2, 2), (2, 3)]

    one.record_shot(P)

    new = (4, 5)
    shot = 'O'
    one.record_shot(new, shot)
