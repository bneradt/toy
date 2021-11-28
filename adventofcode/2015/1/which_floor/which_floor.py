#!/usr/bin/env python3

import argparse
import sys


def description_to_final_floor(description):
    """
    Convert the given description to a floor number.

    Args:
        description (str): A parentheses style description of the floor number.

    Raises:
        ValueError if @a description contains anything other than an open or
        closed parenthesis.

    Return
        (int) An integer describing the final floor level.

    >>> description_to_final_floor('(()(()(')
    3
    """
    floor = 0
    for character in description:
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1
        else:
            raise ValueError(
                f"Unexpected character '{character}' in: \"{description}\"")
    return floor


def get_first_basement_position(description):
    """
    Given the floor description, determine the first position in the
    description in which Santa is in the basement.

    Indexing starts at 1.

    Args:
        description (str): A parentheses style description of the floor number.

    Raises:
        ValueError if @a description contains anything other than an open or
        closed parenthesis.

    Return
        (int) The position in @a description in which Santa first is in the
        basement.

    >>> get_first_basement_position('()())')
    5
    """
    floor = 0
    position = 1
    for character in description:
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1
        else:
            raise ValueError(
                f"Unexpected character '{character}' in: \"{description}\"")

        if floor == -1:
            return position

        position += 1
    return floor


def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert a floor description to an integer.')

    parser.add_argument(
        '-b', '--find_basement_position',
        action='store_true',
        default=False,
        help='Find the first position in which Santa is in the basement.')

    parser.add_argument(
        'floor_description', type=str,
        help='A description of which floor Santa should go to.')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.find_basement_position:
        position = get_first_basement_position(args.floor_description)
        print(position)
    else:
        floor = description_to_final_floor(args.floor_description)
        print(floor)
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
