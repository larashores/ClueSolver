import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from python_gui.constants import total_cards
from python_gui.integercheck import int_validate


class AskNumCards(ttk.Frame):
    def __init__(self, parent, *, name, controller, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.controller = controller
        num_players = self.controller.num_players()
        from_ = 0
        to_ = self.controller.available_cards()
        default = ((total_cards - 3) // num_players) - 1 if num_players else to_
        default = default if default < to_ else to_

        self.var = tk.IntVar(self)
        button_frm = ttk.Frame(self)
        self.button_confirm = ttk.Button(button_frm, text='Confirm')
        self.button_skip = ttk.Button(button_frm, text='Skip')
        question_lbl = ttk.Label(self, text='How many cards does the player have?', style='Subtitle.TLabel')
        entry_frm = ttk.Frame(self)
        lbl = ttk.Label(entry_frm, text=name)
        entry = ttk.Spinbox(entry_frm, textvariable=self.var, justify=tk.CENTER, from_=from_, to_=to_)
        self.var.set(default)
        int_validate(entry, limits=(from_, to_))

        question_lbl.pack()
        entry_frm.pack(pady=5)
        lbl.pack(side=tk.LEFT, padx=(0, 6))
        entry.pack(side=tk.LEFT, padx=(6, 0))
        button_frm.pack(pady=(5, 0))
        self.button_confirm.pack(side=tk.LEFT, padx=(0, 6))
        self.button_skip.pack(side=tk.LEFT, padx=(6, 0))

    def set_confirm_command(self, func):
        def confirm_func():
            if self.get_num_cards() <= self.controller.available_cards():
                func()
            else:
                showwarning(title='Warning',
                            message='Total number of cards must be less than {}.'.format(
                                self.controller.available_cards()))
        def skip_func():
            self.var.set(-1)
            func()
        self.button_confirm.config(command=confirm_func)
        self.button_skip.config(command=skip_func)

    def get_num_cards(self):
        return self.var.get()

