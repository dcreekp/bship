from collections import OrderedDict    
from battleship.players import Human, Computer
from battleship.control import Game
from battleship.board import Board
from battleship.engine import engine

def test_engine():

    engine()





def test_stuff():

    lst = ['abcd', 'efgh', 'ijkl']

    tp = (0,0)
    try:
        new_pos = lst[tp[0]][tp[1]]  
        print 'Hell yeah!'
    except IndexError:
        print 'wrong! wrong! wrong!'

    
    def _con(entry):
        """converts typed coord to readable coord
        """
        # need to convert 'A1' to (0,0) 'c, 6' to (2,5) ' e  7  ' to (4,6)

        a2d = dict(zip('ABCDEFGHI', range(9)))
        for c in entry:
            entry.replace(',',' ')
            entry.replace('.',' ')
            entry.replace('/',' ')
        print entry
        coord = entry.split()
        print entry
        if len(coord) == 2:
            try:
                if coord[0].isalpha() and coord[1].isdigit():
                    return a2d[coord[0].upper()], int(coord[1])
                else:
                    return entry
            except KeyError:
                return entry
        else:
            return entry

    print _con('a,1')
    print _con('b 4')

