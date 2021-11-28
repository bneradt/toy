#!/usr/bin/env python3

import unittest
from which_floor import description_to_final_floor, get_first_basement_position


class TestExamples(unittest.TestCase):

    def test_description_to_final_floor(self):
        self.assertEqual(0, description_to_final_floor(''))
        self.assertEqual(0, description_to_final_floor('(())'))
        self.assertEqual(0, description_to_final_floor('()()'))

        self.assertEqual(3, description_to_final_floor('((('))
        self.assertEqual(3, description_to_final_floor('(()(()('))
        self.assertEqual(3, description_to_final_floor('))((((('))

        self.assertEqual(-1, description_to_final_floor('())'))
        self.assertEqual(-1, description_to_final_floor('))('))

        self.assertEqual(-3, description_to_final_floor(')))'))
        self.assertEqual(-3, description_to_final_floor(')())())'))

    def test_get_first_basement_position(self):
        self.assertEqual(1, get_first_basement_position(')'))
        self.assertEqual(1, get_first_basement_position(')))'))

        self.assertEqual(5, get_first_basement_position('()())'))


if __name__ == '__main__':
    unittest.main()
