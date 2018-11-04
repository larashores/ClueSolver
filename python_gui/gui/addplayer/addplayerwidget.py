import tkinter as tk
from tkinter import ttk

from python_gui.gui.addplayer.askname import AskName
from python_gui.gui.addplayer.asknumcards import AskNumCards
from python_gui.gui.addplayer.askknowscards import AskKnowsCards
from python_gui.gui.new.askcards import AskCards
from python_gui.gui.new.askorder import AskOrder


class AddPlayerWidget(tk.Toplevel):
    def __init__(self, *args, controller, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.controller = controller
        self.wm_title('Add Player Widget')
        self.wm_resizable(False, False)
        self.protocol('WM_DELETE_WINDOW')
        self.grab_set()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

        self.num_cards = -1

        self.player_name_widget = AskName(self.frame, controller=controller)
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
        self.num_cards = self.ask_num_cards_widget.get_num_cards()
        self.ask_order()

    def on_confirm_cards(self):
        self.ask_cards_widget.destroy()
        self.num_cards = len(self.ask_cards_widget.get_selected())
        self.ask_order()

    def ask_order(self):
        self.controller.add_player(self.player_name_widget.get_name(), self.num_cards)
        self.ask_order_widget = AskOrder(self.frame, self.controller.players())
        self.ask_order_widget.set_confirm_command(self.on_confirm_order)
        self.ask_order_widget.pack()

    def on_confirm_order(self):
        self.controller.set_order(self.ask_order_widget.get_choices())
        self.ask_order_widget.destroy()
        self.destroy()
        self.controller.signal_players_changed()