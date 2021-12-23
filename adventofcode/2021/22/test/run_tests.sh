#!/bin/bash

script='reactor/reactor.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}
[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} ${example_input}`
[ ${val} -eq 590784 ] || fail "Unexpected number of intersections: ${val}, expected 590784."

echo "All tests pass"
exit 0
