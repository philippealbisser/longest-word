import unittest
import string
from game import Game

class TestGame(unittest.TestCase):

    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_is_valid(self):
            new_game = Game()
            new_game.grid = list('ABCDETECU')
            self.assertIs(new_game.is_valid('CUTE'), True)

    def test_is_not_valid(self):
        new_game = Game()
        new_game.grid = list('ABCDEFGHI')
        self.assertIs(new_game.is_valid('SQUARE'), False)

    def test_is_not_valid_duplicate_letters(self):
        new_game = Game()
        new_game.grid = list('ABCDEFGHI')
        self.assertIs(new_game.is_valid('CACA'), False)

    def test_unknown_word_is_invalid(self):
          new_game = Game()
          new_game.grid = list('KWIENFUQW')
          self.assertIs(new_game.is_valid('FEUN'), False)

    def test_dict_word_is_valid(self):
          new_game = Game()
          new_game.grid = list('KWIENFUQW')
          self.assertIs(new_game.is_valid('FUN'), True)
