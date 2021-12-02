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

The unit tests for this can be run like so:

```
$ python3 -m unittest
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
```
