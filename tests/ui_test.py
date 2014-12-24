import pytest
from battleship.ui import *


def test_show_game():

    check.current_player.brd.board[(0, 0)] = 'K'
    check.current_player.brd.board[(4, 4)] = '@'

    check.next_player.brd.board[(3, 3)] = 'T'
    check.next_player.brd.board[(3, 4)] = 'T'
    check.next_player.brd.board[(3, 5)] = 'T'
    check.next_player.brd.board[(3, 6)] = 'T'

    # check.show_game()

    check.current_player.brd.board[(5, 4)] = '@'
    # check.show_game()

    check.current_player.brd.board[(6, 4)] = '@'
    show_game(next_player.brd, current_player.brd)


def test_to_quit():

    to_quit()


def test__clean():

    assert clean('A1') == 'A1'
    assert clean('B.2') == 'B2'
    assert clean('c,3') == 'C3'
    assert clean('      d4     ') == 'D4'
    assert clean('e      5') == 'E5'
    assert clean('(a1)') == 'A1'
    assert clean('gg5') is None
    assert clean('5d') is None


def test_convert():

    assert convert('J9') == (9, 9)
    assert convert((0, 0)) == 'A0'
    assert convert((6, 3)) == 'G3'
    assert convert((0, 3)) == 'A3'

    # with pytest.raises(KeyError):
    assert convert('S3') is None


def test_flip():

    flip()


def test_pick_coord():

    pick_coord('hide_tail')
