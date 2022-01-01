# Description

This solves the Advent of Code [2021 day
9](https://adventofcode.com/2021/day/9) puzzle. Currently only part 1 is
solved.

# Usage

```
usage: parse_heightmap.py [-h] input_file

Implements heightmap parsing functionality.

positional arguments:
  input_file  The file containing the desciption of the heightmap.

optional arguments:
  -h, --help  show this help message and exit

```

For example, to find the risk factor of the given heightmap in input.txt (part
1 of the puzzle):

```
$ ./heightmap/parse_heightmap.py input.txt 
444
```

# Tests


Both these unit tests and the end to end tests can be run using the provided 
`./test/run_tests.sh` script:

```
$ ./test/run_tests.sh 
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
All tests pass
```
