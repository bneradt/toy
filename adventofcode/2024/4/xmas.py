#!/usr/bin/env python3
'''Find all XMAS in a wordsearch.'''

import argparse
import sys

from typing import List

def parse_args() -> argparse.Namespace:
    '''Parse the command line arguments.
    :return: The parsed arguments.
    '''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=argparse.FileType('r'), help='The wordsearch input file.')
    return parser.parse_args()


def has_xmas_from_with_slope(word_search: List[List[str]], start_row: int, start_column: int, delta_row: int, delta_column: int) -> bool:
    '''Find XMAS from (start_row, start_column) searching (delta_row, run).

    :param word_search: The word search input.
    :param start_row: row dimension from which to start.
    :param start_column: column dimension from which to start.
    :param delta_row: The incremental row dimension to adjust looking for xmas.
    :param delta_column: The incremental column dimension to adjust looking for xmas.

    :return: True if XMAS is in the puzzle from (start_row, start_column) running with
    delta_row, delta_column , False otherwise.

    :example:
    >>> t =     [['.', '.', 'X', '.', '.', '.']]
    >>> t.append(['.', 'S', 'A', 'M', 'X', '.'])
    >>> t.append(['.', 'A', '.', '.', 'A', '.'])
    >>> t.append(['X', 'M', 'A', 'S', '.', 'S'])
    >>> t.append(['.', 'X', '.', '.', '.', '.'])

    >>> has_xmas_from_with_slope(t, 0, 0, 1, 0)
    False
    >>> has_xmas_from_with_slope(t, 0, 2, 1, 0)
    False
    >>> has_xmas_from_with_slope(t, 0, 2, 1, 1)
    True
    >>> has_xmas_from_with_slope(t, 4, 1, -1, 0)
    True
    '''
    this_row = start_row
    this_column = start_column
    for finding_char in ['X', 'M', 'A', 'S']:
        if this_row == -1 or this_row >= len(word_search):
            return False
        if this_column == -1 or this_column >= len(word_search[this_row]):
            return False

        if word_search[this_row][this_column] != finding_char:
            return False
        this_row += delta_row
        this_column += delta_column
    return True

def count_xmas_from(word_search: List[List[str]], start_row: int, start_column: int) -> int:
    '''Count all occurences of XMAS from (start_row, start_column)
    :param word_search: The word search input.
    :param start_row: row dimension from which to start.
    :param start_column: column dimension from which to start.

    :return: The number of XMAS words starting from (start_row, start_column).

    :example:
    >>> t =     [['.', '.', 'X', '.', '.', '.']]
    >>> t.append(['.', 'S', 'M', 'M', 'X', '.'])
    >>> t.append(['.', 'A', 'A', '.', 'A', '.'])
    >>> t.append(['X', 'M', 'S', 'S', '.', 'S'])
    >>> t.append(['.', 'X', '.', '.', '.', '.'])

    >>> count_xmas_from(t, 0, 2)
    2
    >>> count_xmas_from(t, 4, 1)
    1
    >>> count_xmas_from(t, 0, 1)
    0
    >>>
    '''
    count = 0
    for delta_row in (-1, 0, 1):
        for delta_column in (-1, 0, 1):
            if (delta_row, delta_column) == (0, 0):
                continue
            if has_xmas_from_with_slope(word_search, start_row, start_column, delta_row, delta_column):
                count += 1
    return count


def count_all_xmas(word_search: List[List[str]]) -> int:
    '''Count the number of XMAS in the word search.
    :param word_search: The puzzle input.
    :return: The number of times XMAS occurs in word_search.
    '''
    count = 0
    for row_index, row in enumerate(word_search):
        for column_index, column in enumerate(row):
            count += count_xmas_from(word_search, row_index, column_index)
    return count


def main() -> int:
    '''Find XMAS in the wordsearch.
    :return: The exit code.
    '''
    args = parse_args()
    
    word_search: List[List[str]] = []
    for line in args.input:
        word_search.append([])
        for char in line.strip():
            word_search[-1].append(char)

    count = count_all_xmas(word_search)
    print(count)
    return 0

if __name__ == '__main__':
    sys.exit(main())
