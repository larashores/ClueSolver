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
        self.button_apply = ttk.Button(self, text='Add', command=self.on_add)
        self.lbox.signal_delete.connect(self.on_delete)

        self._original_values = []

        self.combo.state(['readonly'])

        self.combo.pack()
        self.lbox.pack(pady=5)
        self.button_apply.pack()

    def set_values(self, values):
        self._original_values = values
        self.combo.set_values(values)

    def clear_lboox(self):
        self.lbox.clear()

    def add_to_lbox(self, player):
        self.lbox.append(player)
        self.combo.set_values([value for value in self._original_values if value not in self.lbox])

        if self.combo.index() == -1:
            self.combo.set('')

    def on_add(self):
        ind = self.combo.index()
        if ind != -1:
            self.add_to_lbox(self.combo.values()[ind])

    def on_delete(self):
        self.lbox.pop(self.lbox.get_selection())
        self.combo.set_values([value for value in self._original_values if value not in self.lbox])

    def state(self, *args, **kwargs):
        for widget in self.combo, self.lbox, self.button_apply:
            widget.state(*args, **kwargs)


if __name__ == '__main__':
    root = tk.Tk()
    widget = SkipWidget(root, controller=None)
    widget.pack()
    root.mainloop()