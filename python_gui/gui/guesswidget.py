from tkinter import ttk
import tkinter as tk

from python_gui.gui.combolabel import ComboLabel
from python_gui import constants

class GuessWidget(ttk.Frame):
    def __init__(self, *args, controller, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller
        label = ttk.Label(self, text='Make Suggestion', style='Subtitle.TLabel')
        self.guesser = ComboLabel(self, text='Guessing Player?')
        self.character = ComboLabel(self, text='Murderer?', values=constants.people)
        self.weapon = ComboLabel(self, text='Weapon?', values=constants.weapons)
        self.location = ComboLabel(self, text='Room?', values=constants.rooms)
        self.answerer = ComboLabel(self, text='Answering Player?')
        self.shown = ComboLabel(self, text='Card Shown?')
        self.confirm = ttk.Button(self, text='Confirm')

        for combo in self.guesser, self.character, self.weapon, self.location, self.answerer, self.shown:
            combo.state(['readonly'])
            combo._var.trace('w', lambda var, ind, op: self.validate_state())
        self.validate_state()

        label.pack()
        self.guesser.pack()
        self.character.pack()
        self.weapon.pack()
        self.location.pack()
        self.answerer.pack()
        self.shown.pack()
        self.confirm.pack(pady=10)

        self.controller.signal_players_changed.connect(self.on_players_changed)
        self.controller.signal_player_name_changed(self.on_players_changed)

    def validate_state(self):
        guesser = self.guesser.get()
        murderer = self.character.get()
        weapon = self.weapon.get()
        room = self.location.get()

        for widget in self.guesser, self.character, self.weapon, self.location, self.answerer, self.shown, self.confirm:
            widget.state(['!disabled' if self.guesser.values() else 'disabled'])

        self.confirm.state(['!disabled'
                            if murderer and weapon and room and guesser
                            else 'disabled'])
        self.shown.state(['!disabled' if murderer and weapon and room else 'disabled'])
        self.shown.set_values([murderer, weapon, room])

    def on_players_changed(self):
        names = [player.name for player in self.controller.players()]
        self.guesser.set_values(names)
        self.answerer.set_values(names)
        self.validate_state()