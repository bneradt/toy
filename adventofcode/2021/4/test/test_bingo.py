#!/usr/bin/env python3

import unittest
from bingo import Place, Board

class TestPlace(unittest.TestCase):

    def test_initialiation(self):
        p = Place(3)
        self.assertFalse(p.is_marked())
        self.assertEqual(3, p.get_number())

    def test_bool_override(self):
        p = Place(2)
        self.assertFalse(p)
        p.mark_if_matches(2)
        self.assertTrue(p)

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.small_board = Board(
                [[1, 2],
                 [3, 4]])

        rows: list[int] = []
        rows.append([14, 21, 17, 24,  4])
        rows.append([10, 16, 15,  9, 19])
        rows.append([18,  8, 23, 26, 20])
        rows.append([22, 11, 13,  6,  5])
        rows.append([ 2,  0, 12,  3,  7])
        self.large_board = Board(rows)

    def test_initialization(self):
        self.assertFalse(self.small_board.is_winning())
        self.assertEqual(0, self.small_board.get_board_score())
        self.assertFalse(self.large_board.is_winning())
        self.assertEqual(0, self.large_board.get_board_score())

    def test_row_is_winning(self):
        self.assertFalse(self.small_board.mark_number(1))
        self.assertFalse(self.small_board.is_winning())
        self.assertEqual(0, self.small_board.get_board_score())

        self.assertTrue(self.small_board.mark_number(2))
        self.assertTrue(self.small_board.is_winning())
        self.assertEqual(14, self.small_board.get_board_score())

    def test_column_is_winning(self):
        self.assertFalse(self.small_board.mark_number(2))
        self.assertFalse(self.small_board.is_winning())
        self.assertEqual(0, self.small_board.get_board_score())

        self.assertTrue(self.small_board.mark_number(4))
        self.assertTrue(self.small_board.is_winning())
        self.assertEqual(16, self.small_board.get_board_score())

    def test_larger_board_row_wins(self):
        for number in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21]:
            self.assertFalse(self.large_board.mark_number(number))
            self.assertFalse(self.large_board.is_winning())
            self.assertEqual(0, self.large_board.get_board_score())
        self.assertTrue(self.large_board.mark_number(24))
        self.assertTrue(self.large_board.is_winning())
        self.assertEqual(4512, self.large_board.get_board_score())

    def test_larger_board_column_wins(self):
        for number in [15, 4, 13, 5, 11, 17, 23, 2, 0, 14, 21]:
            self.assertFalse(self.large_board.mark_number(number))
            self.assertFalse(self.large_board.is_winning())
        self.assertTrue(self.large_board.mark_number(12))
        self.assertTrue(self.large_board.is_winning())
