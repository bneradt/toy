# Description

This solves the Advent of Code [2021 day
12](https://adventofcode.com/2021/day/12) puzzle. Currently it just solves part
1 of the puzzle.

# Usage

```
$ ./best_path/best_path.py --help
usage: best_path.py [-h] input_file

Process the various paths in a cave system.

Paths are described in a file that looks like this:

start-A
start-b
A-c
A-b
b-d
A-end
b-end

Which corresponds to a cave system represented like this:

    start
    /   \
c--A-----b--d
    \   /
     end

positional arguments:
  input_file  The file containing the description of the cave network.

optional arguments:
  -h, --help  show this help message and exit
```

For example, to count the number of paths from start to end of the cave network
described in input.txt, run the script like so:

```
$ ./best_path/best_path.py input.txt 
3887
```

# Tests

The unit tests for this can be run with the
[unittest](https://docs.python.org/3/library/unittest.html) module:

```
$ python3 -m unittest
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Both these unit tests and the end to end tests can be run using the provided 
`./test/run_tests.sh` script:

```
$ ./test/run_tests.sh 
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
All tests pass
```
