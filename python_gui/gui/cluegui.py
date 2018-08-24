from tkinter import ttk
import tkinter as tk

from python_gui.gui.guesswidget import GuessWidget
from python_gui.gui.namewidget import NameWidget
from python_gui.gui.carddisplay import CardDisplay
from python_gui.gui.new.newgamewidget import NewGameWidget
from python_gui.gui.buttongrid import ButtonGrid
from python_gui.constants import people, weapons, rooms
from python_gui.gui.listchoice import ListChoice
from python_gui.gui.combolabel import ComboLabel
from python_gui.gui.tristatusbutton import TriStatusButton
from python_gui import constants

import python_gui.pyclue as pyclue


class ClueGui(ttk.Frame):
    def __init__(self, *args, game, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.card_display = CardDisplay(self, columns=4, game=game)
        self.guess_list = ListChoice(self, width=100)
        self.guesses = GuessWidget(self)
        self.names = NameWidget(self, names=['Vince', 'Kristina', 'Vanessa', 'Cassandra'])

        self.card_display.grid(column=1, row=1, rowspan=2)

        self.names.grid(column=2, row=1)
        self.guess_list.grid(column=2, row=2, sticky=(tk.N + tk.S + tk.E + tk.W))
        self.guesses.grid(column=3, row=1, rowspan=2, sticky=tk.N, padx=(0, 10))
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)


class Clue:
    def __init__(self, parent=None):
        self.game = pyclue.Game()
        self.gui = ClueGui(parent, game=self.game)

    def on_new(self):
        widget = NewGameWidget(self.gui, game=self.game)
        widget.set_close_command(self.on_close_new)

    def on_close_new(self):
        self.gui.card_display.regrid(len(self.game.get_players()))
        self.gui.card_display.update_buttons(self.game)
