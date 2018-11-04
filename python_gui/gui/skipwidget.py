import tkinter as tk
from tkinter import ttk

from python_gui.gui.combolabel import ComboLabel
from python_gui.gui.listchoice import ListChoice

class SkipWidget(ttk.Frame):
    def __init__(self, parent, *, controller, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.controller = controller
        self.combo = ComboLabel(self, text='Skipped Players')
        self.lbox = ListChoice(self)
        self.button_apply = ttk.Button(self, text='Add')

        self.combo.state(['readonly'])

        self.combo.pack()
        self.lbox.pack(pady=5)
        self.button_apply.pack()

    def state(self, *args, **kwargs):
        for widget in self.combo, self.lbox, self.button_apply:
            widget.state(*args, **kwargs)


if __name__ == '__main__':
    root = tk.Tk()
    widget = SkipWidget(root, controller=None)
    widget.pack()
    root.mainloop()