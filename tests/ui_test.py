import pytest
from battleship.ui import *

def test_to_quit():

    to_quit()

def test__clean():

    assert clean('A1') == 'A1'
    assert clean('B.2') == 'B2'
    assert clean('c,3') == 'C3'
    assert clean('      d4     ') == 'D4'
    assert clean('e      5') == 'E5'
    assert clean('(a1)') == 'A1'
    assert clean('gg5') == None
    assert clean('5d') == None

def test_convert():

    assert convert('J9') == (9,9)
    assert convert((0,0)) == 'A0'
    assert convert((6,3)) == 'G3'
    assert convert((0,3)) == 'A3'
    
    #with pytest.raises(KeyError):
    assert convert('S3') == None

def test_flip():

    flip()
