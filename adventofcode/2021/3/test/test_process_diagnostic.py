#!/usr/bin/env python3

from process_diagnostic import BinaryStat, ReportProcessor
import unittest

class TestBinaryStat(unittest.TestCase):
    def test_one(self):
        b = BinaryStat()
        b.process_binary(1)
        self.assertEqual(1, b.get_preponderance())

    def test_one_str(self):
        b = BinaryStat()
        b.process_binary('1')
        self.assertEqual(1, b.get_preponderance())

    def test_zero(self):
        b = BinaryStat()
        b.process_binary(0)
        self.assertEqual(0, b.get_preponderance())

    def test_zero_str(self):
        b = BinaryStat()
        b.process_binary('0')
        self.assertEqual(0, b.get_preponderance())

    def test_multiple_numbers_to_zero(self):
        b = BinaryStat()
        b.process_binary(0)
        b.process_binary('0')
        b.process_binary(1)
        self.assertEqual(0, b.get_preponderance())

    def test_multiple_numbers_to_one(self):
        b = BinaryStat()
        b.process_binary(1)
        b.process_binary('1')
        b.process_binary('0')
        self.assertEqual(1, b.get_preponderance())

class TestReportProcessor(unittest.TestCase):
    def setUp(self):
        self.report_processor = ReportProcessor()
        self.report_processor.process_number('00100')
        self.report_processor.process_number('11110')
        self.report_processor.process_number('10110')
        self.report_processor.process_number('10111')
        self.report_processor.process_number('10101')
        self.report_processor.process_number('01111')
        self.report_processor.process_number('00111')
        self.report_processor.process_number('11100')
        self.report_processor.process_number('10000')
        self.report_processor.process_number('11001')
        self.report_processor.process_number('00010')
        self.report_processor.process_number('01010')

    def test_0_get_num_entries(self):
        r = ReportProcessor()
        self.assertEqual(0, r.get_num_entries())

    def test_get_num_entries(self):
        self.assertEqual(12, self.report_processor.get_num_entries())

    def test_get_gamma(self):
        self.assertEqual(22, self.report_processor.get_gamma())

    def test_get_epsilon(self):
        self.assertEqual(9, self.report_processor.get_epsilon())

    def test_get_power_consumption(self):
        self.assertEqual(198, self.report_processor.get_power_consumption())

    def test_get_oxygen_rating(self):
        self.assertEqual(23, self.report_processor.get_oxygen_rating())

    def test_get_co2_rating(self):
        self.assertEqual(10, self.report_processor.get_co2_rating())

    def test_get_life_support_rating(self):
        self.assertEqual(230, self.report_processor.get_life_support_rating())
