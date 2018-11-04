import tkinter as tk
from tkinter import ttk

from python_gui.gui.addplayer.askname import AskName


class AddPlayerWidget(tk.Toplevel):
    def __init__(self, *args, controller, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.controller = controller
        self.wm_title('Add Player Widget')
        self.wm_resizable(False, False)
        self.protocol('WM_DELETE_WINDOW')
        self.grab_set()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

        self.num_players_widget = AskName(self.frame, controller=controller)
        self.num_players_widget.set_confirm_command(self.on_confirm_name)
        self.num_players_widget.pack()

    def on_confirm_name(self):
        pass
