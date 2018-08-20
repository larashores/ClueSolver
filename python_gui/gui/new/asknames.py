import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning


class AskNames(ttk.Frame):
    def __init__(self, *args, num_names, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self._vars = []
        self.button_confirm = ttk.Button(self, text='Confirm')
        question_lbl = ttk.Label(self, text='What are the player names?', style='Subtitle.TLabel')
        question_lbl.grid(column=1, row=1, columnspan=2)
        for i in range(num_names):
            var = tk.StringVar(self)
            self._vars.append(var)
            default = 'Player {}'.format(i+1)
            lbl = ttk.Label(self, text=default)
            entry = ttk.Entry(self, textvariable=var, justify=tk.CENTER)
            var.set(default)

            lbl.grid(column=1, row=i+2, pady=5, padx=(0, 6), sticky=tk.E)
            entry.grid(column=2, row=i+2, pady=5, padx=(6, 0), sticky=tk.W)
        self.button_confirm.grid(column=1, row=num_names + 3, columnspan=2, pady=(5, 0))

    def set_confirm_command(self, func):
        def confirm_func():
            names = self.get_names()
            if len(set(names)) == len(names):
                func()
            else:
                showwarning(title='Warning', message='Cannot have two of the same names')
        self.button_confirm.config(command=confirm_func)

    def get_names(self):
        return [var.get().strip() for var in self._vars]