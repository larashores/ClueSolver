import tkinter as tk
from tkinter import ttk


class AskPlayer(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        lbl = ttk.Label(self, text='Which player are you?', style='Subtitle.TLabel')
        self.var = tk.StringVar(self)
        self.combobox = ttk.Combobox(self, textvariable=self.var, justify=tk.CENTER)
        self.button = ttk.Button(self, text='Confirm')

        self.combobox.state(['readonly'])

        lbl.pack()
        self.combobox.pack(pady=10)
        self.button.pack()


def ask_player(parent, names):
    top = tk.Toplevel(parent)
    ask = AskPlayer(top)
    ask.combobox.config(values=names)
    ask.var.set(names[0])

    ask.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    ask.button.config(command=ask.quit)
    ask.mainloop()
    return ask.var.get()
