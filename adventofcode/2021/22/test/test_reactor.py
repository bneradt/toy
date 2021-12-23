#!/usr/bin/env python3

from reactor import Cube, Reactor
import unittest

class TestCube(unittest.TestCase):

    def test_constructor(self):
        c = Cube()
        self.assertFalse(c.is_on())
        self.assertTrue(c.is_off())

    def test_turn_on_and_off(self):
        c = Cube()
        self.assertFalse(c.turn_off())
        self.assertTrue(c.is_off())

        self.assertTrue(c.turn_on())
        self.assertFalse(c.is_off())
        self.assertTrue(c.is_on())

        self.assertFalse(c.turn_on())
        self.assertFalse(c.is_off())
        self.assertTrue(c.is_on())

        self.assertTrue(c.turn_off())
        self.assertTrue(c.is_off())
        self.assertFalse(c.is_on())

        self.assertFalse(c.turn_off())
        self.assertTrue(c.is_off())
        self.assertFalse(c.is_on())

class TestReactor(unittest.TestCase):

    def setUp(self):
        self.r = Reactor(5)
        self.assertEqual(7, self.r.process_steps([
            'on x=-2..1,y=1..2,z=1..1', # Turns on 8.
            'off x=-2..-2,y=0..1,z=1..2', # Turns off 1 that were on.
            ]))

    def test_constructor(self):
        with self.assertRaises(ValueError):
            r = Reactor(100)
        r = Reactor(11)
        self.assertEqual(11*11*11, r.off_count())
        self.assertEqual(0, r.on_count())

    def test_on_count(self):
        self.assertEqual(7, self.r.on_count())

    def test_off_count(self):
        self.assertEqual(5*5*5 - 7, self.r.off_count())
