#!/usr/bin/env python3
"""Perform syntax checking for the Advent of Code day 10 problem."""

import argparse
import sys
from typing import List


class LineChecker:
    """Perform syntax checking on a navigation line."""

    _line: str
    _first_illegal_character: str
    _unclosed_characters: List[str]

    _pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }

    _illegal_character_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def __init__(self, line: str):
        """Initialize the checker with the given line.

        :param line: The line to perform syntax checking upon.

        """
        self._line = line.strip()
        self._first_illegal_character = ''
        self._unclosed_characters = []
        self._syntax_error_score = 0
        self._process_line()

    def is_incomplete(self) -> bool:
        """Return whether the line has unclosed characters.

        :examples:
            >>> l = LineChecker('{()}')
            >>> l.is_incomplete()
            False

            >>> l = LineChecker('{([(<{}[<>[]}>{[]{[(<()>')
            >>> l.is_incomplete()
            False

            # An incomplete line.
            >>> l = LineChecker('[({(<(())[]>[[{[]{<()<>>')
            >>> l.is_incomplete()
            True

        """
        return (self._first_illegal_character == '' and
                len(self._unclosed_characters) > 0)

    def is_corrupted(self) -> bool:
        """Return whether the line is corrupted.

        :examples:
            >>> l = LineChecker('{()}')
            >>> l.is_corrupted()
            False

            >>> l = LineChecker('{([(<{}[<>[]}>{[]{[(<()>')
            >>> l.is_corrupted()
            True

            # An incomplete line.
            >>> l = LineChecker('[({(<(())[]>[[{[]{<()<>>')
            >>> l.is_corrupted()
            False

        """
        return self._first_illegal_character != ''

    def get_unclosed_characters(self) -> List[str]:
        """Return the list of unclosed characters in the line.

        If the line is corrupted, then this returns an empty list.

        :examples:
            >>> l = LineChecker('{()}')
            >>> l.get_unclosed_characters()
            []

            >>> l = LineChecker('{([(<{}[<>[]}>{[]{[(<()>')
            >>> l.get_unclosed_characters()
            []

            >>> l = LineChecker('[({([[{{')
            >>> l.get_unclosed_characters()
            ['[', '(', '{', '(', '[', '[', '{', '{']
        """
        if self._first_illegal_character != '':
            return []
        return self._unclosed_characters

    def _process_line(self) -> None:
        """Process the line for syntax issues."""
        for character in self._line:
            if character in LineChecker._pairs:
                self._unclosed_characters.append(character)
            elif character not in LineChecker._pairs.values():
                raise ValueError(f"Unexpected character in input: {character}")
            else:
                last_opening_character = self._unclosed_characters.pop()
                expected_closing_character = \
                    LineChecker._pairs[last_opening_character]
                if character != expected_closing_character:
                    self._first_illegal_character = character
                    break
        if self._first_illegal_character != '':
            self._syntax_error_score = \
                LineChecker._illegal_character_score[
                    self._first_illegal_character]

    def get_first_illegal_character(self) -> str:
        """Find the first corrupted character in the line.

        A corrupted character is a closing character which doesn't match the
        corresponding opening character.

        :expamples:
            >>> l = LineChecker('{()}')
            >>> l.get_first_illegal_character()
            ''
            >>> l.get_first_illegal_character()
            ''

            >>> l = LineChecker('{([(<{}[<>[]}>{[]{[(<()>')
            >>> l.get_first_illegal_character()
            '}'
            >>> l.get_first_illegal_character()
            '}'

            >>> l = LineChecker('[<[([]))<([[{}[[()]]]')
            >>> l.get_first_illegal_character()
            ')'

            >>> l = LineChecker('[{[{({}]{}}([{[{{{}}([]')
            >>> l.get_first_illegal_character()
            ']'

            >>> l = LineChecker('<{([([[(<>()){}]>(<<{{')
            >>> l.get_first_illegal_character()
            '>'

            # An incomplete line.
            >>> l = LineChecker('[({(<(())[]>[[{[]{<()<>>')
            >>> l.get_first_illegal_character()
            ''

        """
        return self._first_illegal_character

    def get_syntax_error_score(self) -> int:
        """Find the syntax score for any errors in the line.

        :examples:
            >>> l = LineChecker('{()}')
            >>> l.get_syntax_error_score()
            0

            >>> l = LineChecker('{([(<{}[<>[]}>{[]{[(<()>')
            >>> l.get_syntax_error_score()
            1197

            >>> l = LineChecker('[<[([]))<([[{}[[()]]]')
            >>> l.get_syntax_error_score()
            3

            >>> l = LineChecker('[{[{({}]{}}([{[{{{}}([]')
            >>> l.get_syntax_error_score()
            57

            >>> l = LineChecker('<{([([[(<>()){}]>(<<{{')
            >>> l.get_syntax_error_score()
            25137

            # An incomplete line.
            >>> l = LineChecker('[({(<(())[]>[[{[]{<()<>>')
            >>> l.get_syntax_error_score()
            0

        """
        return self._syntax_error_score


def parse_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=argparse.FileType('rt'),
        default=sys.stdin,
        help='The file containing the navigation commands.')
    return parser.parse_args()


def main():
    """Begin the script's logic."""
    args = parse_args()
    syntax_error_score = 0
    for line in args.input_file:
        line_checker = LineChecker(line)
        syntax_error_score += line_checker.get_syntax_error_score()
    print(syntax_error_score)
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
