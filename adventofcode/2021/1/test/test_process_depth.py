#!/usr/bin/env python3

from process_depth import count_increases, IntFileIterator
from tempfile import NamedTemporaryFile
import unittest

class TestCountIncreasesWindowSize1(unittest.TestCase):
    """
    Test count_increases with a window size of 1 (the default).
    """
    def test_all_increases(self):
        l = [-20, 1, 2, 10, 100, 103]
        self.assertEqual(len(l) - 1, count_increases(l))

    def test_all_decreases(self):
        l = [120, 8, 5, 0, -1]
        self.assertEqual(0, count_increases(l))

    def test_mix(self):
        l = [-30, -40, -20, -5, 0, 3, 2, -1, 5, 8, 7, 8, 8, 6]
        self.assertEqual(7, count_increases(l))

class TestCountWindowIncreases(unittest.TestCase):
    """
    Test count_increases with a window size greater than 1.
    """
    def test_with_sample_input(self):
        l = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(5, count_increases(l, 3))

class TestIntFileIterator(unittest.TestCase):
    """
    Test the IntFileIterator.
    """
    def setUp(self):
        self.test_file = NamedTemporaryFile(mode='w+t')


    def test_iterator_functionality(self):
        input_list = [14, 24, 103, 2, -1, -1, 22, 22]
        for input_int in input_list:
            self.test_file.write(f'{input_int}\n')

        file_ints = IntFileIterator(self.test_file)
        for i, file_int in enumerate(file_ints):
            self.assertEqual(input_list[i], file_int)


if __name__ == '__main__':
    unittest.main()
