# Description

This solves the Advent of Code [2021 day
10](https://adventofcode.com/2021/day/10) puzzle.

# Usage

```
$ ./syntax_checker/syntax_checker.py -h
usage: syntax_checker.py [-h] [-a] input_file

Perform syntax checking for the Advent of Code day 10 problem.

positional arguments:
  input_file          The file containing the navigation commands.

optional arguments:
  -h, --help          show this help message and exit
  -a, --autocomplete  Calculate the autocomplete score. By default the syntax error score is completed.
```

For example, to find the syntax error score (the corruption score) of the input
in input.txt, do the following:

```
$ ./syntax_checker/syntax_checker.py input.txt 
358737
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
