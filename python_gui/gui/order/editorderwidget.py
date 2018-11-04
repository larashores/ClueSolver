import tkinter as tk
from tkinter import ttk

from python_gui.gui.popupwindow import PopupWindow
from python_gui.gui.new.askorder import AskOrder


class EditOrderWidget(PopupWindow):
    def __init__(self, *args, **kwargs):
        PopupWindow.__init__(self, *args, **kwargs)

        self.ask_order_widget = AskOrder(self.frame, self.controller.players())
        self.ask_order_widget.set_confirm_command(self.on_confirm_order)
        self.ask_order_widget.pack()

    def on_confirm_order(self):
        self.ask_order_widget.destroy()
        self.destroy()
        self.controller.set_order(self.ask_order_widget.get_choices())
        self.controller.signal_players_changed()
        pass
