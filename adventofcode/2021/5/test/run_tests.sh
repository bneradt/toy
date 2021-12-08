#!/bin/bash

script='intersect/intersect.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}
[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} ${example_input}`
[ ${val} -eq 5 ] || fail "Unexpected number of intersections: ${val}, expected 5."

val=`${script} -d ${example_input}`
[ ${val} -eq 12 ] || fail "Unexpected number of intersections: ${val}, expected 12."

val=`${script} input.txt`
[ ${val} -eq 4728 ] || fail "Unexpected number of intersections: ${val}, expected 4728."

val=`${script} -d input.txt`
[ ${val} -eq 17717 ] || fail "Unexpected number of intersections: ${val}, expected 17717."

echo "All tests pass"
exit 0
