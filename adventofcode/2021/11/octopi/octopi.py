#!/usr/bin/env python3

import argparse
import sys
from typing import List

class Octopus:
    """
    Represent a "Dumbo Octopus" which lights up over time.
    """

    _energy_level: int
    _neighbors: List['Octopus']
    _flashed_this_step: bool
    _flash_count: int

    def __init__(self, energy_level: int):
        self._energy_level = energy_level
        self._neighbors = []
        self._flashed_this_step = False
        self._flash_count = 0

    def __str__(self):
        return f'{self._energy_level}'

    def get_energy_level(self) -> int:
        """
        Return the energy level of the Octopus.

        >>> o = Octopus(3)
        >>> o.get_energy_level()
        3
        >>> o.start_step()
        >>> o.get_energy_level()
        4
        """
        return self._energy_level

    def get_flash_count(self) -> int:
        """
        Return the number of times self has ever flashed.

        >>> o = Octopus(9)
        >>> o.get_flash_count()
        0
        >>> o.start_step()
        >>> o.get_flash_count()
        1
        """
        return self._flash_count

    def add_neighbor(self, other: 'Octopus') -> None:
        """
        Add a neighbor octopus within line of site of self's flashes.

        This also adds self as a neighbor to other.
        """
        if other in self._neighbors:
            # This will prevent infinite recursion.
            return
        self._neighbors.append(other)
        other.add_neighbor(self)

    def is_neighbor_with(self, other: 'Octopus') -> bool:
        """
        Return whether self is a neighbor of other.

        >>> o1 = Octopus(4)
        >>> o2 = Octopus(9)

        >>> o1.is_neighbor_with(o2)
        False

        >>> o1.add_neighbor(o2)
        >>> o1.is_neighbor_with(o2)
        True
        >>> o2.is_neighbor_with(o1)
        True
        """
        return other in self._neighbors

    def finish_step(self) -> None:
        """
        Indicate that the step has completed. Prepare for the next step.
        """
        self._flashed_this_step = False
        if self._energy_level >= 10:
            self._energy_level = 0

    def start_step(self) -> None:
        """
        Process one time step.
        """
        self._increment_energy_level()

    def get_shined_on(self) -> None:
        """
        A neighbor Octopus flashed and shined on self.

        >>> o = Octopus(9)
        >>> o.get_flash_count()
        0
        >>> o.get_shined_on()
        >>> o.get_flash_count()
        1
        """
        self._increment_energy_level()

    def _increment_energy_level(self) -> None:
        """
        Increment self's energy level by one, flashing if appropriate.
        """
        self._energy_level += 1
        if self._energy_level >= 10:
            self._flash()

    def _flash(self) -> None:
        """
        Flash light on the neighbors, unless self has flashed already.
        """
        if self._flashed_this_step:
            return
        self._flashed_this_step = True
        self._flash_count += 1
        for neighbor in self._neighbors:
            neighbor.get_shined_on()

