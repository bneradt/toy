#!/usr/bin/env python3

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Parse expense reports.')

    parser.add_argument(
        'expense_report',
        type=argparse.FileType('r'),
        help='The file containing the expense report.')

    parser.add_argument(
        '-3', '--three',
        action='store_true',
        help='Return the product of three entries that sum to 2020. '
        'By default, the product of two entries that sum to 2020 '
        'is returned.')

    return parser.parse_args()


def find_two_entry_product(numbers):
    """
    Given the list of numbers, print the product of two that sum to 2020.

    numbers (list): A list of integers.

    Return (int): The product of two entries in numbers that sum to 2020.

    Raises:
        ValueError if no two entries in numbers sums to 2020.

    >>> l = [1721, 675, 299]
    >>> find_two_entry_product(l)
    514579
    """
    for index, number1 in enumerate(numbers):
        for number2 in numbers[index+1:]:
            if (number1 + number2) == 2020:
                return number1 * number2
    raise ValueError('No two entries in numbers sums to 2020')


def find_three_entry_product(numbers):
    """
    Given the list of numbers, print the product of three that sum to 2020.

    numbers (list): A list of integers.

    Return (int): The product of three entries in numbers that sum to 2020.

    Raises:
        ValueError if no three entries in numbers sums to 2020.

    >>> l = [979, 366, 675]
    >>> find_three_entry_product(l)
    241861950
    """
    for index1, number1 in enumerate(numbers):
        for index2, number2 in enumerate(numbers[index1+1:]):
            for number3 in numbers[index1 + index2 + 2:]:
                if (number1 + number2 + number3) == 2020:
                    return number1 * number2 * number3
    raise ValueError('No three entries in numbers sums to 2020')


def main():
    args = parse_args()

    numbers = []
    for line in args.expense_report:
        number = int(line)
        if number > 2020:
            continue
        numbers.append(number)

    try:
        if args.three:
            product = find_three_entry_product(numbers)
        else:
            product = find_two_entry_product(numbers)
    except ValueError:
        num_entries = 'three' if args.three else 'two'
        print(f'No {num_entries} numbers in the expense report sum to 2020.')
        return 1

    print(product)
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
