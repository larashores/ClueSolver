from tkinter import ttk
import tkinter as tk

from PIL import Image, ImageTk

from python_gui.gui.tristatebutton import TriStateButton
from python_gui.constants import people, weapons, rooms
from python_gui.gui.listchoice import ListChoice


class ClueGui(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.left = ttk.Frame(self)
        self.right = ListChoice(self, width=100)
        self.people, self.people_buttons = self.create_button_grid(people, 4)
        self.rooms, self.room_buttons = self.create_button_grid(rooms, 4)
        self.weapons, self.weapon_buttons = self.create_button_grid(weapons, 4)

        self.left.pack(side=tk.LEFT)
        self.people.pack(pady=(0, 5))
        self.rooms.pack(pady=5)
        self.weapons.pack(pady=(5, 0))
        self.right.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH, padx=(5, 0), pady=(5, 0))

    def create_button_grid(self, row_names, columns):
        buttons = []
        frame = ttk.Frame(self.left)
        for i, name in enumerate(row_names):
            buttons.append([])
            row_frame = ttk.Frame(frame)
            row_frame.pack()
            ttk.Label(row_frame, text=name, width=15, anchor=tk.E).pack(side=tk.LEFT)
            for j in range(columns):
                button = TriStateButton(row_frame)
                button.config(command=lambda b=button: b.toggle())
                buttons[i].append(button)
                button.pack(side=tk.LEFT)
        return frame, buttons
