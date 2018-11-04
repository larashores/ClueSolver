import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from python_gui.constants import total_cards
from python_gui.integercheck import int_validate


class AskWhichPlayer(ttk.Frame):
    def __init__(self, parent, *, controller, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.controller = controller
        players = [player.name for player in self.controller.players()]

        question_lbl = ttk.Label(self, text='Which player to remove?', style='Subtitle.TLabel')
        combo = ttk.Combobox(self, values=players)
        self.button_confirm = ttk.Button(self, text='Confirm')

        combo.state(['readonly'])

        question_lbl.pack()
        combo.pack(pady=5)
        self.button_confirm.pack()

    def set_confirm_command(self, func):
        def confirm_func():
            func()
        self.button_confirm.config(command=confirm_func)


