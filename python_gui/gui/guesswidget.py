from tkinter import ttk
import tkinter as tk

from python_gui.gui.skipwidget import SkipWidget
from python_gui.gui.combolabel import ComboLabel
from python_gui import constants

class GuessWidget(ttk.Frame):
    def __init__(self, *args, controller, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller
        deck = self.controller.deck()
        label = ttk.Label(self, text='Make Suggestion', style='Subtitle.TLabel')
        self.guesser = ComboLabel(self, text='Guessing Player?')
        self.character = ComboLabel(self, text='Murderer?', values=deck.people())
        self.weapon = ComboLabel(self, text='Weapon?', values=deck.weapons())
        self.location = ComboLabel(self, text='Room?', values=deck.rooms())
        self.answerer = ComboLabel(self, text='Answering Player?')
        self.shown = ComboLabel(self, text='Card Shown?')
        self.skip = SkipWidget(self, controller=controller)
        self.confirm = ttk.Button(self, text='Confirm', command=self.on_guess)

        for combo in self.guesser, self.answerer:
            combo._var.trace('w', lambda var, ind, op: self.update_skips())

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

        answerers = [player for player in self.controller.players() if player != self.guesser.get()]
        self.answerer.set_values([''] + answerers)
        self.shown.set_values(['', murderer, weapon, room])
        for combo in self.shown, self.answerer, self.skip.combo:
            if combo.index() == -1:
                combo.set("")

        for widget in self.guesser, self.character, self.weapon, self.location, self.answerer:
            widget.state(['!disabled' if self.guesser.values() else 'disabled'])
        self.skip.state(['!disabled' if self.guesser.get() else 'disabled'])
        self.confirm.state(['!disabled'
                            if guesser and murderer and weapon and room
                            else 'disabled'])
        self.shown.state(['!disabled' if murderer and weapon and room and self.answerer.get() else 'disabled'])

    def update_skips(self):
        guesser = self.guesser.get()
        answerer = self.answerer.get()

        skips = [player for player in self.controller.players()
                 if player != self.guesser.get() and player != self.answerer.get()]
        self.skip.set_values(skips)
        self.skip.lbox.clear()
        if guesser and answerer:
            players = self.controller.players()
            ind = players.index(guesser) + 1
            end = players.index(answerer)
            while ind != end:
                self.skip.add_to_lbox(players[ind])
                ind = (ind + 1) % len(players)
        elif guesser:
            for player in self.controller.players():
                if player != guesser:
                    self.skip.add_to_lbox(player)

    def on_players_changed(self):
        self.guesser.set_values(self.controller.players())
        self.validate_state()

    def on_guess(self):
        guesser = self.guesser.get()
        answer = self.answerer.get() if self.answerer.get() else None
        skipped = [player for player in self.skip.lbox]
        murderer = self.character.get()
        weapon = self.weapon.get()
        room = self.location.get()
        card = self.shown.get() if self.shown.get() else None
        self.controller.add_guess(guesser, answer, skipped, murderer, weapon, room, card)
        self.controller.signal_update_analytics()

        for combo in self.guesser, self.answerer, self.character, self.weapon, self.location, self.shown:
            combo.set('')
        self.update_skips()
        self.validate_state()