#!/usr/bin/env python3
"""Decipher the broken displays.

Reads the set of broken display output and deciphers it. This solves the
Advent of Code 2021 day 8 puzzle which can be found here:

    https://adventofcode.com/2021/day/8

"""

import argparse
import sys
from typing import List, Set


class EntryReader:
    """Reads an entry to decipher the digits."""

    _digit_strings: List[str]
    _output_digit_strings: List[str]
    _output_digits: List[int]

    _one_set: Set
    _two_set: Set
    _three_set: Set
    _four_set: Set
    _five_set: Set
    _six_set: Set
    _seven_set: Set
    _eight_set: Set
    _nine_set: Set

    def __init__(self, entry: str):
        """Initialize an EntryReader.

        :param entry: The journal entry for a single display.

        """
        digit_string, output_string = [x.strip() for x in entry.split('|')]
        self._digit_strings = digit_string.split()
        self._output_digit_strings = output_string.split()
        self._output_digits = []

        self._zero_set = set()
        self._one_set = set()
        self._two_set = set()
        self._three_set = set()
        self._four_set = set()
        self._five_set = set()
        self._six_set = set()
        self._seven_set = set()
        self._eight_set = set()
        self._nine_set = set()

    def _parse(self) -> None:
        """Parse the journal entry to interpret the output digits.

        Here are the correct entries:
          0:      1:      2:      3:      4:
         aaaa    ....    aaaa    aaaa    ....
        b    c  .    c  .    c  .    c  b    c
        b    c  .    c  .    c  .    c  b    c
         ....    ....    dddd    dddd    dddd
        e    f  .    f  e    .  .    f  .    f
        e    f  .    f  e    .  .    f  .    f
         gggg    ....    gggg    gggg    ....

        5:      6:      7:      8:      9:
         aaaa    aaaa    aaaa    aaaa    aaaa
        b    .  b    .  .    c  b    c  b    c
        b    .  b    .  .    c  b    c  b    c
         dddd    dddd    ....    dddd    dddd
        .    f  e    f  .    f  e    f  .    f
        .    f  e    f  .    f  e    f  .    f
         gggg    gggg    ....    gggg    gggg

        Number of segments : Possible digits
        1                  : None
        2                  : 1
        3                  : 7
        4                  : 4
        5                  : 2, 3, 5
        6                  : 0, 6, 9
        7                  : 8

        The values of each can be determined as such:

        * 1, 4, 7, and 8 are determined simply from the digits because they
          each have a unique number of segments.
        * Of 2, 3, and 5:
            * A 3 has both the segments of 1 in it.
        * Of 0, 6, 9:
            * 6 does not have both of 1's segments in it.
            * 9 has all of 4's segments in it, 0 doesn't.
            * 0 is the remaining one.

        Segment analysis:
            * 'a' is the difference between 1 and 7.
            * 'b' is the unidentified segment in 4 after c, d, and f are
              identified.
            * 'c' is the segment of 1 not in 6.
            * 'd' is the difference between 8 and 0.
            * 'e' is the difference between 8 and 9.
            * 'f' is the segment of 1 in 6.
            * 'g' is the remaining segment.

        Given the deciphering of the segments, 2 and 5 can be differentiated
        since 2 has c and e, while 5 has b and f.

        """

        # First: find all the digit strings that are determined simply
        # by their length.
        two_three_and_five: List[str] = []
        zero_six_and_nine: List[str] = []
        for digit_string in self._digit_strings:
            if len(digit_string) == 2:
                self._one_set = set(digit_string)
            elif len(digit_string) == 3:
                self._seven_set = set(digit_string)
            elif len(digit_string) == 4:
                self._four_set = set(digit_string)
            elif len(digit_string) == 5:
                two_three_and_five.append(digit_string)
            elif len(digit_string) == 6:
                zero_six_and_nine.append(digit_string)
            elif len(digit_string) == 7:
                self._eight_set = set(digit_string)

        # Now, determine some of the digits of the same length from what
        # is known of the digits having a unique length.
        three_string = ''
        for digit_string in two_three_and_five:
            digit_string_set = set(digit_string)
            if self._one_set.issubset(digit_string_set):
                three_string = digit_string
                break
        if not three_string:
            raise RuntimeError("Failed to determine three string.")
        two_and_five = two_three_and_five
        two_and_five.remove(three_string)
        self._three_set = set(three_string)

        six_string = ''
        for digit_string in zero_six_and_nine:
            digit_string_set = set(digit_string)
            if not self._one_set.issubset(digit_string_set):
                six_string = digit_string
                break

        if not six_string:
            raise RuntimeError("Failed to determine six string.")

        zero_and_nine = zero_six_and_nine
        zero_and_nine.remove(six_string)
        self._six_set = set(six_string)

        nine_string = ''
        for digit_string in zero_and_nine:
            digit_string_set = set(digit_string)
            if self._four_set.issubset(digit_string_set):
                nine_string = digit_string
        if not nine_string:
            raise RuntimeError("Failed to determine nine string.")

        zero_list = zero_and_nine
        zero_list.remove(nine_string)
        self._nine_set = set(nine_string)
        self._zero_set = set(zero_list[0])

        # Now we know all the digits except for two and five. Now determine the
        # segments.

        # a_segment is not used.
        # a_segment = (self._seven_set - self._one_set).pop()

        f_segment = (self._one_set.intersection(set(six_string))).pop()
        c_segment = (self._one_set - set(f_segment)).pop()
        d_segment = (self._eight_set - self._zero_set).pop()

        # e_segment is not used.
        # e_segment = (self._eight_set - self._nine_set).pop()

        b_segment = (self._four_set -
                     set([c_segment, d_segment, f_segment])).pop()

        # g_segment is not used.
        # g_segment = (self._three_set -
        #              set([a_segment, c_segment, d_segment, f_segment])).pop()

        # Finally, distinguish between two and five.
        for digit_string in two_and_five:
            if c_segment in digit_string:
                self._two_set = set(digit_string)
            elif b_segment in digit_string:
                self._five_set = set(digit_string)

        for output_digit_string in self._output_digit_strings:
            if self._zero_set == set(output_digit_string):
                self._output_digits.append(0)
            if self._one_set == set(output_digit_string):
                self._output_digits.append(1)
            elif self._two_set == set(output_digit_string):
                self._output_digits.append(2)
            elif self._three_set == set(output_digit_string):
                self._output_digits.append(3)
            elif self._four_set == set(output_digit_string):
                self._output_digits.append(4)
            elif self._five_set == set(output_digit_string):
                self._output_digits.append(5)
            elif self._six_set == set(output_digit_string):
                self._output_digits.append(6)
            elif self._seven_set == set(output_digit_string):
                self._output_digits.append(7)
            elif self._eight_set == set(output_digit_string):
                self._output_digits.append(8)
            elif self._nine_set == set(output_digit_string):
                self._output_digits.append(9)

    def get_output_digits(self) -> List[int]:
        """Return the deciphered output digits.

        :return: The output digits.

        :example:

        # b corresponds the original f
        #        8       5     2     3     7   9      6      4    0      1
        >>> d = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
        >>> o = 'cdfeb fcadb cdfeb cdbaf'
        >>> r = EntryReader(f'{d} | {o}')
        >>> r.get_output_digits()
        [5, 3, 5, 3]
        """
        if not self._output_digits:
            self._parse()
        return self._output_digits


