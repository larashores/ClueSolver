import tkinter as tk
from tkinter import ttk

from tkinter.messagebox import showwarning

from python_gui.constants import total_cards
from python_gui.integercheck import int_validate


class AskCards(ttk.Frame):
    def __init__(self, parent, names, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.vars = []
        self.button = ttk.Button(self, text='Confirm')
        question_lbl = ttk.Label(self, text='How many cards does each player have?', style='Subtitle.TLabel')
        from_ = 0
        to_ = ((total_cards - 3) // len(names)) + 1
        for i, name in enumerate(names):
            var = tk.IntVar(self)
            self.vars.append(var)
            lbl = ttk.Label(self, text=name)
            entry = ttk.Spinbox(self, textvariable=var, justify=tk.CENTER, from_=from_, to_=to_)
            var.set(to_ - 1)
            int_validate(entry, limits=(from_, to_))

            lbl.grid(column=1, row=i+2, pady=5, padx=(0, 6), sticky=tk.E)
            entry.grid(column=2, row=i+2, pady=5, padx=(6, 0), sticky=tk.W)
        question_lbl.grid(column=1, row=1, columnspan=2)
        self.button.grid(column=1, row=len(names)+3, columnspan=2, pady=(5, 0))

    def get_totals(self):
        return [var.get() for var in self.vars]

    def validate(self):
        total = sum(self.get_totals())
        return total <= (total_cards - 3)


def ask_cards(parent, names=list()):
    def quit():
        if ask.validate():
            parent.quit()
            ask.destroy()
        else:
            showwarning(title='Warning', message='Total number of cards must be less than {}.'.format(total_cards - 2))

    ask = AskCards(parent, names)
    ask.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    ask.button.config(command=quit)
    parent.mainloop()
    return ask.get_totals()
