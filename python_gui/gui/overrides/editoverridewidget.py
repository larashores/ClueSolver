import tkinter as tk
from tkinter import ttk

from python_gui.gui.popupwindow import PopupWindow
from python_gui.gui.overrides.askoverrides import AskOverrides


class EditOverrideWidget(PopupWindow):
    def __init__(self, *args, **kwargs):
        PopupWindow.__init__(self, *args, **kwargs)

        self.ask_override_widget = AskOverrides(self.frame, controller=self.controller)
        self.ask_override_widget.pack()

    def on_confirm_overrides(self):
        self.ask_override_widget.destroy()
        pass
