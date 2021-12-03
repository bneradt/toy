#!/usr/bin/env python3

import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(
            description="Process the planned submarine course.")

    parser.add_argument(
            "course",
            type=argparse.FileType('rt'),
            default=sys.stdin,
            help="The submarine course instructions.")
    parser.add_argument(
            "-w", "--wrong_instructions",
            default=False,
            action='store_true',
            help="Use this to follow the old, wrong instructions.")

    return parser.parse_args()

class Submarine:

    def __init__(self):
        """
        Initialize the submarine.

        >>> s = Submarine()
        >>> s.get_horizontal_position()
        0
        >>> s.get_depth()
        0
        """
        self._horizontal_position = 0
        self._depth = 0
        self._aim = 0

    def get_depth(self):
        """
        Return the submarine's depth.

        Return (int): The depth.
        """
        return self._depth

    def get_horizontal_position(self):
        """
        Return the submarine's horizontal position.

        Return (int): The horizontal position.
        """
        return self._horizontal_position 
    
    def get_position_product(self):
        """
        Return the product of the horizontal position and depth.

        Return (int): The product of the horizontal and depth.
        """
        return self._horizontal_position * self._depth

    def follow_wrong_instruction(self, instruction):
        """
        Have the submarine follow the given instruction, the old,
        incorrect way.

        Instructions are made up of a direction and a magnitude of how far to
        move in that direction. Directions can be one of:

            forward: increase the horizontal position.
            down: increase the depth.
            up: decrease the depth.

        Here are some example values for @a instruction:

            forward 5
            down 5
            up 3

        Arguments:
            instruction (str): The desciption of how the submarine should move.

        Raise:
            ValueError if the instruction does not fit the expected format.

        >>> s = Submarine()

        >>> s.follow_wrong_instruction('forward 5')
        >>> s.get_horizontal_position()
        5
        >>> s.get_depth()
        0

        >>> s.follow_wrong_instruction('down 8')
        >>> s.get_depth()
        8
        """
        split_line = instruction.split()
        if len(split_line) != 2:
            raise ValueError(f'Poorly formatted instuction: "{instruction}"')

        direction, magnitude = split_line
        try:
            magnitude = int(magnitude)
        except ValueError:
            raise ValueError(f'Magnitude in instruction is not an int: "{magnitude}"')

        if direction == 'forward':
            self._horizontal_position += magnitude
        elif direction == 'down':
            self._depth += magnitude
        elif direction == 'up':
            self._depth -= magnitude
        else:
            raise ValueError(f'Unrecognized direction: "{direction}"')

    def follow_wrong_instructions(self, instructions):
        """
        Follow a set of instructions, per @a follow_instruction.

        Arguments:
            instructions: iterable of instruction strings.

        Raise:
            ValueError if any of the instructions do not fit the expected
            format.

        >>> s = Submarine()
        >>> instructions = ['forward 8', 'down 3']
        >>> s.follow_wrong_instructions(instructions)
        >>> s.get_horizontal_position()
        8
        >>> s.get_depth()
        3
        """
        for instruction in instructions:
            self.follow_wrong_instruction(instruction)


    def follow_instruction(self, instruction):
        """
        Have the submarine follow the given instruction, correctly.

        Instructions are made up of a direction and a magnitude of how far to
        move in that direction. Directions can be one of:

            'down X': increases your aim by X units.
            'up X': decreases your aim by X units.
            'forward X': does two things:
                It increases your horizontal position by X units.
                It increases your depth by your aim multiplied by X.


        Here are some example values for @a instruction:

            forward 5
            down 5
            up 3

        Arguments:
            instruction (str): The desciption of how the submarine should move.

        Raise:
            ValueError if the instruction does not fit the expected format.

        >>> s = Submarine()

        >>> s.follow_instruction('forward 5')
        >>> s.get_horizontal_position()
        5
        >>> s.get_depth()
        0

        >>> s.follow_instruction('down 5')
        >>> s.get_depth()
        0

        >>> s.follow_instruction('forward 1')
        >>> s.get_horizontal_position()
        6
        >>> s.get_depth()
        5
        """
        split_line = instruction.split()
        if len(split_line) != 2:
            raise ValueError(f'Poorly formatted instuction: "{instruction}"')

        direction, magnitude = split_line
        try:
            magnitude = int(magnitude)
        except ValueError:
            raise ValueError(f'Magnitude in instruction is not an int: "{magnitude}"')

        if direction == 'forward':
            self._horizontal_position += magnitude
            self._depth += self._aim * magnitude
        elif direction == 'down':
            self._aim += magnitude
        elif direction == 'up':
            self._aim -= magnitude
        else:
            raise ValueError(f'Unrecognized direction: "{direction}"')

    def follow_instructions(self, instructions):
        """
        Follow a set of instructions, per @a follow_instruction.

        Arguments:
            instructions: iterable of instruction strings.

        Raise:
            ValueError if any of the instructions do not fit the expected
            format.

        >>> s = Submarine()
        >>> instructions = ['forward 8', 'down 3', 'forward 2']
        >>> s.follow_instructions(instructions)
        >>> s.get_horizontal_position()
        10
        >>> s.get_depth()
        6
        """
        for instruction in instructions:
            self.follow_instruction(instruction)

def main():
    args = parse_args();
    submarine = Submarine()
    if args.wrong_instructions:
        submarine.follow_wrong_instructions(args.course)
    else:
        submarine.follow_instructions(args.course)
    print(submarine.get_position_product())
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
