import tkinter as tk
from tkinter import ttk

from python_gui.gui.new.asknumplayers import ask_num_players
from python_gui.gui.new.asknames import ask_names
from python_gui.gui.new.askorder import ask_order
from python_gui.gui.new.askcards import ask_cards
from python_gui.gui.new.askplayer import ask_player


def ask_new(parent=None):
    destroyed = False

    def destroy():
        nonlocal destroyed
        if not destroyed:
            destroyed = True
            top.quit()
            top.destroy()

    top = tk.Toplevel(parent)
    top.wm_title('New Game Creation')
    top.wm_resizable(False, False)
    top.protocol('WM_DELETE_WINDOW', destroy)
    top.grab_set()
    num_players = ask_num_players(top)
    if not destroyed:
        names = ask_names(top, num_players)
    if not destroyed:
        ordered = ask_order(top, names)
    if not destroyed:
        cards = ask_cards(top, ordered)
    if not destroyed:
        ask_player(top, ordered)
    top.destroy()
