from tkinter import ttk
import tkinter as tk

from python_gui.gui.cluegui import ClueGui
from python_gui.gui.styles import configure_styles
from python_gui.gui.cluemenu import ClueMenu


def main():
    root = tk.Tk()
    menu = ClueMenu()
    root.config(menu=menu)
    configure_styles()
    gui = ClueGui(root)
    gui.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()


if __name__ == '__main__':
    main()
