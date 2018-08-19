import tkinter as tk
from tkinter import ttk

from python_gui.constants import total_cards


class AskCards(ttk.Frame):
    def __init__(self, parent, names, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.vars = []
        self.button = ttk.Button(self, text='Confirm')
        question_lbl = ttk.Label(self, text='How many cards does each player have?', style='Subtitle.TLabel')
        for i, name in enumerate(names):
            var = tk.IntVar(self)
            self.vars.append(var)
            lbl = ttk.Label(self, text=name)
            entry = ttk.Spinbox(self, textvariable=var, justify=tk.CENTER)
            var.set(total_cards // len(names))

            lbl.grid(column=1, row=i+2, pady=5)
            entry.grid(column=2, row=i+2, pady=5)
        question_lbl.grid(column=1, row=1, columnspan=2)
        self.button.grid(column=1, row=len(names)+3, columnspan=2, pady=(5, 0))


def ask_cards(parent, names=list()):
    top = tk.Toplevel(parent)
    ask = AskCards(top, names)
    ask.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    ask.button.config(command=ask.quit)
    ask.mainloop()
    return [var.get() for var in ask.vars]