# ClueSolver
C++ and Python library and GUI for solving the board game Clue

This project was an attempt to figure out how to use Boost-Python to create a Python API in C++. The C++ library was created completely indepently from the Python. The C++ API does not need any Boost facilities to run. Wrapper funcions were created as needed for the Python bindings, demonstrating that an API not developed for use in Python could be directly adapted with a little effort.

A Python GUI was created with tkinter to demonstrate use of the Python API. The program takes in guesses to the board game Clue and displays all info that can be deduced from those guesess. It uses these five methods:
1. Cards can be manually proved or disproved from any player. This is the case if it is your card or you know the card from some other means (such as if a card is open to anyone to give ever player the same amount of cards).
2. If a player is proved to have their total number of cards, that the player doesn't have any more cards.
3. If a player is skipped in a round of guessing, they don't have any of the three suggested cards.
4. If a player answers a suggestion with a card that you see, that player has that card and no other players have that card.
5. If a player answers a suggestion with a card that you don't see, but you know that the player doesn't have two of the three cards, you can conclude that the player has the third card.

This an image of the main window between rounds of guessing:
<img src="https://raw.githubusercontent.com/vinceshores/ClueSolver/master/images/mainwindow.png" width="800">

Cards that players for sure do and do not have are displayed on the left. All previous guesses are displayed in the center and can be deleted from there. The right hand column is where info for each guess is entered. The file menu includes options for starting a new game, saving, and loading. The edit menu contains options for adding new players, deleting players, changing the player order, and editing the manual overrides.

This is an image of the different stages of the new game widget (all in one window):
<img src="https://raw.githubusercontent.com/vinceshores/ClueSolver/master/images/newgamewidget.png" width="600">

All of these options can be edited later, but this widget provides a quick way to start up a new game with many players.
