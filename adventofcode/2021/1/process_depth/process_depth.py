#!/usr/bin/env python3

import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(
            description='Process a set of depth measurements.')
    parser.add_argument(
            'depth_report_file',
            type=argparse.FileType('r'),
            default=sys.stdin,
            help="The input file containing the depth measurements.")
    parser.add_argument(
            '-w', '--window_size',
            type=int,
            default=1,
            help="Using a sliding window of the given size "
                "to count depth increases. Default: 1")

    return parser.parse_args()

def count_increases(numbers, window_size=1):
    """
    Count how many times a sliding window of @a window_size increases in @a
    numbers.

    Arguments:
        window_size (int): The size of the sliding window.
        numbers (iterable of numbers): The list of numbers.

    Returns (int): The number of times a sliding window of three integers
    increases in @a numbers.

    >>> count_increases([1, 10, 2, 2, 3, 1])
    2
    """
    window = []

    numbers_seen = 0
    increase_count = 0
    for number in numbers:
        if len(window) > window_size:
            raise RuntimeError("Logic error: window exceeded the expected size.")

        if len(window) == window_size:
            # Since values after the first in the previous window and before
            # the last in the current window are the same, they need not be
            # accounted for. Only the first entry in the previous window needs
            # to be compared with the last in the current.
            if number > window[0]:
                increase_count += 1
            window = window[1:]
        window.append(number)
        
    return increase_count


def IntFileIterator(file):
    """
    An iterator for processing a file with a number on each line.
    """
    for line in file:
        yield int(line)

def main():
    args = parse_args()
    depth_iterator = IntFileIterator(args.depth_report_file)
    depth_increase_count = count_increases(depth_iterator, args.window_size)
    print(depth_increase_count)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
