from tkinter import ttk
import tkinter as tk

from python_gui.gui.cluegui import ClueGui
from python_gui.gui.styles import configure_styles


def main():
    root = tk.Tk()
    configure_styles()
    gui = ClueGui(root)
    gui.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()


if __name__ == '__main__':
    main()
