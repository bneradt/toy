#!/usr/bin/env python3

import unittest
from process_course import Submarine

class TestSubmarine(unittest.TestCase):
    
    def test_construction(self):
        s = Submarine()
        self.assertEqual(0, s.get_depth())
        self.assertEqual(0, s.get_horizontal_position())

    def test_wrong_forward(self):
        s = Submarine()
        s.follow_wrong_instruction('forward 13')
        self.assertEqual(13, s.get_horizontal_position())
        self.assertEqual(0, s.get_depth())

    def test_wrong_down(self):
        s = Submarine()
        s.follow_wrong_instruction('down 8')
        self.assertEqual(0, s.get_horizontal_position())
        self.assertEqual(8, s.get_depth())

    def test_wrong_up(self):
        s = Submarine()
        s.follow_wrong_instruction('down 10')
        self.assertEqual(0, s.get_horizontal_position())
        self.assertEqual(10, s.get_depth())

        s.follow_wrong_instruction('up 3')
        self.assertEqual(0, s.get_horizontal_position())
        self.assertEqual(7, s.get_depth())

    def test_follow_wrong_instructions(self):
        s = Submarine()
        instructions =  [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2']
        s.follow_wrong_instructions(instructions)

        self.assertEqual(15, s.get_horizontal_position())
        self.assertEqual(10, s.get_depth())

    def test_forward(self):
        s = Submarine()
        s.follow_instruction('forward 13')
        self.assertEqual(13, s.get_horizontal_position())
        self.assertEqual(0, s.get_depth())

    def test_down(self):
        s = Submarine()
        s.follow_instruction('down 8')
        self.assertEqual(0, s.get_horizontal_position())
        # Should just increase aim, not down.
        self.assertEqual(0, s.get_depth())

    def test_up(self):
        s = Submarine()
        s.follow_instruction('down 10')
        self.assertEqual(0, s.get_horizontal_position())
        self.assertEqual(0, s.get_depth())

        s.follow_instruction('up 3')
        self.assertEqual(0, s.get_horizontal_position())
        self.assertEqual(0, s.get_depth())

        s.follow_instruction('forward 2')
        self.assertEqual(2, s.get_horizontal_position())
        self.assertEqual(14, s.get_depth())

    def test_follow_instructions(self):
        s = Submarine()
        instructions =  [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2']
        s.follow_instructions(instructions)

        self.assertEqual(15, s.get_horizontal_position())
        self.assertEqual(60, s.get_depth())

    def test_position_product(self):
        s = Submarine()
        s.follow_wrong_instruction('down 5')
        s.follow_wrong_instruction('forward 6')
        self.assertEqual(30, s.get_position_product())

        # Make sure aim doesn't confuse things.
        s = Submarine()
        s.follow_instruction('down 5')
        s.follow_instruction('forward 6')
        self.assertEqual(180, s.get_position_product())
