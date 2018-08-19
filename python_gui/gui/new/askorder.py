from tkinter import ttk
import tkinter as tk

from python_gui.gui.orderer import Orderer


def ask_order(parent, names=list()):
    def quit_and_destroy():
        orderer.gui.quit()
        orderer.gui.destroy()

    orderer = Orderer(parent, names=names)
    orderer.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    orderer.gui.confirm.config(command=quit_and_destroy)
    orderer.gui.mainloop()
    return [name for name in orderer]
