# Description

This solves the Advent of Code [2021 day 4](https://adventofcode.com/2021/day/4) puzzle (just part 1 so far).

# Usage

```
$ ./bingo/bingo.py 
usage: bingo.py [-h] input
bingo.py: error: the following arguments are required: input

```

For example, to get the winning board score from input.txt:

```
$ ./bingo/bingo.py input.txt 
49860
```

# Tests

The unit tests for this can be run with the
[unittest](https://docs.python.org/3/library/unittest.html) module:

```
$ python3 -m unittest
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Both these unit tests and the end to end tests can be run using the provided 
`./test/run_tests.sh` script:

```
$ ./test/run_tests.sh 
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
All tests pass
```
