#!/usr/bin/env python3

"""Simulates lanternfish behavior for Advent of Code 2021 day 6."""

import argparse
import sys
from typing import List


class LanternFishSchool:
    """Represents a school of LanternFish.

    Has the responsibility of simulating each lantern fish as the simulated
    days progress.

    """

    _school: List[int]

    def __init__(self, initial_school: List[int]):
        """Initialize the school.

        Arguments
        ---------
        initial_school : list[int]
            The set of initial timer values for the school of fish.

        """
        self._school = [0 for _ in range(9)]
        for initial_value in initial_school:
            self._school[initial_value] += 1

    def get_school_size(self) -> int:
        """Retrieve the number of fish in the school.

        Returns
        -------
        int
            The number of fish in the school.

        >>> s = LanternFishSchool([1, 3, 4])
        >>> s.get_school_size()
        3

        """
        return sum(self._school)

    def advance_one_day(self) -> int:
        """Advance each fish in the school by one day.

        Returns
        -------
        int
             The number of fish in the school after the day finishes.  This
             includes any new fish that were spawned this day.

        >>> s = LanternFishSchool([1, 3, 0])
        >>> s.get_school_size()
        3
        >>> s.advance_one_day()
        4

        """
        num_to_spawn = self._school.pop(0)
        self._school.append(num_to_spawn)
        self._school[6] += num_to_spawn
        return self.get_school_size()


def csv_to_ints(school_description: str) -> List[int]:
    """Convert a comma separated string of integers to a list of integers.

    Returns
    -------
    list[int]
        The list of integers from the string of comma separated values.

    >>> csv_to_ints('3,8,0')
    [3, 8, 0]

    """
    return [int(integer) for integer in school_description.strip().split(',')]


def parse_args():
    """Parse the user's command line argumens."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-n', '--num_days',
        type=int,
        default=80,
        help='The number of days to run the simulation.')
    parser.add_argument(
        'input_file',
        type=argparse.FileType('rt'),
        default=sys.stdin,
        help='The file containing the set of initial timers of the school of '
             'lanternfish.')
    return parser.parse_args()


def main():
    """Implement the main entry point into the program."""
    args = parse_args()

    csv = args.input_file.readline()
    initial_timer_values = csv_to_ints(csv)
    school = LanternFishSchool(initial_timer_values)

    for _ in range(args.num_days):
        school.advance_one_day()
    print(school.get_school_size())

    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
