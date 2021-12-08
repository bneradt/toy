#!/usr/bin/env python3

import unittest
from intersect import Point, Slope, Segment

class TestPoint(unittest.TestCase):

    def test_eq(self):
        p1 = Point(1, 2)
        p2 = Point(2, 1)
        p3 = Point(2, 1)
        self.assertEqual(p2, p3)
        self.assertNotEqual(p1, p2)

    def test_str(self):
        self.assertEqual('(4, 5)', str(Point(4, 5)))

    def test_get_x(self):
        self.assertEqual(0, Point(0, 2).get_x())
        self.assertEqual(5, Point(5, 3).get_x())

    def test_get_y(self):
        self.assertEqual(2, Point(0, 2).get_y())
        self.assertEqual(0, Point(5, 0).get_y())

    def test_set(self):
        p1 = Point(1, 2)
        p2 = Point(3, 0)
        p3 = Point(7, 9)
        p4 = Point(7, 9)

        s = set()
        self.assertEqual(0, len(s))
        s.add(p1)
        self.assertEqual(1, len(s))
        s.add(p2)
        self.assertEqual(2, len(s))
        s.add(p3)
        self.assertEqual(3, len(s))
        s.add(p4)
        self.assertEqual(3, len(s))

        s.add(p1)
        self.assertEqual(3, len(s))

        self.assertTrue(p1 in s)
        self.assertFalse(Point(100, 200) in s)

class TestSlope(unittest.TestCase):
    
    def test_get_rise(self):
        s = Slope(Point(1, 0), Point(8, 7))
        self.assertEqual(1, s.get_rise())

        s = Slope(Point(5, 7), Point(1, 3))
        self.assertEqual(-1, s.get_rise())

        s = Slope(Point(5, 7), Point(1, 7))
        self.assertEqual(0, s.get_rise())

        s = Slope(Point(1, 5), Point(3, 3))
        self.assertEqual(-1, s.get_rise())

    def test_get_run(self):
        s = Slope(Point(1, 0), Point(5, 4))
        self.assertEqual(1, s.get_run())

        s = Slope(Point(5, 7), Point(1, 3))
        self.assertEqual(-1, s.get_run())

        s = Slope(Point(5, 7), Point(5, 0))
        self.assertEqual(0, s.get_run())

        s = Slope(Point(1, 5), Point(3, 3))
        self.assertEqual(1, s.get_run())

    def test_non_equal_rise_over_run(self):
        with self.assertRaises(ValueError):
            s = Slope(Point(1, 5), Point(3, 20))

class TestSegment(unittest.TestCase):

    def test_is_horizontal_or_vertical(self):
        s = Segment(Point(6, 0), Point(6, 7))
        self.assertTrue(s.is_horizontal_or_vertical())

        s = Segment(Point(6, 7), Point(0, 7))
        self.assertTrue(s.is_horizontal_or_vertical())

        s = Segment(Point(6, 7), Point(3, 4))
        self.assertFalse(s.is_horizontal_or_vertical())

    def test_get_points_vertical(self):
        s = Segment(Point(6, 0), Point(6, 3))
        expected = [Point(6, 0), Point(6, 1), Point(6, 2), Point(6, 3)]
        self.assertEqual(expected, s.get_points())

    def test_get_points_horizontal(self):
        s = Segment(Point(6, 0), Point(3, 0))
        expected = [Point(6, 0), Point(5, 0), Point(4, 0), Point(3, 0)]
        self.assertEqual(expected, s.get_points())

    def test_get_points_diagonal(self):
        s = Segment(Point(1, 3), Point(3, 5))
        expected = [Point(1, 3), Point(2, 4), Point(3, 5)]
        self.assertEqual(expected, s.get_points())

        s = Segment(Point(1, 5), Point(3, 3))
        expected = [Point(1, 5), Point(2, 4), Point(3, 3)]
        self.assertEqual(expected, s.get_points())

    def test_get_intersection_diagnonal_cross(self):
        s1 = Segment(Point(1, 3), Point(3, 5))
        s2 = Segment(Point(1, 5), Point(3, 3))
        self.assertEqual([Point(2, 4)], s1.get_intersection(s2))

    def test_get_intersection_horizontal(self):
        s1 = Segment(Point(1, 3), Point(4, 3))
        s2 = Segment(Point(3, 3), Point(5, 3))
        self.assertEqual([Point(3, 3), Point(4, 3)], s1.get_intersection(s2))

    def test_get_intersection_vertical(self):
        s1 = Segment(Point(1, 3), Point(1, 5))
        s2 = Segment(Point(1, 3), Point(1, 6))
        self.assertEqual([Point(1, 3), Point(1, 4), Point(1, 5)], s1.get_intersection(s2))
