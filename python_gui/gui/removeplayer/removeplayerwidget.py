import tkinter as tk
from tkinter import ttk

from python_gui.gui.removeplayer.askwhichplayer import AskWhichPlayer


class RemovePlayerWidget(tk.Toplevel):
    def __init__(self, *args, controller, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.controller = controller
        self.wm_title('Remove Player Widget')
        self.wm_resizable(False, False)
        self.protocol('WM_DELETE_WINDOW')
        self.grab_set()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

        self.player_name_widget = AskWhichPlayer(self.frame, controller=controller)
        self.player_name_widget.set_confirm_command(self.on_confirm_which_player)
        self.player_name_widget.pack()

    def on_confirm_which_player(self):
        self.player_name_widget.destroy()
        pass
