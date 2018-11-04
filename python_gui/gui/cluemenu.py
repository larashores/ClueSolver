import tkinter as tk
from tkinter import ttk


from python_gui.signal import Signal


class ClueMenu(tk.Menu):
    def __init__(self, *args, **kwargs):
        tk.Menu.__init__(self, *args, **kwargs)

        self.signal_new = Signal()
        self.signal_add = Signal()
        self.signal_remove = Signal()
        self.signal_edit_overrides = Signal()

        file = tk.Menu(self, tearoff=0)
        file.add_command(label='New', accelerator='Ctrl+N', command=self.signal_new)
        file.add_command(label='Open...', accelerator='Ctrl+O')
        file.add_command(label='Save', accelerator='Ctrl+S')
        file.add_command(label='Save as...', accelerator='Ctrl+Alt+S')
        file.add_separator()
        file.add_command(label='Exit', accelerator='Alt+F4')
        self.add_cascade(label='File', menu=file)

        edit = tk.Menu(self, tearoff=0)
        edit.add_command(label='Add Player', command=self.signal_add)
        edit.add_command(label='Remove Player', command=self.signal_remove)
        edit.add_command(label='Overrides', command=self.signal_edit_overrides)
        self.add_cascade(label='Edit', menu=edit)
