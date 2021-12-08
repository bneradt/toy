# Description

This solves the Advent of Code [2021 day 5](https://adventofcode.com/2021/day/5) puzzle.

# Usage

```
$ ./intersect/intersect.py -h
usage: intersect.py [-h] [-d] segments_file

Find the intersection of lines.

positional arguments:
  segments_file         A file with a set of segment descriptions.

optional arguments:
  -h, --help            show this help message and exit
  -d, --count_diagonal  Count diagonal intersections as well.
```

For example, to count the number of vertical and horizontal intersections in a
file of segments described by input.txt, do the following:

```
$ ./intersect/intersect.py input.txt
4728
```

# Tests

The unit tests for this can be run with the
[unittest](https://docs.python.org/3/library/unittest.html) module:

```
$ python3 -m unittest
...............
----------------------------------------------------------------------
Ran 15 tests in 0.001s

OK
```

Both these unit tests and the end to end tests can be run using the provided 
`./test/run_tests.sh` script:

```
$ ./test/run_tests.sh
...............
----------------------------------------------------------------------
Ran 15 tests in 0.001s

OK
All tests pass
```
