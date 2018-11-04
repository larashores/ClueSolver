from tkinter import ttk
import tkinter as tk

class NameWidget(ttk.Frame):
    def __init__(self, *args, controller, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller
        self.labels = []

        self.controller.signal_players_changed.connect(self.on_players_changed)
        self.controller.signal_player_name_changed.connect(self.on_players_changed)

    def on_players_changed(self):
        names = [player.name for player in self.controller.players()]

        for label in self.labels:
            label.destroy()
        self.labels.clear()

        for i, name in enumerate(names):
            label = ttk.Label(self, text='{}) {}   '.format(i+1, name), style='Subtitle.TLabel')
            label.pack(side=tk.LEFT)
            self.labels.append(label)
