import os
import sys
import unittest
import gc

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


class TestEquality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.game = pc.Game()

    def test_player_equality(self):
        self.game.add_player('Player', 4)
        player1 = self.game.get_players()[0]
        player2 = self.game.get_players()[0]
        self.assertEqual(player1, player2)

    def test_card_equality(self):
        first1 = self.game.deck.people()[0]
        first2 = self.game.deck.people()[0]

        self.game.add_player('Player', 4)
        player = self.game.get_players()[0]
        self.game.add_override(player, first1, True)
        as_card = next(iter(self.game.analyzer.stats().values())).positives()[0]
        self.assertEqual(first1, first2)
        self.assertEqual(first1, as_card)


class TestHash(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.game = pc.Game()

    def test_player_hash(self):
        self.game.add_player('Player', 4)
        player1 = self.game.get_players()[0]
        player2 = self.game.get_players()[0]
        dict_ = {player1: 0}
        self.assertTrue(player1 in dict_)
        self.assertTrue(player2 in dict_)

    def test_card_hash(self):
        first1 = self.game.deck.people()[0]
        first2 = self.game.deck.people()[0]
        self.game.add_player('Player', 4)
        self.game.add_override(self.game.get_players()[0], first1, True)
        first3 = next(iter(self.game.positive_overrides().values()))[0]
        dict_ = {first1: 0}
        self.assertTrue(first1 in dict_)
        self.assertTrue(first2 in dict_)
        self.assertTrue(first3 in dict_)


if __name__ == '__main__':
    reference_suite = unittest.TestLoader().loadTestsFromTestCase(TestReferences)
    equality_suite = unittest.TestLoader().loadTestsFromTestCase(TestEquality)
    hash_suite = unittest.TestLoader().loadTestsFromTestCase(TestHash)
    unittest.TextTestRunner(verbosity=2).run(reference_suite)
    unittest.TextTestRunner(verbosity=2).run(equality_suite)
    unittest.TextTestRunner(verbosity=2).run(hash_suite)
