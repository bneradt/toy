# Description

This solves the Advent of Code [2021 day 7](https://adventofcode.com/2021/day/7) puzzle.

# Usage

```
$ ./save_fuel/save_fuel.py -h
usage: save_fuel.py [-h] [-c] input_file

Calculate the position of least fuel cost. Given a set of crab positions, calculate the position of least possible cost to which all the crabs can unite.

positional arguments:
  input_file            The input file containing the initial swarm position.

optional arguments:
  -h, --help            show this help message and exit
  -c, --use_compounding_costs
                        Use the compounding crab costs for crab movement.
```

For example, to calulate the cost of the most efficient position for the crabs
to go to with their initial positions described in input.txt:

```
$ ./save_fuel/save_fuel.py input.txt 
342641
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
Ran 2 tests in 0.000s

OK
All tests pass

```
