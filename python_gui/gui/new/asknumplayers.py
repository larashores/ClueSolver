import tkinter as tk
from tkinter import ttk

from python_gui.integercheck import int_validate

_MIN = 2
_MAX = 8


class AskNumPlayers(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        lbl = ttk.Label(self, text='How many players are there?', style='Subtitle.TLabel')
        self._var = tk.IntVar(self)
        self._var.set(2)
        spinbox = ttk.Spinbox(self, textvariable=self._var, from_=_MIN, to_=_MAX, justify=tk.CENTER)
        self.button_confirm = ttk.Button(self, text='Confirm')

        int_validate(spinbox, limits=(_MIN, _MAX))

        lbl.pack()
        spinbox.pack(pady=10)
        self.button_confirm.pack()

    def set_confirm_command(self, func):
        self.button_confirm.config(command=func)

    def get_num_players(self):
        return self._var.get()
