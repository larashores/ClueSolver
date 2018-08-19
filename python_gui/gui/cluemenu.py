import tkinter as tk
from tkinter import ttk


from python_gui.signal import Signal


class ClueMenu(tk.Menu):
    def __init__(self, *args, **kwargs):
        tk.Menu.__init__(self, *args, **kwargs)

        self.signal_new = Signal()

        file = tk.Menu(self, tearoff=0)
        file.add_command(label='New', accelerator='Ctrl+N', command=self.signal_new)
        file.add_command(label='Open...', accelerator='Ctrl+O')
        file.add_command(label='Save', accelerator='Ctrl+S')
        file.add_command(label='Save as...', accelerator='Ctrl+Alt+S')
        file.add_separator()
        file.add_command(label='Exit', accelerator='Alt+F4')
        self.add_cascade(label='File', menu=file)
