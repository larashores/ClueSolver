from python_gui.signal import Signal
from python_gui.pyclue import Game

class Controller:
    def __init__(self):
        self.signal_players_changed = Signal()
        self.signal_player_name_changed = Signal()
        self.signal_update_analytics = Signal()
        self._game = Game()

    def add_player(self, *args, **kwargs):
        self._game.add_player(*args, **kwargs)

    def add_override(self, *args, **kwargs):
        self._game.add_override(*args, **kwargs)

    def stats(self, *args, **kwargs):
        return self._game.analyzer.stats(*args, **kwargs)

    def deck(self):
        return self._game.deck

    def players(self):
        return self._game.get_players()

    def num_players(self):
        return len(self._game.get_players())
