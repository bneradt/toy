import unittest
from process_report import find_two_entry_product, find_three_entry_product


class TestFindTwoEntryProduct(unittest.TestCase):

    def test_emptry_report(self):
        with self.assertRaises(ValueError):
            find_two_entry_product([])

    def test_single_entry(self):
        with self.assertRaises(ValueError):
            find_two_entry_product([2020])

    def test_none_sum_to_2020(self):
        with self.assertRaises(ValueError):
            find_two_entry_product([1, 2, 3])

    def test_two_entries(self):
        self.assertEqual(514579, find_two_entry_product([1721, 299]))
        self.assertEqual(514579, find_two_entry_product([299, 1721]))

    def test_three_entries(self):
        self.assertEqual(514579, find_two_entry_product([1721, 299, 20]))
        self.assertEqual(514579, find_two_entry_product([1721, 20, 299]))
        self.assertEqual(514579, find_two_entry_product([20, 1721, 299]))


class TestFindThreeEntryProduct(unittest.TestCase):

    def test_emptry_report(self):
        with self.assertRaises(ValueError):
            find_three_entry_product([])

    def test_single_entry(self):
        with self.assertRaises(ValueError):
            find_three_entry_product([2020])

    def test_two_entries(self):
        with self.assertRaises(ValueError):
            find_three_entry_product([2007, 13])

    def test_none_sum_to_2020(self):
        with self.assertRaises(ValueError):
            find_three_entry_product([1, 2, 3])

    def test_three_entries(self):
        self.assertEqual(241861950, find_three_entry_product([979, 366, 675]))
        self.assertEqual(241861950, find_three_entry_product([366, 979, 675]))

    def test_four_entries(self):
        self.assertEqual(
            241861950, find_three_entry_product([20, 979, 366, 675]))
        self.assertEqual(
            241861950, find_three_entry_product([979, 20, 366, 675]))
        self.assertEqual(
            241861950, find_three_entry_product([979, 366, 20, 675]))

    def test_five_entries(self):
        self.assertEqual(241861950, find_three_entry_product(
            [20, 979, 13, 366, 675]))
        self.assertEqual(241861950, find_three_entry_product(
            [20, 979, 366, 675, 13]))


if __name__ == '__main__':
    unittest.main()
