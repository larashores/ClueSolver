import tkinter as tk
from tkinter import ttk


class AskActivePlayer(ttk.Frame):
    def __init__(self, *args, names, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        lbl = ttk.Label(self, text='Which player are you?', style='Subtitle.TLabel')
        self._var = tk.StringVar(self)
        self.combobox = ttk.Combobox(self, textvariable=self._var, justify=tk.CENTER, values=names)
        self.button_confirm = ttk.Button(self, text='Confirm')
        self._var.set(names[0])

        self.combobox.state(['readonly'])

        lbl.pack()
        self.combobox.pack(pady=10)
        self.button_confirm.pack()

    def set_confirm_command(self, func):
        self.button_confirm.config(command=func)

    def get_active_player(self):
        return self._var.get()
