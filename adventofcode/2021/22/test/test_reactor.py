#!/usr/bin/env python3

from reactor import Reactor
import unittest

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
        self.assertEqual(0, r.on_count())

    def test_on_count(self):
        self.assertEqual(7, self.r.on_count())
