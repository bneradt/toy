#!/usr/bin/env python3
"""Calculate the position of least fuel cost.

Given a set of crab positions, calculate the position of least possible
cost to which all the crabs can unite.
"""


import argparse
import sys
from typing import List

class Swarm:
    """A swarm of crabs.

    This represents a swarm of crabs.
    """

    _positions: List[int]

    def __init__(self, positions: List[int]):
        """Construct a swarm of crabs from its positions.

        Arguments
        ---------
        positions: List[int]
            The set of initial positions of the crabs.
        """
        self._positions = positions

    def calculate_compounding_position_cost(self, position: int) -> int:
        """Calculate the total cost of the position if each movement costs
        1 unit more than the one before it for each crab.

        Parameters
        ----------
        position: int
            The position for which the cost of the swarm moving to should be
            calculated.

        Returns
        -------
        int
            Return the calculated cost of all the crabs moving to the given
            position.

        >>> s = Swarm([1, 2, 3])
        >>> s.calculate_compounding_position_cost(2)
        2
        >>> s.calculate_compounding_position_cost(3)
        4
        """

        def calculate_crab_cost(start: int, end: int) -> int:
            """Calculate the cost of the crab going from start to end, with
            each step costing one more than the one before.

            Parameters
            ----------
            start: int
                The starting position of the crab.
            end: int
                The ending position of the crab.

            Returns
            -------
            int
                The cost of the crab going from start to end.

            >>> calculate_crab_cost(16, 5)
            66
            >>> calculate_crab_cost(1, 5)
            10

            """
            diff = abs(end - start)
            return int((diff / 2) * (diff + 1))

        costs = [calculate_crab_cost(p, position) for p in self._positions]
        return sum(costs)

    def calculate_position_cost(self, position: int) -> int:
        """Calculate the cost of the provided position.

        Parameters
        ----------
        position: int
            The position for which the cost of the swarm moving to should be
            calculated.

        Returns
        -------
        int
            Return the calculated cost of all the crabs moving to the given
            position.

        >>> s = Swarm([1, 2, 3])
        >>> s.calculate_position_cost(2)
        2
        >>> s.calculate_position_cost(3)
        3

        """
        distances = [abs(p - position) for p in self._positions]
        return sum(distances)

    def find_least_cost_position(self) -> int:
        """Find the position of least cost for the swarm.

        Returns
        -------
        int
            The position which requires the least amount of movement
            for the crabs to which all the crabs can align to.

        >>> s = Swarm([1, 2, 3])
        >>> s.find_least_cost_position()
        2
        """
        min_position = min(self._positions)
        max_position = max(self._positions)
        least_cost_position = 0
        least_cost_position_cost = None
        for possible_position in range(min_position, max_position + 1):
            position_cost = self.calculate_position_cost(possible_position)
            if (least_cost_position_cost is None or
                    position_cost < least_cost_position_cost):
                least_cost_position = possible_position
                least_cost_position_cost = position_cost
        return least_cost_position

    def find_least_compounding_cost_position(self) -> int:
        """Find the position of least cost for the swarm.

        Returns
        -------
        int
            The position which requires the least amount of movement
            for the crabs to which all the crabs can align to.

        >>> s = Swarm([1, 2, 3])
        >>> s.find_least_cost_position()
        2
        """
        min_position = min(self._positions)
        max_position = max(self._positions)
        least_cost_position = 0
        least_cost_position_cost = None
        for possible_position in range(min_position, max_position + 1):
            position_cost = self.calculate_compounding_position_cost(
                possible_position)
            if (least_cost_position_cost is None or
                    position_cost < least_cost_position_cost):
                least_cost_position = possible_position
                least_cost_position_cost = position_cost
        return least_cost_position


def parse_args():
    """Parse the user's command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=argparse.FileType('rt'),
        default=sys.stdin,
        help='The input file containing the initial swarm position.')
    parser.add_argument(
        '-c', '--use_compounding_costs',
        action='store_true',
        default=False,
        help='Use the compounding crab costs for crab movement.')
    return parser.parse_args()


def main() -> int:
    """Implement the main entry point into this file."""
    args = parse_args()
    positions_string = args.input_file.readline()
    swarm_positions = [int(position)
                       for position in positions_string.strip().split(',')]
    swarm = Swarm(swarm_positions)
    if args.use_compounding_costs:
        least_cost_position = swarm.find_least_compounding_cost_position()
        print(swarm.calculate_compounding_position_cost(least_cost_position))
    else:
        least_cost_position = swarm.find_least_cost_position()
        print(swarm.calculate_position_cost(least_cost_position))
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
