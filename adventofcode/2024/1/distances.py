#!/usr/bin/env python3
'''Find the distance between sorted lists.'''

import argparse
import bisect
import sys

def calculate_distance(list1: list[int], list2: list[int]) -> int:
    '''Calculate the distance between the two lists.
    :param list1: The first sorted list of integers.
    :param list2: The second sorted list of integers.
    :return: The sum of the differences between list1 and list2.
    :examples:
    >>> calculate_distance([], [])
    0
    >>> calculate_distance([2], [4])
    2
    >>> calculate_distance([2], [4])
    2
    >>> l1 = [4, 5, 6, 10]
    >>> l2 = [5, 5, 8, 9]
    >>> calculate_distance(l1, l2)
    4
    '''
    sum: int = 0
    for index in range(len(list1)):
        i: int = list1[index]
        j: int = list2[index]
        if i >= j:
            sum += i - j
        else:
            sum += j - i
    return sum


def calculate_similarity(ids: list[int], multipliers: dict[int, int]) -> int:
    '''Calculate the similarity of list1 using multipliers.
    :param ids: A list of values.
    :param multipliers: The list of multipliers for each value in list.
    :return: The calculated similarity.
    :example:
    >>> calculate_similarity([], {})
    0
    >>> calculate_similarity([1], {1: 3})
    3
    >>> calculate_similarity([0, 10, 5], {0: 3, 10: 4, 5: 5})
    65
    '''
    similarity = 0
    for id in ids:
        try:
            similarity += id * multipliers[id]
        except KeyError:
            # Not in the list, so similarity does not increase.
            pass
    return similarity


def parse_args() -> argparse.Namespace:
    '''Parse the command line arguments.
    
    :return: The parsed command line arguments.
    '''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input',
        type=argparse.FileType('r'),
        help='The input file with the two lists.')
    parser.add_argument(
        '-s', '--similarity',
        action='store_true',
        help='Find the similarity score instead of the distance.')
    return parser.parse_args()

def main() -> int:
    '''Calculate distances.
    :return: The exit code.
    '''
    args = parse_args()
    list1: list[int] = []
    list2: list[int] = []
    multipliers: dict[int, int] = {}
    for line in args.input:
        first, second = line.strip().split()
        first, second = int(first), int(second)
        bisect.insort(list1, first)
        if args.similarity:
            count = multipliers.setdefault(second, 0)
            multipliers[second] = count + 1
        else:
            bisect.insort(list2, second)
    if args.similarity:
        value = calculate_similarity(list1, multipliers)
    else:
        value = calculate_distance(list1, list2)
    print(value)
    return 0

if __name__ == '__main__':
    sys.exit(main())
