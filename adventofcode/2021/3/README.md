# Description

This solves the Advent of Code [2021 day 3](https://adventofcode.com/2021/day/3) puzzle.

# Usage

```
$ ./process_diagnostic/process_diagnostic.py -h
usage: process_diagnostic.py [-h] [-l] report

Process the submarine's diagnostic report.

positional arguments:
  report                The submarine's diagnostic report.

optional arguments:
  -h, --help            show this help message and exit
  -l, --get_life_support_rating
                        Get the life support rating from the report. By default, the power consumption rating is calculated.
```

For example, to find the life support rating from the report, do the following:

```
$ ./process_diagnostic/process_diagnostic.py -l input.txt
4550283
```

# Tests

The unit tests for this can be run with the
[unittest](https://docs.python.org/3/library/unittest.html) module:

```
$ python3 -m unittest
..............
----------------------------------------------------------------------
Ran 14 tests in 0.003s

OK
```

Both these unit tests and the end to end tests can be run using the provided 
`./test/run_tests.sh` script:

```
$ ./test/run_tests.sh
..............
----------------------------------------------------------------------
Ran 14 tests in 0.002s

OK
All tests passed.
```
