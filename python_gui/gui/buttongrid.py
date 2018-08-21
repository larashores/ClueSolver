from tkinter import ttk
import tkinter as tk

from python_gui.gui.tristatusbutton import TriStatusButton


class ButtonGrid(ttk.Frame):
    def __init__(self, parent=None, columns=0, row_names=list(), column_names=list(), **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self._button_rows = [[] for _ in range(len(row_names))]
        for i, name in enumerate(row_names):
            ttk.Label(self, text=name, width=15, anchor=tk.E).grid(row=i+2, column=1)
        for j, name in enumerate(column_names):
            ttk.Label(self, text=name, style='Subtitle.TLabel').grid(row=1, column=j+2)
        for j in range(columns):
            for i in range(len(row_names)):
                button = TriStatusButton(self)
                button.grid(row=i+2, column=j+2)
                self._button_rows[i].append(button)

    def get_statuses_from_column(self, col):
        return [row[col].get_status() for row in self._button_rows]

    def set_button_command(self, func):
        for row in self._button_rows:
            for button in row:
                button.config(command=lambda b=button: func(b))
