#!/usr/bin/env python3

import sys
from typing import Any, List
import argparse

class Cube:
    ON: bool = True
    OFF: bool = False

    def __init__(self):
        self._state = Cube.OFF

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'Cube({self._state})'

    def is_on(self) -> bool:
        """
        Return whether the reactor is on.

        Return (bool): True if the reactor is on, False otherwise.

        >>> c = Cube()
        >>> c.is_on()
        False
        >>> c.turn_on()
        True
        >>> c.is_on()
        True
        """
        return self._state == Cube.ON

    def is_off(self) -> bool:
        """
        Return whether the reactor is off.

        Return (bool): True if the reactor is off, False otherwise.

        >>> c = Cube()
        >>> c.is_off()
        True
        >>> c.turn_on()
        True
        >>> c.is_off()
        False
        """
        return self._state == Cube.OFF

    def turn_on(self) -> bool:
        """
        Turn the cube on.

        Returns (bool): True if the cube was off and now it is on. Return
        False if it was already on.

        >>> c = Cube()
        >>> c.turn_on()
        True
        >>> c.turn_on()
        False
        """
        if self._state == Cube.OFF:
            self._state = Cube.ON
            return True
        else:
            return False

    def turn_off(self) -> bool:
        """
        Turn the cube off.

        Returns (bool): True if the cube was on and now it is off. Return
        False if it was already off.

        >>> c = Cube()
        >>> c.turn_off()
        False
        >>> c.turn_on()
        True
        >>> c.turn_off()
        True
        """
        if self._state == Cube.ON:
            self._state = Cube.OFF
            return True
        else:
            return False

class Reactor:

    def __init__(self, side_size: int = 101):
        """
        Initialize a reactor cube, with side_size cubes on a side.

        Arguments:
            side_size (int): The number of reactors on a side.
        """
        if side_size % 2 == 0:
            raise ValueError(f"side_size should be odd. Was: {side_size}")

        self._cubes: List[List[List[Cube]]] = []
        for x in range(side_size):
            self._cubes.append([])
            for y in range(side_size):
                self._cubes[x].append([])
                for z in range(side_size):
                    self._cubes[x][y].append(Cube())

    def off_count(self) -> int:
        """
        The number of cubes that are off.

        >>> r = Reactor(3)
        >>> r.off_count()
        27
        """
        count = 0
        for x in self._cubes:
            for y in x:
                for cube in y:
                    if cube.is_off():
                        count += 1
        return count

    def on_count(self) -> int:
        """
        The number of cubes that are off.

        >>> r = Reactor(3)
        >>> r.on_count()
        0
        >>> r.process_step('on x=-1..1,y=0..0,z=1..1')
        3
        """
        count = 0
        for x in self._cubes:
            for y in x:
                for cube in y:
                    if cube.is_on():
                        count += 1
        return count


    def _parse_step(self, step_description: str) -> List[Any]:
        """
        Parse the step into the command and its ranges.

        >>> r = Reactor(3)
        >>> r._parse_step('on x=-1..-1,y=0..0,z=1..1')
        [True, 0, 1, 1, 2, 2, 3]
        """
        ret: List[Any] = []
        command, ranges_str = step_description.split()
        if command.lower()  == 'on':
            ret.append(Cube.ON)
        if command.lower()  == 'off':
            ret.append(Cube.OFF)
        ranges = ranges_str.split(',')

        offset = int(len(self._cubes) / 2)
        for r in ranges:
            axis, r = r.split('=')
            begin_str, end_str = r.split('..')

            begin = int(begin_str) + offset
            ret.append(begin)

            end = int(end_str) + offset + 1
            ret.append(end)
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
        >>> r.process_step('on x=5..10,y=0..0,z=1..1')
        0
        """
        command, xbegin, xend, ybegin, yend, zbegin, zend = \
                self._parse_step(step_description)

        count = 0
        try:
            for x in self._cubes[xbegin:xend]:
                for y in x[ybegin:yend]:
                    for cube in y[zbegin:zend]:
                        if command == Cube.ON:
                            if cube.turn_on():
                                count += 1
                        else:
                            if cube.turn_off():
                                count -= 1
        except IndexError:
            return 0
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
            'reboot_steps_file',
            type=argparse.FileType('rt'),
            default=sys.stdin,
            help='A file containing the reboot steps.')
    return parser.parse_args()


def main():
    args = parse_args()

    r = Reactor()
    count = r.process_steps(args.reboot_steps_file)
    print(count)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    sys.exit(main())
