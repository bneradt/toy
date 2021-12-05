#!/bin/bash

script='bingo/bingo.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}
[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."
val=`${script} ${example_input}`
[ ${val} -eq 4512 ] || fail "Unexpected board scrore: ${val}, expected 4512."


val=`${script} input.txt`
[ ${val} -eq 49860 ] || fail "Unexpected board score: ${val}, expected 49860."

echo "All tests pass"
exit 0
