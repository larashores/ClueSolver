from tkinter import ttk
import tkinter as tk

from python_gui.gui.tristatebutton import TriStateButton


class ButtonGrid(ttk.Frame):
    def __init__(self, parent=None, columns=0, row_names=list(), column_names=list(), **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.buttons = [[] for row in range(len(row_names))]
        for i, name in enumerate(row_names):
            ttk.Label(self, text=name, width=15, anchor=tk.E).grid(row=i+2, column=1)
        for j, name in enumerate(column_names):
            ttk.Label(self, text=name, style='Subtitle.TLabel').grid(row=1, column=j+2)
        for j in range(columns):
            for i in range(len(row_names)):
                button = TriStateButton(self)
                button.config(command=lambda b=button: b.toggle())
                button.grid(row=i+2, column=j+2)
                self.buttons[i].append(button)
