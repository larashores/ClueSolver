import tkinter as tk
from tkinter import ttk

from python_gui.gui.overrides.askoverrides import AskOverrides


class EditOverrideWidget(tk.Toplevel):
    def __init__(self, *args, controller, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.controller = controller
        self.wm_title('Remove Player Widget')
        self.wm_resizable(False, False)
        self.protocol('WM_DELETE_WINDOW')
        self.grab_set()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

        self.ask_override_widget = AskOverrides(self.frame, controller=controller)
        self.ask_override_widget.pack()

    def on_confirm_overrides(self):
        self.ask_override_widget.destroy()
        pass
