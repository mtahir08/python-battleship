import unittest
import sys
sys.path.append('../')
from battleship.board import Board


class TestBattleship(unittest.TestCase):

    def test_plot_ship_vertically(self):
      board = Board(10, 10)
      board.plot_ship_on_board(1, 2, "ship-1", 4, 'V')
      can_plot_ship = board.can_plot_ship_vertically(5, 7, 5)
      self.assertTrue(can_plot_ship)

    def test_plot_ship_horizontally(self):
      board = Board(10, 10)
      board.plot_ship_on_board(2, 1, "ship-1", 4, 'H')
      can_plot_ship = board.can_plot_ship_horizontally(5, 7, 7)
      self.assertTrue(can_plot_ship)

    def test_fail_plot_ship_vertically(self):
      board = Board(10, 10)
      board.plot_ship_on_board(1, 4, "ship-2", 6, 'V')
      can_plot_ship = board.can_plot_ship_vertically(1, 4, 6)
      self.assertFalse(can_plot_ship)

    def test_fail_plot_ship_horizontally(self):
      board = Board(10, 10)
      board.plot_ship_on_board(1, 4, "ship-2", 4, 'H')
      can_plot_ship = board.can_plot_ship_horizontally(1, 4, 4)
      self.assertFalse(can_plot_ship)

    # def test_shot_hit(self):
    #   board = Board(10, 10)
    #   board.plot_ship_on_board(2, 1, "ship-1", 2, 'H')
    #   shot = board.place_shot(2, 1)
    #   self.assertEqual(shot, "HIT")

    # def test_shot_sink(self):
    #   board = Board(10, 10)
    #   board.plot_ship_on_board(3, 1, "ship-1", 1, 'V')
    #   shot = board.place_shot(3, 1)
    #   self.assertEqual(shot, "SINK")

    # def test_shot_water(self):
    #   board = Board(10, 10)
    #   board.plot_ship_on_board(2, 1, "ship-1", 2, 'H')
    #   shot = board.place_shot(6, 4)
    #   self.assertEqual(shot, "WATER")

if __name__ == "__main__":
    unittest.main()