#!/usr/bin/env python3

import unittest
from syntax_checker import LineChecker


class TestLineChecker(unittest.TestCase):

    def test_get_corruption_score(self):
        lc = LineChecker('{([(<{}[<>[]}>{[]{[(<()>')
        self.assertEqual(1197, lc.get_corruption_score())

        lc = LineChecker('[[<[([]))<([[{}[[()]]]')
        self.assertEqual(3, lc.get_corruption_score())

        lc = LineChecker('[{[{({}]{}}([{[{{{}}([]')
        self.assertEqual(57, lc.get_corruption_score())

        lc = LineChecker('[<(<(<(<{}))><([]([]()')
        self.assertEqual(3, lc.get_corruption_score())

        lc = LineChecker('<{([([[(<>()){}]>(<<{{')
        self.assertEqual(25137, lc.get_corruption_score())

    def test_get_autocomplete_score(self):
        lc = LineChecker('[({(<(())[]>[[{[]{<()<>>')
        self.assertEqual(288957, lc.get_autocomplete_score())

        lc = LineChecker('[(()[<>])]({[<{<<[]>>(')
        self.assertEqual(5566, lc.get_autocomplete_score())

        lc = LineChecker('(((({<>}<{<{<>}{[]{[]{}')
        self.assertEqual(1480781, lc.get_autocomplete_score())

        lc = LineChecker('{<[[]]>}<{[{[{[]{()[[[]')
        self.assertEqual(995444, lc.get_autocomplete_score())

        lc = LineChecker('<{([{{}}[<[[[<>{}]]]>[]]')
        self.assertEqual(294, lc.get_autocomplete_score())
