from tkinter import ttk
import tkinter as tk

class NameWidget(ttk.Frame):
    def __init__(self, *args, names=list(), **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        for i, name in enumerate(names):
            label = ttk.Label(self, text='{}) {}   '.format(i+1, name), style='Subtitle.TLabel')
            label.pack(side=tk.LEFT)