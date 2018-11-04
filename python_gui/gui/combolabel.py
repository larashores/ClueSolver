from tkinter import ttk
import tkinter as tk


class ComboLabel(ttk.Frame):
    def __init__(self, parent=None, *, text=None, values=None, **kwargs):
        ttk.Frame.__init__(self, parent)
        self._values = values
        self._var = tk.StringVar(self)
        self._combo = ttk.Combobox(self, values=values, justify=tk.CENTER, width=17,
                                   textvariable=self._var, **kwargs)
        self._label = ttk.Label(self, text=text, anchor=tk.CENTER)

        self._label.pack(fill=tk.X)
        self._combo.pack(expand=tk.YES, fill=tk.X)

    def values(self):
        return self._values

    def set_values(self, values):
        self._values = values
        self._combo.config(values=values)

    def state(self, statespec=None):
        self._label.state(statespec)
        self._combo.state(statespec)
        return ttk.Frame.state(self, statespec)

    def get(self):
        index = self.index()
        if index != -1:
            return self._values[index]
        else:
            return self._var.get()

    def set(self, text):
        self._var.set(text)

    def index(self):
        return self._combo.current()
