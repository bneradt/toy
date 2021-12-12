#!/bin/bash

script='octopi/octopi.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}
[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} ${example_input}`
[ ${val} -eq 1656 ] || fail "Unexpected number of intersections: ${val}, expected 1656."

val=`${script} -s ${example_input}`
[ ${val} -eq 195 ] || fail "Unexpected number of intersections: ${val}, expected 195."

val=`${script} input.txt`
[ ${val} -eq 1739 ] || fail "Unexpected number of intersections: ${val}, expected 1739."

val=`${script} -s input.txt`
[ ${val} -eq 324 ] || fail "Unexpected number of intersections: ${val}, expected 324."

echo "All tests pass"
exit 0
