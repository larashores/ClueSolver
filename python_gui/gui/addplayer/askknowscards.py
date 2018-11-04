import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from python_gui.constants import total_cards
from python_gui.integercheck import int_validate


class AskKnowsCards(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self._knows_cards = False

        button_frm = ttk.Frame(self)
        self.button_yes = ttk.Button(button_frm, text='Yes')
        self.button_no = ttk.Button(button_frm, text='No')
        question_lbl = ttk.Label(self, text='Do you know the cards of this player?', style='Subtitle.TLabel')

        question_lbl.pack()
        button_frm.pack(pady=(5, 0))
        self.button_yes.pack(side=tk.LEFT, padx=(0, 6))
        self.button_no.pack(side=tk.LEFT, padx=(6, 0))

    def set_confirm_command(self, func):
        def yes_func():
            self._knows_cards = True
            func()
        def no_func():
            self._knows_cards = False
            func()
        self.button_yes.config(command=yes_func)
        self.button_no.config(command=no_func)

    def get_knows_cards(self):
        return self._knows_cards
