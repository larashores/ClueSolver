from tkinter import ttk
import tkinter as tk

from python_gui.gui.new.askplayers import ask_players
from python_gui.gui.new.asknames import ask_names
from python_gui.gui.new.askorder import ask_order
from python_gui.gui.new.askcards import ask_cards


def ask_new(parent=None):
    num_players = ask_players(parent)
    names = ask_names(parent, num_players)
    ordered = ask_order(parent, names)
    cards = ask_cards(parent, ordered)

