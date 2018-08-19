import tkinter as tk
from tkinter import ttk

from python_gui.integercheck import int_validate

_MIN = 2
_MAX = 8


class AskPlayers(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        lbl = ttk.Label(self, text='How many players are there?', style='Subtitle.TLabel')
        self.var = tk.IntVar(self)
        self.var.set(2)
        spinbox = ttk.Spinbox(self, textvariable=self.var, from_=_MIN, to_=_MAX, justify=tk.CENTER)
        self.button = ttk.Button(self, text='Confirm')

        int_validate(spinbox, limits=(_MIN, _MAX))

        lbl.pack()
        spinbox.pack(pady=10)
        self.button.pack()


def ask_players(parent=None):
    top = tk.Toplevel(parent)
    ask = AskPlayers(top)
    ask.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    ask.button.config(command=ask.quit)
    ask.mainloop()
    return ask.var.get()
