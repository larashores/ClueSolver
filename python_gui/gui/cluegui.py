from tkinter import ttk
import tkinter as tk

from python_gui.gui.tristatebutton import TriStateButton
from python_gui.constants import people, weapons, rooms
from python_gui.gui.listchoice import ListChoice
from python_gui.gui.combolabel import ComboLabel


class GuessingFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        label = ttk.Label(self, text='Make Suggestion', style='Subtitle.TLabel')
        guesser = ComboLabel(self, text='Guessing Player?')
        character = ComboLabel(self, text='Murderer?')
        weapon = ComboLabel(self, text='Weapon?')
        location = ComboLabel(self, text='Room?')
        answerer = ComboLabel(self, text='Answering Player?')
        shown = ComboLabel(self, text='Card Shown?')
        confirm = ttk.Button(self, text='Confirm')

        shown.state(['disabled'])

        label.pack()
        guesser.pack()
        character.pack()
        weapon.pack()
        location.pack()
        answerer.pack()
        shown.pack()
        confirm.pack(pady=10)


class ButtonGrid(ttk.Frame):
    def __init__(self, parent=None, columns=0, row_names=list(), column_names=list(), **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.buttons = [[] for row in range(len(row_names))]
        for i, name in enumerate(row_names):
            ttk.Label(self, text=name, width=15, anchor=tk.E).grid(row=i+2, column=1)
        for j, name in enumerate(column_names):
            ttk.Label(self, text=name, style='Subtitle.TLabel').grid(row=1, column=j+2)
        for j in range(columns):
            for i in range(len(row_names)):
                button = TriStateButton(self)
                button.config(command=lambda b=button: b.toggle())
                button.grid(row=i+2, column=j+2)
                self.buttons[i].append(button)


class ClueGui(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.people = ButtonGrid(self, 4, people, [str(i + 1) for i in range(4)])
        self.weapons = ButtonGrid(self, 4, weapons)
        self.rooms = ButtonGrid(self, 4, rooms)
        self.guess_list = ListChoice(self, width=100)
        self.guesses = GuessingFrame(self)

        self.people.grid(row=1, column=1)
        self.weapons.grid(row=2, column=1, pady=10)
        self.rooms.grid(row=3, column=1)
        self.guess_list.grid(row=1, column=2, rowspan=3, sticky=(tk.N + tk.S + tk.E + tk.W))
        self.guesses.grid(row=1, column=3, rowspan=3, sticky=tk.N, padx=(0, 10))
        for i in range(3):
            tk.Grid.rowconfigure(self, i+1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)
