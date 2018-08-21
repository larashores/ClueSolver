from tkinter import ttk
from PIL import Image, ImageTk
import enum

from python_gui.resources import check_png, cross_png, empty_png


class TriStatusButton(ttk.Button):

    class Status(enum.Enum):
        NO = -1
        BLANK = 0
        YES = 1

    def __init__(self, *args, **kwargs):
        ttk.Button.__init__(self, *args, **kwargs)
        self._check = ImageTk.PhotoImage(Image.open(check_png))
        self._cross = ImageTk.PhotoImage(Image.open(cross_png))
        self._empty = ImageTk.PhotoImage(Image.open(empty_png))
        self._status = TriStatusButton.Status.BLANK
        self.config(image=self._empty)

    def get_status(self):
        return self._status

    def set_status(self, state):
        self._status = state
        Status = TriStatusButton.Status
        if state == Status.BLANK:
            self.config(image=self._empty)
        elif state == Status.YES:
            self.config(image=self._check)
        elif state == Status.NO:
            self.config(image=self._cross)

    def toggle(self):
        Status = TriStatusButton.Status
        if self._status == Status.BLANK:
            self.set_status(Status.YES)
        elif self._status == Status.YES:
            self.set_status(Status.NO)
        elif self._status == Status.NO:
            self.set_status(Status.BLANK)
