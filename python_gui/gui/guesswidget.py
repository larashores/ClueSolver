from tkinter import ttk
import tkinter as tk

from python_gui.gui.combolabel import ComboLabel
from python_gui import constants

class GuessWidget(ttk.Frame):
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