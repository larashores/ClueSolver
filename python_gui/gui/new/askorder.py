from tkinter import ttk
import tkinter as tk

from python_gui.gui.orderer import Orderer


def ask_order(parent, names=list()):
    top = tk.Toplevel(parent)
    orderer = Orderer(top, names=names)
    orderer.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    orderer.gui.confirm.config(command=top.quit)
    top.mainloop()
    return [name for name in orderer]
