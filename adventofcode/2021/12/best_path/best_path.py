#!/usr/bin/env python3
r"""Process the various paths in a cave system.

Paths are described in a file that looks like this:

start-A
start-b
A-c
A-b
b-d
A-end
b-end

Which corresponds to a cave system represented like this:

    start
    /   \
c--A-----b--d
    \   /
     end

"""


import argparse
import sys
from typing import Dict, List, Set


class Cave:
    """Represents a cave that has paths to other caves in it."""

    _name: str
    _is_small: bool
    _is_start: bool
    _is_end: bool
    _neighbors: Set['Cave']

    def __init__(self, name: str) -> None:
        """Initialize the cave.

        Caves that are upper case are large while lower case ones are small.

        :param name: The name of the cave.

        """
        self._is_start = False
        self._is_end = False
        self._is_small = False

        self._name = name
        if name == 'start':
            self._is_start = True
        elif name == 'end':
            self._is_end = True

        # Note that 'start' and 'end' are "small" in the sense that they can be
        # entered only once.
        self._is_small = name.islower()
        self._neighbors = set()

    def __str__(self):
        """How to print a cave in a string."""
        return self._name

    def __repr__(self):
        """How to represent a cave in a string."""
        return f'Cave("{self._name}")'

    def __eq__(self, other: 'Cave') -> bool:
        """Return whether this Cave is other."""
        return self._name == other._name

    def __ne__(self, other: 'Cave') -> bool:
        """Return whether this Cave is not other."""
        return not Cave.__eq__(self, other)

    def __hash__(self):
        """Hash the self_name for sets."""
        return sum([ord(character) for character in self._name])

    def add_connection(self, other: 'Cave') -> None:
        """Add a connection to a neighbor Cave.

        :param other: The cave to which there is a connection.

        """
        self._neighbors.add(other)
        other._neighbors.add(self)

    def find_all_paths_to_end(
            self,
            path_to_here: List['Cave']) -> List[List['Cave']]:
        """Find all paths to end from here.

        :param path_to_here: The path taken to get to this Cave.

        :return: The list of all paths from here to end.

        """
        if self._is_end:
            return [[self]]
        paths = []
        new_paths_to_here = path_to_here + [self]
        for neighbor in self._neighbors:
            if neighbor._is_small and neighbor in path_to_here:
                continue
            paths_to_end = neighbor.find_all_paths_to_end(new_paths_to_here)
            if paths_to_end:
                paths += paths_to_end
        if not paths:
            return []
        return [[self] + path for path in paths]


class Caves:
    """Represent a network of Caves."""

    _start: Cave
    _end: Cave
    _caves: Dict[str, Cave]

    def __init__(self) -> None:
        """Initialize a network of Caves."""
        self._start = Cave('start')
        self._end = Cave('end')
        self._caves = {
            'start': self._start,
            'end': self._end,
        }

    def add_connection(self, connection: str) -> None:
        """Add a connection between two caves.

        If either or both of the caves in the description does not exist, they
        will be created.

        :param connection: A description of a connection between two caves.

        :example:
            >>> caves = Caves()
            >>> caves.add_connection('start-b')
            >>> caves.add_connection('b-end')
            >>> caves.find_all_paths_to_end()
            [[Cave("start"), Cave("b"), Cave("end")]]
        """
        first, second = connection.strip().split('-')

        if first not in self._caves:
            self._caves[first] = Cave(first)
        first_cave = self._caves[first]

        if second not in self._caves:
            self._caves[second] = Cave(second)
        second_cave = self._caves[second]

        first_cave.add_connection(second_cave)

    def find_all_paths_to_end(self) -> List[List[Cave]]:
        """Find all paths to end from start.

        :return: The list of all paths from start to end.

        """
        return self._start.find_all_paths_to_end([self._start])


def parse_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'input_file',
        type=argparse.FileType('rt'),
        default=sys.stdin,
        help='The file containing the description of the cave network.')
    return parser.parse_args()


def main():
    """Begin script execution logic."""
    args = parse_args()
    caves = Caves()
    for line in args.input_file:
        caves.add_connection(line)
    paths_to_end = caves.find_all_paths_to_end()
    print(len(paths_to_end))
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
