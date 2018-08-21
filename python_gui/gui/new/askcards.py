import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from python_gui.constants import people, weapons, rooms
from python_gui.gui.buttongrid import ButtonGrid


class AskCards(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        label = ttk.Label(self, text='Please select your cards', style='Subtitle.TLabel')
        self.people = ButtonGrid(self, 1, people)
        self.weapons = ButtonGrid(self, 1, weapons)
        self.rooms = ButtonGrid(self, 1, rooms)
        self.button_confirm = ttk.Button(self, text='Confirm')

        label.grid(column=1, row=1)
        self.people.grid(column=1, row=2)
        self.weapons.grid(column=1, row=3, pady=10)
        self.rooms.grid(column=1, row=4)
        self.button_confirm.grid(column=1, row=5, pady=10)

    def set_confirm_command(self, func):
        def confirm_func():
            if True:
                func()
            else:
                showwarning(title='Warning', message='Cannot have two of the same names')
        self.button_confirm.config(command=func)
