#!/usr/bin/env python3

import unittest
from heightmap import HeightMap


class TestHeightMap(unittest.TestCase):

    def setUp(self):
        self.heightmap = HeightMap()
        self.heightmap.add_line('2199943210')
        self.heightmap.add_line('3987894921')
        self.heightmap.add_line('9856789892')
        self.heightmap.add_line('8767896789')
        self.heightmap.add_line('9899965678')

    def test_get_low_points(self):
        low_points = self.heightmap.get_low_points()
        self.assertEqual([1, 0, 5, 5], low_points)

    def test_get_risk_level(self):
        self.assertEqual(15, self.heightmap.get_risk_level())
