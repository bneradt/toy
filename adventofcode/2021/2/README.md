# Description

This solves the Advent of Code [2021 day 2](https://adventofcode.com/2021/day/2) puzzle.

# Usage

```
$ ./process_course/process_course.py -h
usage: process_course.py [-h] [-w] course

Process the planned submarine course.

positional arguments:
  course                The submarine course instructions.

optional arguments:
  -h, --help            show this help message and exit
  -w, --wrong_instructions
                        Use this to follow the old, wrong instructions.
```

For example, follow the provided course described in input.txt, do the
following:

```
$ ./process_course/process_course.py input.txt
1340836560
```

# Tests

The unit tests for this can be run with the
[unittest](https://docs.python.org/3/library/unittest.html) module:

```
$ python3 -m unittest
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```

Both these unit tests and the end to end tests can be run using the provided 
`./test/run_tests.sh` script:

```
$ ./test/run_tests.sh
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
All tests passed.
```
