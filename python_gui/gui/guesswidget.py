from tkinter import ttk
import tkinter as tk

from python_gui.gui.skipwidget import SkipWidget
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
        self.skip = SkipWidget(self, controller=controller)
        self.confirm = ttk.Button(self, text='Confirm')

        for combo in self.guesser, self.answerer:
            combo._var.trace('w', lambda var, ind, op: self.update_skips)

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
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(expand=tk.YES, fill=tk.X, pady=(6, 0))
        self.skip.pack()
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(expand=tk.YES, fill=tk.X, pady=(6, 0))
        self.confirm.pack(pady=10)

        self.controller.signal_players_changed.connect(self.on_players_changed)
        self.controller.signal_player_name_changed(self.on_players_changed)

    def validate_state(self):
        guesser = self.guesser.get()
        murderer = self.character.get()
        weapon = self.weapon.get()
        room = self.location.get()

        answer_names = [player.name for player in self.controller.players() if player.name != self.guesser.get()]
        skip_names = [player.name for player in self.controller.players()
                      if player.name != self.guesser.get() and player.name != self.answerer.get()]
        self.answerer.set_values([' '] + answer_names)
        self.skip.combo.set_values(skip_names)
        self.shown.set_values([murderer, weapon, room])
        for combo in self.shown, self.answerer, self.skip.combo:
            if combo.index() == -1:
                combo.set("")

        for widget in self.guesser, self.character, self.weapon, self.location, self.answerer, self.shown, \
                      self.skip, self.confirm:
            widget.state(['!disabled' if self.guesser.values() else 'disabled'])

        self.confirm.state(['!disabled'
                            if guesser and murderer and weapon and room and self.shown.get()
                            else 'disabled'])
        self.shown.state(['!disabled' if murderer and weapon and room else 'disabled'])

    def update_skips(self):
        guesser = self.guesser.get()
        answerer = self.answerer.get()

    def on_players_changed(self):
        names = [player.name for player in self.controller.players()]
        self.guesser.set_values(names)
        self.validate_state()