""" config.py contains
    prompts and
    functions to display the Board
"""
from battleship.ship import Ship

PROMPT = {
## .control
'title': "\n\t    **BATTLESHIPS**\n",
'explain': """   Battleships is a two player guessing game.
   Each player hides five ships, and takes turns to guess
   the coordinates of their enemy's ships.
   The first player to sink all five enemy ships is the winner.\n""",
'example': """\n   The ships are labelled as Sign Name(Size).
   for example: %s has head coordinate %s
   and tail coordinate %s.""",
'ready': "\nReady to play? >> ",
'border': "\n   ===============*Hide Ships*================",
'turn_line': "\n   ===============* Battle %d *==================",
'which_ship': "Which ship do you want to hide?\n   %s\t(Type the sign of a ship or type 'A' to autohide.)\n>> ",
'already_hidden': "You have already hidden the %s.",
'which_ship_explain': "Select a ship to hide by typing K T S Y or P.\n",
'good2go': "Are you good with this board?\n(Y/n) >> ",
'start_again': "OK let's reset the board...",
'result': "\n   ===============** result **===================",
'one_wins': "\n   Player1 wins!\n",
'comp_wins': "\n   Computer wins!\n",
'comprehend': ">>",
## .players
'miss': "   MISS!",
'already_shot': "   You've already shot here, what a waste!",
'already_sunk': "   You've already sunk a ship here, what a waste!",
'sunk': "   And sinks the enemy %s!",
'hit': "   And hits the enemy %s.",
'bad_coord': "Type a coordinate LETTERnumber eg. %s",
'off_board': "Your coordinate missed the sea. Try again.",
'where2bomb': "Which coordinate do you want to bomb??\n>> ",
'lets_hide': "Let's hide the %s.",
'player_hidden': "   Player1 has hidden the %s",
'comp_hidden': "   Computer has hidden the %s",
'hide_head': "Which coordinate do you want to hide the head of the ship??\n>> ",
'hide_tail': "Pick a coordinate for the tail of the ship (or type 'R' to relocate head coord).\n>> ", 
'tail_option': "The tail of the ship can be hidden in these coordinates:\n\t{ %s }",
'revise': "Or did you want to change the head coordinate of the ship??\n(Y/n) >> ",
'wrong_tail': "You will have to hide the ship with a new head coordinate...",
'occupied': "These coordinates are already occupied by another ship of your fleet.",
'no_tail': "For this head coordinate, there are no possible tail coordinates. Choose another head coordinate.",
'this_tail_ok': "The tail of the ship can be hidden in this coordinate:\n\t{ %s }\n(Y/n) >> ",
'quitter': "Are you bored... do you want to quit??\n(Y/n) >> ",
'pos_ok?': "The %s will be hidden here:\n\t[ %s ]\n(Y/n) >> ",
'player_attack': "Player1 attacks %s.",
'comp_attack': "Computer attacks %s.",
'bored': "OK you're bored, Goodbye!!"
}

POINT = {
'open': '.',
'miss': 'x',
'hit': '@'
}

FLEET = {
'K': Ship('AircraftCarrier', 'K', 5),
'T': Ship('Battleship', 'T', 4),
'S': Ship('Submarine', 'S', 3),
'Y': Ship('Destroyer', 'Y', 3),
'P': Ship('PatrolBoat', 'P', 2)
}
