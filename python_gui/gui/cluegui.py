from tkinter import ttk
import tkinter as tk

from python_gui.gui.new.newgamewidget import NewGameWidget
from python_gui.gui.buttongrid import ButtonGrid
from python_gui.constants import people, weapons, rooms
from python_gui.gui.listchoice import ListChoice
from python_gui.gui.combolabel import ComboLabel
from python_gui import constants

import python_gui.pyclue as pyclue


class GuessingFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        label = ttk.Label(self, text='Make Suggestion', style='Subtitle.TLabel')
        self.guesser = ComboLabel(self, text='Guessing Player?')
        self.character = ComboLabel(self, text='Murderer?', values=constants.people)
        self.weapon = ComboLabel(self, text='Weapon?', values=constants.weapons)
        self.location = ComboLabel(self, text='Room?', values=constants.rooms)
        self.answerer = ComboLabel(self, text='Answering Player?')
        self.shown = ComboLabel(self, text='Card Shown?')
        self.confirm = ttk.Button(self, text='Confirm')

        self.shown.state(['disabled'])
        for combo in self.guesser, self.character, self.weapon, self.location, self.answerer, self.shown:
            combo.state(['readonly'])
            combo.var.trace('w', self.validate_state)
        self.confirm.state(['disabled'])

        label.pack()
        self.guesser.pack()
        self.character.pack()
        self.weapon.pack()
        self.location.pack()
        self.answerer.pack()
        self.shown.pack()
        self.confirm.pack(pady=10)

    def validate_state(self, var, ind, op):
        murderer = self.character.get()
        weapon = self.weapon.get()
        room = self.location.get()

        self.confirm.state(['!disabled'
                            if murderer and weapon and room and self.guesser.get()
                            else 'disabled'])
        self.shown.state(['!disabled' if murderer and weapon and room else 'disabled'])
        self.shown.combo.config(values=[murderer, weapon, room])


class Names(ttk.Frame):
    def __init__(self, *args, names=list(), **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        for i, name in enumerate(names):
            label = ttk.Label(self, text='{}) {}   '.format(i+1, name), style='Subtitle.TLabel')
            label.pack(side=tk.LEFT)


class ClueGui(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.people = ButtonGrid(self, 4, people, [str(i + 1) for i in range(4)])
        self.weapons = ButtonGrid(self, 4, weapons)
        self.rooms = ButtonGrid(self, 4, rooms)
        self.guess_list = ListChoice(self, width=100)
        self.guesses = GuessingFrame(self)
        self.names = Names(self, names=['Vince', 'Kristina', 'Vanessa', 'Cassandra'])

        self.people.grid(column=1, row=1, rowspan=2)
        self.weapons.grid(column=1, row=3, pady=10)
        self.rooms.grid(column=1, row=4)

        self.names.grid(column=2, row=1)
        self.guess_list.grid(column=2, row=2, rowspan=3, sticky=(tk.N + tk.S + tk.E + tk.W))

        self.guesses.grid(column=3, row=1, rowspan=4, sticky=tk.N, padx=(0, 10))
        for i in range(3):
            tk.Grid.rowconfigure(self, i+2, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)


class Clue:
    def __init__(self, parent=None):
        self.gui = ClueGui(parent)
        self.game = pyclue.Game()

    def on_new(self):
        widget = NewGameWidget(self.gui, game=self.game)
