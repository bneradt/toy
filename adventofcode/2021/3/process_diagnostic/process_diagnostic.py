#!/usr/bin/env python3

import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(
            description="Process the submarine's diagnostic report.")

    parser.add_argument(
            'report',
            type=argparse.FileType('rt'),
            default=sys.stdin,
            help="The submarine's diagnostic report.")

    parser.add_argument(
            '-l', '--get_life_support_rating',
            action='store_true',
            default=False,
            help="Get the life support rating from the report. "
                 "By default, the power consumption rating is calculated.")

    return parser.parse_args()

class BinaryStat:
    def __init__(self):
        self._zero_count = 0
        self._one_count = 0

    def process_binary(self, value):
        """
        Process the give value and update stats accordingly.
        """
        if str(value) == '0':
            self._zero_count += 1
        elif str(value) == '1':
            self._one_count += 1
        else:
            raise ValueError(f"Non-binary value: '{value}'")

    def get_preponderance(self):
        """
        Return the binary value seen the most.

        Raises:
            RuntimeError: If the two stats are equal.

        >>> b = BinaryStat()
        >>> b.process_binary(1)
        >>> b.get_preponderance()
        1

        >>> b.process_binary(0)
        >>> b.get_preponderance()
        Traceback (most recent call last):
        ...
        RuntimeError: Same number of ones and zeros: 1

        >>> b.process_binary(0)
        >>> b.get_preponderance()
        0
        """
        if self._zero_count > self._one_count:
            return 0
        elif self._zero_count < self._one_count:
            return 1
        else:
            raise RuntimeError(f"Same number of ones and zeros: {self._zero_count}")

    def get_minority(self):
        """
        Return the binary value seen the least.

        Raises:
            RuntimeError: If the two stats are equal.

        >>> b = BinaryStat()
        >>> b.process_binary(1)
        >>> b.get_minority()
        0

        >>> b.process_binary(0)
        >>> b.get_minority()
        Traceback (most recent call last):
        ...
        RuntimeError: Same number of ones and zeros: 1

        >>> b.process_binary(0)
        >>> b.get_minority()
        1
        """
        if self.get_preponderance() == 1:
            return 0
        else:
            return 1

