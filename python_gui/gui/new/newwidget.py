import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from python_gui.gui.orderer import Orderer
from python_gui.gui.new.asknumplayers import AskNumPlayers
from python_gui.gui.new.asknames import AskNames
from python_gui.gui.new.askcards import AskCards
from python_gui.gui.new.askplayer import AskPlayer
from python_gui.constants import total_cards


class NewGameWidget(tk.Toplevel):
    def __init__(self, *args, game, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.wm_title('New Game Creation')
        self.wm_resizable(False, False)
        self.protocol('WM_DELETE_WINDOW')
        self.grab_set()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

        self.num_players_widget = AskNumPlayers(self.frame)
        self.num_players_widget.button_confirm.config(command=self.on_confirm_num_players)
        self.num_players_widget.pack()

    def on_confirm_num_players(self):
        self.num_players_widget.destroy()
        self.ask_names_widget = AskNames(self.frame, num_names=self.num_players_widget.get_num_players())
        self.ask_names_widget.button_confirm.config(command=self.on_confirm_names)
        self.ask_names_widget.pack()

    def on_confirm_names(self):
        names = self.ask_names_widget.get_names()
        if len(set(names)) == len(names):
            self.ask_names_widget.destroy()
            self.ask_order_widget = Orderer(self.frame, names=self.ask_names_widget.get_names())
            self.ask_order_widget.gui.button_confirm.config(command=self.on_confirm_order)
            self.ask_order_widget.pack()
        else:
            showwarning(title='Warning', message='Cannot have two of the same names')

    def on_confirm_order(self):
        self.ask_order_widget.gui.destroy()
        self.ask_num_cards_widget = AskCards(self.frame, [name for name in self.ask_order_widget])
        self.ask_num_cards_widget.button_confirm.config(command=self.on_confirm_num_cards)
        self.ask_num_cards_widget.pack()

    def on_confirm_num_cards(self):
        if self.ask_num_cards_widget.validate():
            self.ask_num_cards_widget.destroy()
            self.ask_active_player_widget = AskPlayer(self.frame, names=[name for name in self.ask_order_widget])
            self.ask_active_player_widget.button_confirm.config(command=self.on_confirm_active_player)
            self.ask_active_player_widget.pack()
        else:
            showwarning(title='Warning', message='Total number of cards must be less than {}.'.format(total_cards - 2))

    def on_confirm_active_player(self):
        self.ask_active_player_widget.destroy()
        self.destroy()
