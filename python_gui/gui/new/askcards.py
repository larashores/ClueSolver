import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from python_gui.gui.buttongrid import ButtonGrid
from python_gui.gui.tristatusbutton import TriStatusButton


class AskCards(ttk.Frame):
    def __init__(self, *args, controller, num_cards, **kwargs):
        self.controller = controller
        ttk.Frame.__init__(self, *args, **kwargs)
        self.num_cards = num_cards
        label = ttk.Label(self, text='Please select the cards', style='Subtitle.TLabel')
        deck = self.controller.deck()
        self.people = ButtonGrid(self, 1, [person.name for person in deck.people()])
        self.weapons = ButtonGrid(self, 1, [weapon.name for weapon in deck.weapons()])
        self.rooms = ButtonGrid(self, 1, [room.name for room in deck.rooms()])
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
        deck = self.controller.deck()
        pairs = [(deck.people(), self.people),
                 (deck.weapons(), self.weapons),
                 (deck.rooms(), self.rooms)]
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
            for card in self.get_selected():
                for player, cards in self.controller.positive_overrides().items():
                    if card in cards:
                        showwarning(title='Warning', message="Card '{}' already taken".format(card))
                        return
            yeses = sum(get_statuses(self.people) + get_statuses(self.weapons) + get_statuses(self.rooms))
            if (self.num_cards is None and yeses < self.controller.available_cards()) or (yeses == self.num_cards):
                func()
            else:
                showwarning(title='Warning', message='Please select {} cards.'.format(self.num_cards))
        self.button_confirm.config(command=confirm_func)