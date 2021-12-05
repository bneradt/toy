#!/usr/bin/env python3

import argparse
import sys

class Place:
    """
    A place on a bingo card.
    """
    def __init__(self, number: int):
        self._number: int = number
        self._marked: bool = False

    def __bool__(self) -> bool:
        """
        An object is True if it is marked, false otherwise.

        >>> p = Place(2)
        >>> not p
        True
        >>> p.mark_if_matches(2)
        True
        >>> not p
        False
        """
        return self._marked

    def get_number(self) -> int:
        """
        Return the number associated with this Bingo place.

        Return (int): The number associated with the place.

        >>> p = Place(3)
        >>> p.get_number()
        3
        """
        return self._number
    
    def is_marked(self) -> bool:
        """
        Return whether the place has been marked.

        Return (bool): True if the place is marked, false otherwise.

        >>> p = Place(3)
        >>> p.is_marked()
        False
        >>> p.mark_if_matches(3)
        True
        >>> p.is_marked()
        True
        """
        return self._marked
    
    def mark_if_matches(self, number: int) -> bool:
        """
        Mark this place on the board if the number matches the number of the
        place.

        Return (bool): True if the number matched and the board was marked,
        false otherwise.

        >>> p = Place(3)
        >>> p.mark_if_matches(3)
        True
        >>> p.is_marked()
        True
        """
        if number == self._number:
            self._marked = True
            return True
        return False

class Board:
    def __init__(self, rows: list[list[int]]) -> None:
        """
        Initialize a board with a list of rows.

        >>> board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        """

        self._rows: list[list[Place]] = []
        self._winning_number: int = 0
        for row_index, row in enumerate(rows):
            self._rows.append([])
            for column_index, number in enumerate(row):
                self._rows[row_index].append(Place(number))

    def is_winning(self) -> bool:
        """
        Indicate whether the board has a completed row or column.

        Return (bool): True if the board has a row or column that is completely
        marked, False otherwise.
        """
        for row in self._rows:
            if all(row):
                return True

        # Check for columns that have all marked.
        num_columns = len(self._rows[0])
        for column_index in range(num_columns):
            for row_index in range(len(self._rows)):
                if not self._rows[row_index][column_index]:
                    break
            else:
                return True

    def mark_number(self, number: int) -> bool:
        """
        Mark the places on the board with the given number.

        Return (bool): True if there is a row or column that now has every
        place marked.
        """

        # Be aware that the board may have duplicate numbers, so
        # don't break early if something matches.
        a_place_was_marked: bool = False
        for row in self._rows:
            for place in row:
                a_place_was_marked |= place.mark_if_matches(number)

        if not a_place_was_marked:
            return False

        # Check for rows that have all marked.
        if self.is_winning():
            if not self._winning_number:
                self._winning_number = number
            return True
        return False

    def get_board_score(self) -> int:
        """
        Return the score of this board.

        If the board is not winning, this will return 0.

        Return (int): The sum of all unmarked numbers multiplied by the winning
        number.
        """
        unmarked_sum: int = 0
        for row in self._rows:
            for place in row:
                if not place:
                    unmarked_sum += place.get_number()
        return unmarked_sum * self._winning_number

def string_to_int_list(line) -> list[int]:
    """
    Given a line containing integers, return a list of ints.

    Return list[int]: A list of integers from the string.

    >>> string_to_int_list('22 13 17 11  0')
    [22, 13, 17, 11, 0]
    >>> string_to_int_list('22,13,17,11,0')
    [22, 13, 17, 11, 0]
    """
    line = line.strip()
    if ',' in line:
        return [int(x) for x in line.split(',')]
    else:
        return [int(x) for x in line.split()]

def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
            description='Process called Bingo numbers to find a winning board.')
    parser.add_argument(
            'input',
            type=argparse.FileType('rt'),
            default=sys.stdin,
            help='The called number and Bingo board input.')

    parser.add_argument(
            '-l', '--find_last_winner',
            action='store_true',
            default=False,
            help='Find the score of the last winning board. By '
                 'default the score of the first winning board '
                 'is printed.')
    return parser.parse_args()



def main():
    args = parse_args()

    called_numbers: list[int] = []
    boards: list[Board] = []
    rows: list[list[int]] = []
    for line in args.input:
        if not called_numbers:
            called_numbers = string_to_int_list(line)
            continue

        if not line.strip():
            if rows:
                boards.append(Board(rows))
                rows = []
            continue
        rows.append(string_to_int_list(line))

    # In case there wasn't a final empty new line to create the
    # last board.
    if rows:
        boards.append(Board(rows))

    # Now call the numbers.
    last_winning_score: int = None
    for number in called_numbers:
        for board in boards:
            if board.is_winning():
                continue
            if board.mark_number(number):
                last_winning_score = board.get_board_score()
                if not args.find_last_winner:
                    print(last_winning_score)
                    return 0

    if last_winning_score is not None:
        print(last_winning_score)
        return 0

    # No winning board was found.
    return 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
