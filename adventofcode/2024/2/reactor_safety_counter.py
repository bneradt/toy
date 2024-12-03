#!/usr/bin/env python3

from typing import List
import sys

def is_safe(levels: List[int]) -> bool:
    '''Return whether the report is safe.

    :params levels: The levels to analyze.
    :examples:
    
    # Must have at least two values.
    >>> is_safe([])
    False
    >>> is_safe([1])
    False
    
    >>> is_safe([7, 6, 4, 2, 1])
    True
    >>> is_safe([1, 2, 7, 8, 9])
    False
    >>> is_safe([9, 7, 6, 2, 1])
    False
    >>> is_safe([1, 3, 2, 4, 5])
    False
    >>> is_safe([8, 6, 4, 4, 1])
    False
    >>> is_safe([1, 3, 6, 7, 9])
    True
    '''
    if len(levels) < 2:
        return False
    last_level = None
    is_first_comparison = True
    is_increasing = False
    for this_level in levels:
        if last_level is None:
            last_level = this_level
            continue

        if last_level == this_level:
            return False

        if is_first_comparison:
            is_first_comparison = False
            if last_level > this_level:
                is_increasing = False
            else:
                is_increasing = True

        if is_increasing:
            if last_level > this_level:
                return False
            difference = this_level - last_level
        else:
            if last_level < this_level:
                return False
            difference  = last_level - this_level
        
        if difference > 3 or difference < 1:
            return False
        # Last thing: set last_level
        last_level = this_level

    return True

def main() -> int:
    '''Inspect the reports.

    :return: the programs exit code.
    '''
    if len(sys.argv) != 2:
        print('Must provide report file.')
        return 1
    filename = sys.argv[1]
    safe_count = 0
    for line in open(filename, 'r'):
        levels = [int(i) for i in line.strip().split()]
        if is_safe(levels):
            safe_count += 1

    print(safe_count)
    return 0

if __name__ == '__main__':
    sys.exit(main())
