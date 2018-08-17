from tkinter import ttk
import tkinter as tk

from PIL import Image, ImageTk

from python_gui.gui.tristatebutton import TriStateButton
from python_gui.constants import people, weapons, rooms
from python_gui.gui.listchoice import ListChoice
from python_gui.gui.combolabel import ComboLabel
from python_gui.gui.resources import *


class ClueGui(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.left = ttk.Frame(self)
        self.right = ttk.Frame(self)
        self.choices = ListChoice(self.right, width=100)
        self.guesses = self.create_guess_selector()
        self.images = []
        self.people, self.people_buttons = self.create_button_grid(4, people, [str(i + 1) for i in range(4)])
        self.weapons, self.weapon_buttons = self.create_button_grid(4, weapons)
        self.rooms, self.room_buttons = self.create_button_grid(4, rooms)

        self.left.pack(side=tk.LEFT)
        self.people.pack(pady=(0, 5))
        self.weapons.pack(pady=(5, 0))
        self.rooms.pack(pady=5)
        self.right.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH, padx=(5, 10), pady=(5, 0))
        self.choices.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.guesses.pack(side=tk.LEFT, fill=tk.Y)

    def create_button_grid(self, columns, row_names, column_names=list()):
        buttons = [[] for row in range(len(row_names))]
        frame = ttk.Frame(self.left)
        for i, name in enumerate(row_names):
            ttk.Label(frame, text=name, width=15, anchor=tk.E).grid(row=i+2, column=1)
        for j, name in enumerate(column_names):
            ttk.Label(frame, text=name, style='Subtitle.TLabel').grid(row=1, column=j+2)
        for j in range(columns):
            for i in range(len(row_names)):
                button = TriStateButton(frame)
                button.config(command=lambda b=button: b.toggle())
                button.grid(row=i+2, column=j+2)
                buttons[i].append(button)
        return frame, buttons

    def create_guess_selector(self):
        frame = ttk.Frame(self.right)
        label = ttk.Label(frame, text='Make Suggestion', style='Subtitle.TLabel')
        guessor = ComboLabel(frame, text='Guessing Player?')
        character = ComboLabel(frame, text='Murderer?')
        weapon = ComboLabel(frame, text='Weapon?')
        location = ComboLabel(frame, text='Room?')
        answerer = ComboLabel(frame, text='Answering Player?')
        shown = ComboLabel(frame, text='Card Shown?')
        confirm = ttk.Button(frame, text='Confirm')

        shown.state(['disabled'])

        label.pack()
        guessor.pack()
        character.pack()
        weapon.pack()
        location.pack()
        answerer.pack()
        shown.pack()
        confirm.pack(pady=10)

        return frame
