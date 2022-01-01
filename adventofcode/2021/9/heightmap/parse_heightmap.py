#!/usr/bin/env python3

"""Implements heightmap parsing functionality."""

import argparse
import sys
from typing import List


class HeightMap:
    """Represents a heightmap file."""

    _heightmap: List[List[int]]

    def __init__(self):
        """Construct a HeightMap object."""
        self._heightmap = []

    def add_line(self, heightmap_line: str) -> None:
        """Add a line to the heightmap.

        :param heightmap_line: A string of digits representing a line in the
        heightmap.

        """
        self._heightmap.append([int(i) for i in heightmap_line.strip()])

    def get_low_points(self) -> List[int]:
        """Retrieve the low points in the heightmap.

        Note that the puzzle defines a low point as "the locations that are
        lower than any of its adjacent locations." That is, the low points are
        those that are lower than, not lower than or equal to, their adjacent
        points.

        :return: The list of low point values in the heightmap.

        :example:
            >>> h = HeightMap()
            >>> h.add_line('3212')
            >>> h.add_line('3222')
            >>> h.add_line('3202')
            >>> h.get_low_points()
            [1, 0]

        """
        low_points: List[int] = []
        num_rows = len(self._heightmap)
        num_columns = len(self._heightmap[0])
        for row, row_values in enumerate(self._heightmap):
            for column, value in enumerate(row_values):
                if row > 0:
                    if value >= self._heightmap[row-1][column]:
                        continue
                if row < num_rows - 1:
                    if value >= self._heightmap[row+1][column]:
                        continue
                if column > 0:
                    if value >= self._heightmap[row][column-1]:
                        continue
                if column < num_columns - 1:
                    if value >= self._heightmap[row][column+1]:
                        continue
                low_points.append(value)
        return low_points

    def get_risk_level(self) -> int:
        """Find the risk level of the heightmap.

        This function calculates the low point heights of the heightmap append
        then assesses the risk level of the map from that. The risk level of
        each low point is the value of the height plus one.

        :return: The risk level of the heightmap.

        :example:
            >>> h = HeightMap()
            >>> h.add_line('3212')
            >>> h.add_line('3222')
            >>> h.add_line('3202')
            >>> h.get_risk_level()
            3

        """
        return sum([low_point + 1 for low_point in self.get_low_points()])


def parse_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=argparse.FileType('rt'),
        default=sys.stdin,
        help='The file containing the desciption of the heightmap.')
    return parser.parse_args()


def main():
    """Implement the main entry point into the script."""
    args = parse_args()
    heightmap = HeightMap()
    for line in args.input_file:
        heightmap.add_line(line)
    print(heightmap.get_risk_level())
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
