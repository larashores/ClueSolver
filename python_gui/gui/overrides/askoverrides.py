from python_gui.gui.carddisplay import CardDisplay
from python_gui.gui.tristatusbutton import TriStatusButton

import tkinter as tk
from tkinter import ttk

class AskOverrides(ttk.Frame):
    def __init__(self, parent, *, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.display = CardDisplay(self, columns=self.controller.num_players(), controller=controller)
        self.controller.signal_update_analytics.disconnect(self.display.update_buttons)
        self.controller.signal_players_changed.disconnect(self.display.regrid)
        self.button_confirm = ttk.Button(self, text='Confirm')

        self.display.pack()
        self.button_confirm.pack(pady=(5, 0))


        self.card_pairs = ((self.controller.deck().people(), self.display.people),
                           (self.controller.deck().weapons(), self.display.weapons),
                           (self.controller.deck().rooms(), self.display.rooms))
        self.initial_buttons()

        def func(button):
            if button.get_status() == TriStatusButton.Status.BLANK:
                status = TriStatusButton.Status.YES
            elif button.get_status() == TriStatusButton.Status.YES:
                status = TriStatusButton.Status.NO
            elif button.get_status() == TriStatusButton.Status.NO:
                status = TriStatusButton.Status.BLANK
            button.set_status(status)

        for button_grid in self.display.people, self.display.weapons, self.display.rooms:
            button_grid.set_button_command(func)

    def initial_buttons(self):
        cards_to_button_row = {}
        deck = self.controller.deck()
        for cards, grid in self.card_pairs:
            for i, card in enumerate(cards):
                cards_to_button_row[card] = grid.get_button_row(i)
        for ind, player in enumerate(self.controller.overrides()):
            override_list = self.controller.overrides()[player]
            for card, is_positive in override_list:
                cards_to_button_row[card][ind].set_status(TriStatusButton.Status.YES
                                                          if is_positive
                                                          else TriStatusButton.Status.NO)

    def get_selected(self):
        player_to_cards = {}
        for ind, player in enumerate(self.controller.players()):
            player_to_cards[player] = []
            for cards, widget in self.card_pairs:
                for card, state in zip(cards, widget.get_statuses_from_column(ind)):
                    if state == TriStatusButton.Status.YES:
                        player_to_cards[player].append((card, True))
                    elif state == TriStatusButton.Status.NO:
                        player_to_cards[player].append((card, False))
        return player_to_cards

    def set_confirm_command(self, func):
        self.button_confirm.config(command=func)