from python_gui.gui.carddisplay import CardDisplay

import tkinter as tk
from tkinter import ttk

class AskOverrides(ttk.Frame):
    def __init__(self, parent, *, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.display = CardDisplay(self, columns=self.controller.num_players(), controller=controller)
        self.button_confirm = ttk.Button(self, text='Confirm')

        self.display.pack()
        self.button_confirm.pack(pady=(5, 0))