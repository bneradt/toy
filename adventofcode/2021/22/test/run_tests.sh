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

val=`${script} --side_size 101 ${example_input}`
[ ${val} -eq 590784 ] || fail "Unexpected number of intersections: ${val}, expected 590784."

val=`${script} --side_size 101 input.txt`
[ ${val} -eq 615869 ] || fail "Unexpected number of intersections: ${val}, expected 615869."

echo "All tests pass"
exit 0
