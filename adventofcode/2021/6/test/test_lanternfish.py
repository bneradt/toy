import unittest
from lanternfish import LanternFishSchool


class TestLanternFishSchool(unittest.TestCase):

    def setUp(self):
        self.example_school = LanternFishSchool([3, 4, 3, 1, 2])

    def test_advance_one_day(self):
        school = LanternFishSchool([1, 0, 2])
        self.assertEqual(4, school.advance_one_day())
        self.assertEqual(4, school.get_school_size())
        self.assertEqual(5, school.advance_one_day())
        self.assertEqual(5, school.get_school_size())

    def test_example_input_18_days(self):
        for day in range(18):
            self.example_school.advance_one_day()
        self.assertEqual(26, self.example_school.get_school_size())

    def test_example_input_80_days(self):
        for day in range(80):
            self.example_school.advance_one_day()
        self.assertEqual(5934, self.example_school.get_school_size())

    def test_example_input_256_days(self):
        for day in range(256):
            self.example_school.advance_one_day()
        self.assertEqual(26984457539, self.example_school.get_school_size())
