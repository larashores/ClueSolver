import tkinter as tk
from tkinter import ttk

from python_gui.gui.addplayer.askname import AskName
from python_gui.gui.addplayer.asknumcards import AskNumCards
from python_gui.gui.addplayer.askknowscards import AskKnowsCards
from python_gui.gui.new.askcards import AskCards
from python_gui.gui.new.askorder import AskOrder


class PopupWindow(tk.Toplevel):
    def __init__(self, *args, controller, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.controller = controller
        self.wm_title('Add Player Widget')
        self.wm_resizable(False, False)
        self.protocol('WM_DELETE_WINDOW')
        self.grab_set()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
