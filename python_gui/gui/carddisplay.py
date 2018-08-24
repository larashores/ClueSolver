from tkinter import ttk
import tkinter as tk

from python_gui.gui.buttongrid import ButtonGrid

class CardDisplay(ttk.Frame):
    def __init__(self, *args, columns, game, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.people = ButtonGrid(self, columns, game.deck.people(), [str(i + 1) for i in range(columns)])
        self.weapons = ButtonGrid(self, columns, game.deck.weapons())
        self.rooms = ButtonGrid(self, columns, game.deck.rooms())

        self.people.pack()
        self.weapons.pack(pady=10)
        self.rooms.pack()

    def regrid(self, columns):
        self.people.regrid(columns, [str(i + 1) for i in range(columns)])
        self.weapons.regrid(columns)
        self.rooms.regrid(columns)

    def update_buttons(self, game):
        cards_to_button_row = {}
        for cards, grid in ((game.deck.people(), self.people),
                            (game.deck.weapons(), self.weapons),
                            (game.deck.rooms(), self.rooms)):
            for i, card in enumerate(cards):
                cards_to_button_row[card] = grid.get_button_row(i)
        stat_map = game.analyzer.stats()
        for ind, player in enumerate(game.get_players()):
            if player in stat_map:
                stats = stat_map[player]
                for card in stats.positives():
                    cards_to_button_row[card][ind].set_status(TriStatusButton.Status.YES)
                for card in stats.negatives():
                    cards_to_button_row[card][ind].set_status(TriStatusButton.Status.NO)