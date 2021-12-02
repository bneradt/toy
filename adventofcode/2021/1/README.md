# Description

This solves the Advent of Code [2021 day 1](https://adventofcode.com/2021/day/1) puzzle.

# Usage

```
$ ./process_depth/process_depth.py -h
usage: process_depth.py [-h] [-w WINDOW_SIZE] depth_report_file

Process a set of depth measurements.

positional arguments:
  depth_report_file     The input file containing the depth measurements.

optional arguments:
  -h, --help            show this help message and exit
  -w WINDOW_SIZE, --window_size WINDOW_SIZE
                        Using a sliding window of the given size to count depth increases.
```

# Tests

The unit tests for this can be run with the unittest module:

```
$ python3 -m unittest
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
```

The end to end tests can be run with the `tests/end_to_end.sh` script:

```
$ bash test/end_to_end.sh
All tests pass.
```
