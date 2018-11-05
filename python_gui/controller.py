from python_gui.signal import Signal
from python_gui.pyclue import Game

from python_gui.constants import total_cards

class Controller:
    def __init__(self):
        self.signal_players_changed = Signal()
        self.signal_player_name_changed = Signal()
        self.signal_update_analytics = Signal()
        self._game = Game()

        self._players = []

    def set_order(self, players):
        if len(players) != len(self._game.get_players()):
            raise ValueError('Must include all players')
        self._players = players

    def add_player(self, *args, **kwargs):
        self._game.add_player(*args, **kwargs)
        self._players.append(self._game.get_players()[-1])
        return self._players[-1]

    def add_override(self, *args, **kwargs):
        self._game.add_override(*args, **kwargs)

    def clear_overrides(self):
        self._game.clear_overrides()

    def overrides(self):
        return self._game.overrides()

    def stats(self, *args, **kwargs):
        return self._game.analyzer.stats(*args, **kwargs)

    def deck(self):
        return self._game.deck

    def players(self):
        return self._players

    def num_players(self):
        return len(self._players)

    def available_cards(self):
        return self._game.remaining_cards()

    def add_guess(self, *args, **kwargs):
        self._game.add_guess(*args, **kwargs)

    def guesses(self):
        return self._game.get_guesses()