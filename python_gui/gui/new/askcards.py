import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from python_gui.gui.buttongrid import ButtonGrid
from python_gui.gui.tristatusbutton import TriStatusButton


class AskCards(ttk.Frame):
    def __init__(self, *args, game, num_cards, **kwargs):
        self.game = game

        ttk.Frame.__init__(self, *args, **kwargs)
        self.num_cards = num_cards
        label = ttk.Label(self, text='Please select your cards', style='Subtitle.TLabel')
        self.people = ButtonGrid(self, 1, [person.name for person in self.game.deck.people()])
        self.weapons = ButtonGrid(self, 1, [weapon.name for weapon in self.game.deck.weapons()])
        self.rooms = ButtonGrid(self, 1, [room.name for room in self.game.deck.rooms()])
        self.button_confirm = ttk.Button(self, text='Confirm')

        def func(button):
            button.set_status(TriStatusButton.Status.BLANK
                              if button.get_status() == TriStatusButton.Status.YES
                              else TriStatusButton.Status.YES)

        for button_grid in self.people, self.weapons, self.rooms:
            button_grid.set_button_command(func)

        label.grid(column=1, row=1)
        self.people.grid(column=1, row=2)
        self.weapons.grid(column=1, row=3, pady=10)
        self.rooms.grid(column=1, row=4)
        self.button_confirm.grid(column=1, row=5, pady=10)

    def get_selected(self):
        card_list = []
        pairs = [(self.game.deck.people(), self.people),
                 (self.game.deck.weapons(), self.weapons),
                 (self.game.deck.rooms(), self.rooms)]
        for cards, widget in pairs:
            for card, state in zip(cards, widget.get_statuses_from_column(0)):

                if state == TriStatusButton.Status.YES:
                    card_list.append(card)

        return card_list

    def set_confirm_command(self, func):
        def get_statuses(button_grid):
            return [(1 if status == TriStatusButton.Status.YES else 0)
                    for status in button_grid.get_statuses_from_column(0)]

        def confirm_func():
            yeses = sum(get_statuses(self.people)) + sum(get_statuses(self.weapons)) + sum(get_statuses(self.rooms))
            if yeses == self.num_cards:
                func()
            else:
                showwarning(title='Warning', message='Please select {} cards.'.format(self.num_cards))
        self.button_confirm.config(command=confirm_func)