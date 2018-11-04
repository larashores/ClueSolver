import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning


class AskName(ttk.Frame):
    def __init__(self, *args, controller, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller
        default_name = 'Player {}'.format(self.controller.num_players()+1)

        self.var = tk.StringVar(self)
        self.var.set(default_name)
        question_lbl = ttk.Label(self, text='What is the player name?', style='Subtitle.TLabel')
        lbl = ttk.Label(self, text=default_name)
        entry = ttk.Entry(self, textvariable=self.var, justify=tk.CENTER)
        self.button_confirm = ttk.Button(self, text='Confirm')

        question_lbl.grid(column=1, row=1, columnspan=2)
        lbl.grid(column=1, row=2, pady=5, padx=(0, 6), sticky=tk.E)
        entry.grid(column=2, row=2, pady=5, padx=(6, 0), sticky=tk.W)
        self.button_confirm.grid(column=1, row=3, columnspan=2, pady=(5, 0))

    def set_confirm_command(self, func):
        def confirm_func():
            names = [player.name for player in self.controller.players()]
            if len(set(names)) == len(names):
                func()
            else:
                showwarning(title='Warning', message='Name is already taken')
        self.button_confirm.config(command=confirm_func)

    def get_name(self):
        return self.var.get()