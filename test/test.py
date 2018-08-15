import os
import sys
import unittest

sys.path.append(os.getcwd())
import pyclue as pc


class TestReferences(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.game = pc.Game()

    def test_references(self):
        change_str = 'Changed'
        self.game.add_player('Player', 4)
        player1 = self.game.get_players()[0]
        player1.name = change_str
        player2 = self.game.get_players()[0]
        self.assertEqual(player1.name, player2.name)
        self.assertEqual(player1.name, change_str)
        self.assertEqual(player2.name, change_str)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReferences)
    unittest.TextTestRunner(verbosity=2).run(suite)
