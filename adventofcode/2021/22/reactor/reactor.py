#!/usr/bin/env python3

import sys
from typing import Any, List, Dict, Set
import argparse


class Reactor:
    """
    Manages the set of all ActiveCube objects.
    """
    _active_cubes: Dict[int, Dict[int, Dict[int, bool]]]
    _on_count: int
    _min_valid: int
    _max_valid: int
    CUBE_ON = True
    CUBE_OFF = False

    def __init__(self, side_size: int = 0):
        """
        Initialize a reactor cube, with side_size cubes on a side.

        Arguments:
            side_size (int): The number of reactors on a side. If the size
            is 0, then the reactor is unbounded in size.
        """
        if side_size != 0 and side_size % 2 == 0:
            raise ValueError(f'side_size must be 0 or an odd value. Got {side_size}.')
        self._active_cubes = {}
        self._on_count = 0
        self._side_size = side_size
        self._min_valid = -1 * int(side_size / 2)
        self._max_valid = int(side_size / 2)


    def on_count(self) -> int:
        """
        The number of cubes that are on.

        >>> r = Reactor()
        >>> r.on_count()
        0
        >>> r.process_step('on x=-1..1,y=0..0,z=1..1')
        3
        >>> r.on_count()
        3
        >>> r.process_step('on x=-1..1,y=0..0,z=1..1')
        0
        >>> r.on_count()
        3
        """
        return self._on_count


    def _parse_step(self, step_description: str) -> List[Any]:
        """
        Parse the step into the command and its useful ranges.

        The first index indicates whether the given range is outside the
        reactor size and therefore should be skipped.

        >>> r = Reactor(3)
        >>> r._parse_step('on x=-1..-1,y=0..0,z=1..1')
        [False, True, -1, 0, 0, 1, 1, 2]

        >>> r = Reactor(3)
        >>> r._parse_step('on x=-4..-1,y=0..0,z=1..1')
        [True, True, -4, 0, 0, 1, 1, 2]
        """
        ret: List[Any] = []
        command, ranges_str = step_description.split()
        if command.lower()  == 'on':
            ret.append(Reactor.CUBE_ON)
        if command.lower()  == 'off':
            ret.append(Reactor.CUBE_OFF)
        ranges = ranges_str.split(',')

        should_skip = False
        for r in ranges:
            axis, r = r.split('=')
            begin_str, end_str = r.split('..')

            begin = int(begin_str)
            if self._min_valid != 0 and begin < self._min_valid:
                should_skip = True
            ret.append(begin)

            end = int(end_str) + 1
            if self._max_valid != 0 and end - 1 > self._max_valid:
                should_skip = True
            ret.append(end)

        ret.insert(0, should_skip)
        return ret


    def process_step(self, step_description: str) -> int:
        """
        Process the described step.

        A range check is done on the steps and if an index is out of range, then
        no processing is done.

        Returns (int): The number of cubes turned on. If the step turns cubes
        off, then the number will be negative. If the state of no cubes is
        changed, a 0 will be returned.

        >>> r = Reactor(3)
        >>> r.process_step('on x=-1..-1,y=0..0,z=1..1')
        1
        >>> r.on_count()
        1

        # Outside the range.
        >>> r.process_step('on x=5..10,y=0..0,z=1..1')
        0
        """
        should_skip, command, xbegin, xend, ybegin, yend, zbegin, zend = \
                self._parse_step(step_description)

        count = 0
        if should_skip:
            return count

        if command == Reactor.CUBE_ON:
            for x in range(xbegin, xend):
                if x not in self._active_cubes:
                    self._active_cubes[x] = {}
                for y in range(ybegin, yend):
                    if y not in self._active_cubes[x]:
                        self._active_cubes[x][y] = {}
                    for z in range(zbegin, zend):
                        if z not in self._active_cubes[x][y]:
                            self._active_cubes[x][y][z] = True
                            count += 1
        else:
            # Disabling cubes.
            for x in range(xbegin, xend):
                for y in range(ybegin, yend):
                    for z in range(zbegin, zend):
                        try:
                            del self._active_cubes[x][y][z]
                            count -= 1
                        except KeyError:
                            continue
        self._on_count += count
        return count

    def process_steps(self, reboot_steps: tuple) -> int:
        """
        Process the steps given in the iterable of reboot_steps.

        Return (int): The final number of reactors that are on after processing
        the steps.

        >>> r = Reactor(3)
        >>> r.process_steps(['on x=-1..1,y=0..0,z=1..1', 'off x=-1..-1,y=0..0,z=1..1'])
        2
        """
        count = 0
        for step in reboot_steps:
            count += self.process_step(step)
        return count


def parse_args():
    parser = argparse.ArgumentParser(
            description='Manage a reactor and rebooting it.')
    parser.add_argument(
            '-s', '--side_size',
            type=int,
            default=0,
            help='The number of cubes on a side of the reactor. 0 means unlimited.')
    parser.add_argument(
            'reboot_steps_file',
            type=argparse.FileType('rt'),
            default=sys.stdin,
            help='A file containing the reboot steps.')
    return parser.parse_args()


def main():
    args = parse_args()

    r = Reactor(args.side_size)
    count = r.process_steps(args.reboot_steps_file)
    print(count)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    sys.exit(main())
