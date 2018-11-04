import tkinter as tk
from tkinter import ttk

from python_gui.gui.popupwindow import PopupWindow
from python_gui.gui.addplayer.askname import AskName
from python_gui.gui.addplayer.asknumcards import AskNumCards
from python_gui.gui.addplayer.askknowscards import AskKnowsCards
from python_gui.gui.new.askcards import AskCards
from python_gui.gui.new.askorder import AskOrder


class AddPlayerWidget(PopupWindow):
    def __init__(self, *args, **kwargs):
        PopupWindow.__init__(self, *args, **kwargs)
        self.player_name_widget = AskName(self.frame, controller=self.controller)
        self.player_name_widget.set_confirm_command(self.on_confirm_name)
        self.player_name_widget.pack()

    def on_confirm_name(self):
        self.player_name_widget.destroy()
        self.ask_knows_cards_widget = AskKnowsCards(self.frame)
        self.ask_knows_cards_widget.set_confirm_command(self.on_confirm_knows_cards)
        self.ask_knows_cards_widget.pack()


    def on_confirm_knows_cards(self):
        self.ask_knows_cards_widget.destroy()
        if self.ask_knows_cards_widget.get_knows_cards():
            self.ask_cards_widget = AskCards(self.frame, num_cards=None, controller=self.controller)
            self.ask_cards_widget.set_confirm_command(self.on_confirm_cards)
            self.ask_cards_widget.pack()
        else:
            self.ask_num_cards_widget = AskNumCards(self.frame, name=self.player_name_widget.get_name(),
                                                    controller=self.controller)
            self.ask_num_cards_widget.set_confirm_command(self.on_confirm_num_cards)
            self.ask_num_cards_widget.pack()

    def on_confirm_num_cards(self):
        self.ask_num_cards_widget.destroy()
        self.controller.add_player(self.player_name_widget.get_name(), self.ask_num_cards_widget.get_num_cards())
        self.ask_order()

    def on_confirm_cards(self):
        self.ask_cards_widget.destroy()
        player = self.controller.add_player(self.player_name_widget.get_name(),
                                            len(self.ask_cards_widget.get_selected()))
        for card in self.ask_cards_widget.get_selected():
            self.controller.add_override(player, card, True)
        self.ask_order()

    def ask_order(self):
        self.ask_order_widget = AskOrder(self.frame, self.controller.players())
        self.ask_order_widget.set_confirm_command(self.on_confirm_order)
        self.ask_order_widget.pack()

    def on_confirm_order(self):
        self.controller.set_order(self.ask_order_widget.get_choices())
        self.ask_order_widget.destroy()
        self.destroy()
        self.controller.signal_players_changed()
        self.controller.signal_update_analytics()