from tkinter import ttk
from PIL import Image, ImageTk
import enum

from python_gui.resources import check_png, cross_png, empty_png


class State(enum.Enum):
    NO = -1
    BLANK = 0
    YES = 1


class TriStateButton(ttk.Button):
    def __init__(self, *args, **kwargs):
        self.check = ImageTk.PhotoImage(Image.open(check_png))
        self.cross = ImageTk.PhotoImage(Image.open(cross_png))
        self.empty = ImageTk.PhotoImage(Image.open(empty_png))
        ttk.Button.__init__(self, *args, image=self.empty, **kwargs)

        self.state = State.BLANK

    def toggle(self):
        if self.state == State.BLANK:
            self.state = State.YES
            self.config(image=self.check)
        elif self.state == State.YES:
            self.state = State.NO
            self.config(image=self.cross)
        elif self.state == State.NO:
            self.state = State.BLANK
            self.config(image=self.empty)
