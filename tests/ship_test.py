from battleship.ship import Ship

ship = Ship('ship', 'C', 2)

def test_shipclass():
 
    assert ship.name == 'ship'
    assert ship.size == 2
    assert ship.hits == 0
    assert ship.sign == 'C'


def test_ship__str_():

    print str(ship)

    assert str(ship) == "C ship(2)"

def test_empty():

    ship.pos = [(1,1),(1,2)]

    ship.empty()
    print ship.pos
    assert ship.pos == []