class OctopusPod:
    """
    A collection of 100 Octopi, in a 10 by 10 grid.
    """

    def __init__(self, num_columns=10):
        """
        Create the pod of octopi.

        Arguments:
            num_columns (int): The number of columns in the pod.
        """
        self._grid = [[]]
        self._octopi = []
        self._num_columns = num_columns

    def __eq__(self, other) -> bool:
        """
        self and other are equal if all energy levels in all the same positions
        are equal.

        """
        for i, octopus in enumerate(self._octopi):
            if octopus.get_energy_level() != other._octopi[i].get_energy_level():
                return False
        return True

    def __str__(self) -> str:
        """
        Print the pod of octopi, showing each of their energy levels.

        >>> o = OctopusPod(3)
        >>> o.add_octopi([4, 0, 5])
        >>> o.add_octopi([9, 8, 9])
        >>> o.add_octopi([1, 5, 3])
        >>> print(o)
        405
        989
        153
        """
        s = ''
        for row in self._grid:
            s += ''.join([str(i) for i in row]) + '\n'
        return s.strip()

    def add_octopus(self, energy_level: int):
        """
        Add an octopus to the pod with the given energy level.

        The octopi are added from top left to bottom right.

        Arguments:
            energy_level (int): Create an Octopus with the given energy level
            and add it to the pod.
        """

        row = self._grid[-1]
        if len(row) == self._num_columns:
            row = []
            self._grid.append(row)

        row_number = len(self._grid) - 1
        column_number = len(row)
        new_octopus = Octopus(energy_level)
        self._octopi.append(new_octopus)
        row.append(new_octopus)

        # Configure the neighbors.
        if column_number > 0:
            previous_octopus = row[column_number - 1]
            previous_octopus.add_neighbor(new_octopus)

        if row_number > 0:
            previous_row = self._grid[row_number - 1]
            above_octopus = previous_row[column_number]
            above_octopus.add_neighbor(new_octopus)

            if column_number > 0:
                above_left_octopus = previous_row[column_number - 1]
                above_left_octopus.add_neighbor(new_octopus)

            if column_number < (self._num_columns - 1):
                above_right_octopus = previous_row[column_number + 1]
                above_right_octopus.add_neighbor(new_octopus)

    def add_octopi(self, energy_levels: List[int]):
        """
        Add an iterable of octopi.

        Arguments:
            energy_levels List[int]: A set of energy levels describing the new
            octopi to create and add, in order.
        """
        for energy_level in energy_levels:
            self.add_octopus(energy_level)

    def get_historic_flash_count(self):
        """
        Return how many flashes have happened over the lifetime of the pod.

        >>> o = OctopusPod(3)
        >>> o.add_octopi([4, 0, 5])
        >>> o.add_octopi([9, 8, 9])
        >>> o.add_octopi([1, 5, 3])
        >>> o.get_historic_flash_count()
        0
        >>> o.step()
        >>> o.get_historic_flash_count()
        3
        """
        flash_count = 0
        for octopus in self._octopi:
            flash_count += octopus.get_flash_count()
        return flash_count

    def step(self):
        """
        Have each of the octopi transition in a single step.

        >>> o = OctopusPod(3)
        >>> o.add_octopi([4, 0, 5])
        >>> o.add_octopi([9, 8, 9])
        >>> o.add_octopi([1, 5, 3])
        >>> o.step()
        >>> print(o)
        748
        000
        496
        """
        for octopus in self._octopi:
            octopus.start_step()
        for octopus in self._octopi:
            octopus.finish_step()

def parse_args():
    parser = argparse.ArgumentParser(
            description='Observe the flashes of a pod of octopi.')

    parser.add_argument(
            '-n', '--num_steps',
            type=int,
            default=100,
            help='The number of steps to observe the pod with.')

    parser.add_argument(
            '-s', '--get_synchronized_step_count',
            action="store_true",
            default=False,
            help='Find the step at which all the octopi flash at once. '
                 'Otherwise the flash count at --num_steps is printed.')

    parser.add_argument(
            'input_file',
            type=argparse.FileType('rt'),
            default=sys.stdin,
            help='The input file describing the octopi pod.')

    return parser.parse_args()

def main():
    args = parse_args()
    pod = OctopusPod()
    for line in args.input_file:
        energy_levels = [int(i) for i in line.strip()]
        if len(energy_levels) != 10:
            ValueError("Expected 10 rows of 10 octopi each.")
        pod.add_octopi(energy_levels)

    if args.get_synchronized_step_count:
        target = OctopusPod()
        for i in range(100):
            target.add_octopus(0)

        step_count = 0
        while target != pod:
            pod.step()
            step_count += 1
        print(step_count)
    else:
        for step_count in range(args.num_steps):
            pod.step()
        print(pod.get_historic_flash_count())
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    sys.exit(main())
