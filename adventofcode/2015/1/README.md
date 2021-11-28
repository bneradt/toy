# Description

This computes solutions for the following Advent of Code puzzle:
https://adventofcode.com/2015/day/1

# Usage

Provide the floor description to get the final floor Santa winds up at:
```
$ python3 ./which_floor/which_floor.py '(()('
2
```

Using the -b option results in finding which position in the description puts
Santa in the basement first.
```
$ python3 ./which_floor/which_floor.py -b '()())'
5
```


# Run the tests

The unit tests are written using the [unittest](https://docs.python.org/3/library/unittest.html) Python module.

```
$ python3 -m unittest
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