class DisplayProcessor:
    """Processes the entire set of display data.

    This class uses EntryReader to interpret each entry and provides an api
    allowing the user to engage in high level interaction with the entire set
    of data.

    """

    _entry_readers: List['EntryReader']

    def __init__(self, entries: List[str]):
        """Create a DisplayProcessor that will process entries.

        :param entries": The journal entries to parse.

        """
        self._entry_readers = []
        for entry in entries:
            self._entry_readers.append(EntryReader(entry))

    def get_display_values(self) -> List[List[int]]:
        """Return the list of display values.

        :return: The list of digits shown on the dials.

        """
        display_values = []
        for entry_reader in self._entry_readers:
            display_values.append(entry_reader.get_output_digits())
        return display_values


def get_one_four_seven_eight_count(display_values: List[List[int]]):
    """Count the number of occurrences of 1, 4, 7, and 8 in the displays.

    :param display_values: The set of display values.

    :return: The count of the number of times 1, 4, 7, and 8 occur in the
    dials.

    :example:

    >>> values = [[8, 4, 3, 9], [1, 1, 3, 8], [5, 2, 5, 5], [7, 2, 5, 8]]
    >>> get_one_four_seven_eight_count(values)
    7

    """
    count = 0
    for display_value in display_values:
        for digit in display_value:
            if digit in [1, 4, 7, 8]:
                count += 1
    return count


def get_sum_of_display_values(display_values: List[List[int]]):
    """Sum the list of display values.

    :param display_values: The set of display values.

    :return: The sum of each of the display values.

    :example:

    >>> values = [[8, 4, 3, 9], [0, 1, 3, 8], [5, 2, 5, 0], [7, 2, 5, 8]]
    >>> get_sum_of_display_values(values)
    21085

    """
    value_sum = 0
    for display_value in display_values:
        numeric_value = int(''.join([str(d) for d in display_value]))
        value_sum += numeric_value
    return value_sum


def parse_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=argparse.FileType('rt'),
        default=sys.stdin,
        help='The file containing the journal entries.')
    parser.add_argument(
        '-c', '--count_one_four_seven_eight_occurrences',
        action='store_true',
        help='Count the occurrences of 1, 4, 7, 8 in the displays.')
    return parser.parse_args()


def main():
    """Entry point into the program."""

    args = parse_args()

    display_processor = DisplayProcessor(args.input_file)
    display_values = display_processor.get_display_values()

    if args.count_one_four_seven_eight_occurrences:
        print(get_one_four_seven_eight_count(display_values))
    else:
        print(get_sum_of_display_values(display_values))

    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
