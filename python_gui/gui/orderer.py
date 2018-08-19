from tkinter import ttk
import tkinter as tk

from PIL import Image, ImageTk

from python_gui.gui.listchoice import ListChoice
from python_gui.gui.resources import up_png, down_png


class OrdererGui(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.label = ttk.Label(self, text='Select Order', style='Title.TLabel')
        self.list_choice = ListChoice(self, width=30)
        self.confirm = ttk.Button(self, text='Confirm')
        self.up_img = ImageTk.PhotoImage(Image.open(up_png))
        self.down_img = ImageTk.PhotoImage(Image.open(down_png))
        self.up = ttk.Button(self, image=self.up_img)
        self.down = ttk.Button(self, image=self.down_img)

        self.label.grid(column=1, row=1, columnspan=2)
        self.list_choice.grid(column=1, row=2, rowspan=2, sticky=(tk.N + tk.E + tk.S + tk.W))
        self.confirm.grid(column=1, row=4, columnspan=2, pady=(5, 0))

        self.up.grid(column=2, row=2, padx=(5, 0))
        self.down.grid(column=2, row=3, padx=(5, 0))

        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.rowconfigure(self, 3, weight=1)


class Orderer:
    def __init__(self, parent=None, names=list()):
        self.gui = OrdererGui()
        self.gui.list_choice.bind('<Control-Up>', self._move_up)
        self.gui.list_choice.bind('<Control-Down>', self._move_down)
        self.gui.up.config(command=self._move_up)
        self.gui.down.config(command=self._move_down)

        for name in names:
            self.gui.list_choice.append(name)

    def pack(self, *args, **kwargs):
        self.gui.pack(*args, **kwargs)

    def _move_up(self, event=None):
        ind = self.gui.list_choice.get_selection()
        if ind is None or ind == 0:
            return
        item = self.gui.list_choice[ind]
        self.gui.list_choice.pop(ind)
        self.gui.list_choice.insert(ind - 1, item)
        self.gui.list_choice.set_selection(ind - 1)

    def _move_down(self, event=None):
        ind = self.gui.list_choice.get_selection()
        if ind is None or ind == len(self.gui.list_choice) - 1:
            return
        item = self.gui.list_choice[ind]
        self.gui.list_choice.pop(ind)
        self.gui.list_choice.insert(ind + 1, item)
        self.gui.list_choice.set_selection(ind + 1)


if __name__ == '__main__':
    from python_gui.gui.styles import configure_styles

    root = tk.Tk()
    configure_styles()
    orderer = Orderer(root, names=['Vince', 'Kristina', 'Cassandra', 'Vanessa', 'Mom'])
    orderer.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    root.mainloop()
