# Description

This solves the Advent of Code [2021 day 11](https://adventofcode.com/2021/day/11) puzzle.

# Usage

```
$ ./octopi/octopi.py -h
usage: octopi.py [-h] [-n NUM_STEPS] [-s] input_file

Observe the flashes of a pod of octopi.

positional arguments:
  input_file            The input file describing the octopi pod.

optional arguments:
  -h, --help            show this help message and exit
  -n NUM_STEPS, --num_steps NUM_STEPS
                        The number of steps to observe the pod with.
  -s, --get_synchronized_step_count
                        Find the step at which all the octopi flash at once. Otherwise the flash count at --num_steps is printed.
```

For example, to count the number of steps needed for a pod of octopi
described by input.txt to flash at the same step:

```
$ ./octopi/octopi.py -s input.txt 
324
```

# Tests

The unit tests for this can be run with the
[unittest](https://docs.python.org/3/library/unittest.html) module:

```
$ python3 -m unittest
.......
----------------------------------------------------------------------
Ran 7 tests in 0.008s

OK
```

Both these unit tests and the end to end tests can be run using the provided 
`./test/run_tests.sh` script:

```
$ ./test/run_tests.sh 
.......
----------------------------------------------------------------------
Ran 7 tests in 0.006s

OK
All tests pass
```
