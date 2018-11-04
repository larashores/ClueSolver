import tkinter as tk
from tkinter import ttk

from python_gui.gui.popupwindow import PopupWindow
from python_gui.gui.overrides.askoverrides import AskOverrides


class EditOverrideWidget(PopupWindow):
    def __init__(self, *args, **kwargs):
        PopupWindow.__init__(self, *args, **kwargs)

        self.ask_override_widget = AskOverrides(self.frame, controller=self.controller)
        self.ask_override_widget.set_confirm_command(self.on_confirm_overrides)
        self.ask_override_widget.pack()

    def on_confirm_overrides(self):
        self.ask_override_widget.destroy()
        self.destroy()
        self.controller.clear_overrides()
        for player, override_list in self.ask_override_widget.get_selected().items():
            for card, is_positive in override_list:
                self.controller.add_override(player, card, is_positive)
        self.controller.signal_update_analytics()
