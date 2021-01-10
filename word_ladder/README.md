# word\_ladder

## Description

Create a word ladder given the first and last steps on the ladder and the
number of steps in the ladder (not inclusive of the first step).

For example, given the following:

parameter  | value
---------  | -----
first step | tare
last step: | card
num steps: | 2

A ladder that satisfies these values is:

1. tare
1. care
1. card

## Invocation

```
$ git clone git@github.com:bneradt/toy.git
$ cd toy/word_ladder
$ ./word_ladder --help
usage: word_ladder [-h] [--word-file word_file] first_word last_word num_steps

Create a word ladder given the first and last steps on the ladder and the
number of steps in the ladder (not inclusive of the first step).

For example, given the following:

first step: "tare"
last step:  "card"
num steps:  2

A ladder that satisfies these values is:

    "tare"
    "care"
    "card"

positional arguments:
  first_word            The first word in the ladder.
  last_word             The last word in the ladder.
  num_steps             The number of steps in the ladder (not including first_word).

optional arguments:
  -h, --help            show this help message and exit
  --word-file word_file
                        A file name containing the list of words to use. One word per line. Default: /usr/share/dict/words
```

Here's an example invocation with the associated output:

```
$ ./word_ladder tree card 5
Ladder 0:
  tree
  cree
  crpe
  cape
  care
  card

Ladder 1:
  tree
  tyee
  tyre
  tare
  care
  card
```


## Word List

A file is read for the word list. A file can be provided via the `--word-file`
argument. If one is not provided, `/usr/share/dict/words` is used which is
available on most Linux and MacOS systems.