class ReportProcessor:
    def __init__(self):
        self._binary_stats = []
        self._numbers = []

    def process_number(self, number):
        """
        Process the binary number and update stats accordingly.
        """
        while len(number) > len(self._binary_stats):
            self._binary_stats.insert(0, BinaryStat())

        for index, binary in enumerate(number):
            self._binary_stats[index].process_binary(binary)

        self._numbers.append(number)

    def get_num_entries(self):
        """
        Return the number of entries in the report.

        >>> r = ReportProcessor()
        >>> r.get_num_entries()
        0
        >>> r.process_number('00100')
        >>> r.get_num_entries()
        1
        >>> r.process_number('11110')
        >>> r.get_num_entries()
        2
        """
        return len(self._numbers)

    def _filter_co2_report(self, position):
        """
        Filter the report for CO2 data and return a new report with the
        subset of data.

        >>> r = ReportProcessor()
        >>> r.process_number('00100')
        >>> r.process_number('11110')
        >>> r.process_number('10110')
        >>> new_r = r._filter_co2_report(0)
        >>> new_r.get_num_entries()
        1
        """
        new_report = ReportProcessor()
        try:
            position_filter = self._binary_stats[position].get_minority()
        except RuntimeError:
            position_filter = 0
        for number in self._numbers:
            if number[position] == str(position_filter):
                new_report.process_number(number)
        return new_report

    def _filter_oxygen_report(self, position):
        """
        Filter the report for oxygen data and return a new report with the
        subset of data.

        >>> r = ReportProcessor()
        >>> r.process_number('00100')
        >>> r.process_number('11110')
        >>> r.process_number('10110')
        >>> new_r = r._filter_oxygen_report(0)
        >>> new_r.get_num_entries()
        2
        >>> new_r = new_r._filter_oxygen_report(1)
        >>> new_r.get_num_entries()
        1
        """
        new_report = ReportProcessor()
        try:
            position_filter = self._binary_stats[position].get_preponderance()
        except RuntimeError:
            position_filter = 1
        for number in self._numbers:
            if number[position] == str(position_filter):
                new_report.process_number(number)
        return new_report


    def get_epsilon(self):
        """
        Return the epsilon number from the report.

        The epsilon number is the binary number for which every place value is
        the one of least occurence across the binary numbers for that place in
        the report.

        >>> r = ReportProcessor()
        >>> r.process_number('00100')
        >>> r.process_number('11110')
        >>> r.process_number('10110')
        >>> r.get_epsilon() == 0b01001
        True
        """
        gamma = ''.join([str(b.get_minority()) for b in self._binary_stats])
        return int(gamma, 2)

    def get_gamma(self):
        """
        Return the gamma number from the report.

        The gamma number is the binary number for which every place value is
        the one of greatest preponderance across the binary numbers for that
        place in the report.

        >>> r = ReportProcessor()
        >>> r.process_number('00100')
        >>> r.process_number('11110')
        >>> r.process_number('10110')
        >>> r.get_gamma() == 0b10110
        True
        """
        gamma = ''.join([str(b.get_preponderance()) for b in self._binary_stats])
        return int(gamma, 2)
    
    def get_power_consumption(self):
        """
        Return the power consumption given the diagnostic report.

        The power consumption is the product of the gamma and epsilon values.

        >>> r = ReportProcessor()
        >>> r.process_number('00100')
        >>> r.process_number('11110')
        >>> r.process_number('10110')
        >>> r.get_gamma()
        22
        >>> r.get_epsilon()
        9
        >>> r.get_power_consumption()
        198
        """
        return self.get_gamma() * self.get_epsilon()

    def get_oxygen_rating(self):
        """
        Return the oxygen rating.

        To find oxygen generator rating, determine the most common value (0 or
        1) in the current bit position, and keep only numbers with that bit in
        that position. If 0 and 1 are equally common, keep values with a 1 in
        the position being considered.

        >>> r = ReportProcessor()
        >>> r.process_number('00100')
        >>> r.process_number('11110')
        >>> r.process_number('10110')
        >>> r.get_oxygen_rating() == 0b11110
        True
        """
        new_report = self
        for position in range(len(self._binary_stats)):
            new_report = new_report._filter_oxygen_report(position)
            if new_report.get_num_entries() == 1:
                break;
        return int(new_report._numbers[0], 2)

    def get_co2_rating(self):
        """
        Return the C02 rating.

        To find CO2 scrubber rating, determine the least common value (0 or 1)
        in the current bit position, and keep only numbers with that bit in
        that position. If 0 and 1 are equally common, keep values with a 0 in
        the position being considered.


        >>> r = ReportProcessor()
        >>> r.process_number('00100')
        >>> r.process_number('11110')
        >>> r.process_number('10110')
        >>> r.get_co2_rating() == 0b00100
        True
        """
        new_report = self
        for position in range(len(self._binary_stats)):
            new_report = new_report._filter_co2_report(position)
            if new_report.get_num_entries() == 1:
                break;
        return int(new_report._numbers[0], 2)
    
    def get_life_support_rating(self):
        """
        Return the life support rating, the product of the oxygen and CO2
        ratings.

        >>> r = ReportProcessor()
        >>> r.process_number('00100')
        >>> r.process_number('11110')
        >>> r.process_number('10110')
        >>> r.get_oxygen_rating()
        30
        >>> r.get_co2_rating()
        4
        >>> r.get_life_support_rating()
        120
        """
        return self.get_oxygen_rating() * self.get_co2_rating()


def main():
    args = parse_args()

    report_processor = ReportProcessor()
    for line in args.report:
        binary_number = line.strip()
        report_processor.process_number(binary_number)

    if args.get_life_support_rating:
        print(report_processor.get_life_support_rating())
    else:
        print(report_processor.get_power_consumption())

    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
