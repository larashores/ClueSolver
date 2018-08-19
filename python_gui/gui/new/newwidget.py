from python_gui.gui.new.asknumplayers import ask_num_players
from python_gui.gui.new.asknames import ask_names
from python_gui.gui.new.askorder import ask_order
from python_gui.gui.new.askcards import ask_cards
from python_gui.gui.new.askplayer import ask_player


def ask_new(parent=None):
    num_players = ask_num_players(parent)
    names = ask_names(parent, num_players)
    ordered = ask_order(parent, names)
    cards = ask_cards(parent, ordered)
    ask_player(parent, ordered)
