from tkinter import ttk
import tkinter as tk

from python_gui.gui.buttongrid import ButtonGrid
from python_gui.gui.tristatusbutton import TriStatusButton

class CardDisplay(ttk.Frame):
    def __init__(self, *args, columns, controller, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller
        deck = self.controller.deck()
        self.controller.signal_players_changed.connect(self.regrid)
        self.controller.signal_update_analytics.connect(self.update_buttons)
        self.people = ButtonGrid(self, columns, deck.people(), [str(i + 1) for i in range(columns)])
        self.weapons = ButtonGrid(self, columns, deck.weapons())
        self.rooms = ButtonGrid(self, columns, deck.rooms())

        self.people.pack()
        self.weapons.pack(pady=10)
        self.rooms.pack()

    def regrid(self):
        columns = self.controller.num_players()
        self.people.regrid(columns, [str(i + 1) for i in range(columns)])
        self.weapons.regrid(columns)
        self.rooms.regrid(columns)

    def update_buttons(self):
        cards_to_button_row = {}
        deck = self.controller.deck()
        for cards, grid in ((deck.people(), self.people),
                            (deck.weapons(), self.weapons),
                            (deck.rooms(), self.rooms)):
            for i, card in enumerate(cards):
                cards_to_button_row[card] = grid.get_button_row(i)
        stat_map = self.controller.stats()
        for ind, player in enumerate(self.controller.players()):
            if player in stat_map:
                stats = stat_map[player]
                for card in stats.positives():
                    cards_to_button_row[card][ind].set_status(TriStatusButton.Status.YES)
                for card in stats.negatives():
                    cards_to_button_row[card][ind].set_status(TriStatusButton.Status.NO)