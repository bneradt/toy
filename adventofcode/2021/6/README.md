# Description

This solves the Advent of Code [2021 day 6](https://adventofcode.com/2021/day/6) puzzle.

# Usage

```
$ ./lanternfish/lanternfish.py -h 
usage: lanternfish.py [-h] input_file

Simulate a school of lanternfish.

positional arguments:
  input_file  The file containing the set of initial timers of the school of lanternfish.

  optional arguments:
    -h, --help  show this help message and exit
```

For example, to count the number of lanternshish in a school from the initial
state described by the file input.txt, do the following:

```
$ ./lanternfish/lanternfish.py input.txt 
355386
```

# Tests

The unit tests for this can be run with the
[unittest](https://docs.python.org/3/library/unittest.html) module:

```
$ python3 -m unittest
...
----------------------------------------------------------------------
Ran 3 tests in 0.029s

OK
```

Both these unit tests and the end to end tests can be run using the provided 
`./test/run_tests.sh` script:

```
$ ./test/run_tests.sh 
...
----------------------------------------------------------------------
Ran 3 tests in 0.033s

OK
All tests pass
```
