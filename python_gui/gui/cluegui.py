from tkinter import ttk
import tkinter as tk

from python_gui.gui.guesswidget import GuessWidget
from python_gui.gui.namewidget import NameWidget
from python_gui.gui.carddisplay import CardDisplay
from python_gui.gui.new.newgamewidget import NewGameWidget
from python_gui.gui.addplayer.addplayerwidget import AddPlayerWidget
from python_gui.gui.removeplayer.removeplayerwidget import RemovePlayerWidget
from python_gui.gui.buttongrid import ButtonGrid
from python_gui.constants import people, weapons, rooms
from python_gui.gui.listchoice import ListChoice
from python_gui.gui.combolabel import ComboLabel
from python_gui import constants

import python_gui.pyclue as pyclue

from tkinter.messagebox import showwarning


class ClueGui(ttk.Frame):
    def __init__(self, *args, controller, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.card_display = CardDisplay(self, columns=4, controller=controller)
        self.guess_list = ListChoice(self, width=100)
        self.guesses = GuessWidget(self, controller=controller)
        self.names = NameWidget(self, controller=controller)

        self.card_display.grid(column=1, row=1, rowspan=2)

        self.names.grid(column=2, row=1)
        self.guess_list.grid(column=2, row=2, sticky=(tk.N + tk.S + tk.E + tk.W))
        self.guesses.grid(column=3, row=1, rowspan=2, sticky=tk.N, padx=(0, 10))
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)


class Clue:
    def __init__(self, *args, controller, **kwargs):
        self.controller = controller
        self.gui = ClueGui(*args, **kwargs, controller=self.controller)

    def on_new(self):
        widget = NewGameWidget(self.gui, controller=self.controller)

    def on_add_player(self):
        widget = AddPlayerWidget(self.gui, controller=self.controller)

    def on_remove_player(self):
        if self.controller.num_players() > 0:
            widget = RemovePlayerWidget(self.gui, controller=self.controller)
        else:
            showwarning(title='Warning', message='No players to delete')
