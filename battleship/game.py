"""runs the game; Battleships"""
from random import randint
from battleship.engine import Engine
from battleship.players import Human, Computer


def run():
    """runs the Engine methods in the right order"""

    game = Engine()

    game.start()
    game.comp_setup()
    game.human_setup()

    # starter = game.who_starts()
    initial = randint(1, 2)

    if initial == 1:
        result = game.play_human_first()
    else:
        result = game.play_comp_first()

    if result == 'human_win':
        game.human_win()
    else:
        game.comp_win()


def game_type():
    """user can choose playing against computer or another user"""
    pass

if __name__ == "__main__":
    run()
