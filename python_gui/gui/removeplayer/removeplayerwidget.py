import tkinter as tk
from tkinter import ttk

from python_gui.gui.popupwindow import PopupWindow
from python_gui.gui.removeplayer.askwhichplayer import AskWhichPlayer


class RemovePlayerWidget(PopupWindow):
    def __init__(self, *args, **kwargs):
        PopupWindow.__init__(self, *args, **kwargs)

        self.player_name_widget = AskWhichPlayer(self.frame, controller=self.controller)
        self.player_name_widget.set_confirm_command(self.on_confirm_which_player)
        self.player_name_widget.pack()

    def on_confirm_which_player(self):
        self.player_name_widget.destroy()
        pass
