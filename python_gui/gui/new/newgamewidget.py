import tkinter as tk
from tkinter import ttk

from python_gui.gui.popupwindow import PopupWindow
from python_gui.gui.new.askorder import AskOrder
from python_gui.gui.new.asknumplayers import AskNumPlayers
from python_gui.gui.new.asknames import AskNames
from python_gui.gui.new.asknumcards import AskNumCards
from python_gui.gui.new.askactiveplayer import AskActivePlayer
from python_gui.gui.new.askcards import AskCards


class NewGameWidget(PopupWindow):
    def __init__(self, *args, **kwargs):
        PopupWindow.__init__(self, *args, **kwargs)

        self.num_players_widget = AskNumPlayers(self.frame)
        self.num_players_widget.set_confirm_command(self.on_confirm_num_players)
        self.num_players_widget.pack()

    def set_close_command(self, func):
        self.close_command = func

    def on_confirm_num_players(self):
        self.num_players_widget.destroy()
        self.ask_names_widget = AskNames(self.frame, num_names=self.num_players_widget.get_num_players())
        self.ask_names_widget.set_confirm_command(self.on_confirm_names)
        self.ask_names_widget.pack()

    def on_confirm_names(self):
        self.ask_names_widget.destroy()
        self.ask_order_widget = AskOrder(self.frame, names=self.ask_names_widget.get_names())
        self.ask_order_widget.set_confirm_command(self.on_confirm_order)
        self.ask_order_widget.pack()

    def on_confirm_order(self):
        self.ask_order_widget.gui.destroy()
        self.ask_num_cards_widget = AskNumCards(self.frame, self.ask_order_widget.get_choices())
        self.ask_num_cards_widget.set_confirm_command(self.on_confirm_num_cards)
        self.ask_num_cards_widget.pack()

    def on_confirm_num_cards(self):
        self.ask_num_cards_widget.destroy()
        self.ask_active_player_widget = AskActivePlayer(self.frame, names=self.ask_order_widget.get_choices())
        self.ask_active_player_widget.set_confirm_command(self.on_confirm_active_player)
        self.ask_active_player_widget.pack()

    def on_confirm_active_player(self):
        num_cards = self.ask_num_cards_widget.get_num_cards()[self.ask_active_player_widget.get_active_index()]
        self.ask_active_player_widget.destroy()
        self.ask_cards_widget = AskCards(self.frame, controller=self.controller, num_cards=num_cards)
        self.ask_cards_widget.set_confirm_command(self.on_confirm_cards)
        self.ask_cards_widget.pack()

    def on_confirm_cards(self):
        self.ask_cards_widget.destroy()
        self.destroy()

        for name, card, in zip(self.ask_order_widget.get_choices(), self.ask_num_cards_widget.get_num_cards()):
            self.controller.add_player(name, card)
        self.controller.signal_players_changed()

        player = self.controller.players()[self.ask_active_player_widget.get_active_index()]
        for card in self.ask_cards_widget.get_selected():
            self.controller.add_override(player, card, True)
        self.controller.signal_update_analytics()
