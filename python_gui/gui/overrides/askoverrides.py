from python_gui.gui.carddisplay import CardDisplay
from python_gui.gui.tristatusbutton import TriStatusButton

import tkinter as tk
from tkinter import ttk

class AskOverrides(ttk.Frame):
    def __init__(self, parent, *, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.display = CardDisplay(self, columns=self.controller.num_players(), controller=controller)
        self.button_confirm = ttk.Button(self, text='Confirm')

        self.display.pack()
        self.button_confirm.pack(pady=(5, 0))

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
        for cards, grid in ((deck.people(), self.display.people),
                            (deck.weapons(), self.display.weapons),
                            (deck.rooms(), self.display.rooms)):
            for i, card in enumerate(cards):
                cards_to_button_row[card] = grid.get_button_row(i)
        for ind, player in enumerate(self.controller.overrides()):
            override_list = self.controller.overrides()[player]
            for card, is_positive in override_list:
                cards_to_button_row[card][ind].set_status(TriStatusButton.Status.YES
                                                          if is_positive
                                                          else TriStatusButton.Status.NO)