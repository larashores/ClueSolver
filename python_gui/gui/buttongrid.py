from tkinter import ttk
import tkinter as tk

from python_gui.gui.tristatusbutton import TriStatusButton


class ButtonGrid(ttk.Frame):
    def __init__(self, parent=None, columns=0, row_names=list(), column_names=list(), **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self._button_columns = []
        self._widgets = []
        self._row_names = row_names
        self.regrid(columns, column_names)

    def regrid(self, columns, column_names=list()):
        for widget in self._widgets:
            widget.destroy()
        self._button_columns = [[] for _ in range(columns)]
        for j, name in enumerate(column_names):
            label = ttk.Label(self, text=name, style='Subtitle.TLabel')
            label.grid(row=1, column=j+2)
            self._widgets.append(label)
        for i, name in enumerate(self._row_names):
            label = ttk.Label(self, text=name, width=15, anchor=tk.E)
            label.grid(row=i+2, column=1)
        for j in range(columns):
            for i in range(len(self._row_names)):
                button = TriStatusButton(self)
                button.grid(row=i+2, column=j+2)
                self._button_columns[j].append(button)
                self._widgets.append(button)

    def state(self, *args, **kwargs):
        for col in self._button_columns:
            for button in col:
                button.state(*args, **kwargs)

    def get_statuses_from_column(self, col):
        return [button.get_status() for button in self._button_columns[col]]

    def set_button_command(self, func):
        for col in self._button_columns:
            for button in col:
                button.config(command=lambda b=button: func(b))


if __name__ == '__main__':
    root = tk.Tk()
    grid = ButtonGrid(root, columns=4, row_names=[str(i+1) for i in range(10)])
    grid.pack()
    button = ttk.Button(root, text='regrid', command=lambda: grid.regrid((len(grid._button_columns) % 6) + 1))
    button.pack()
    root.mainloop()
