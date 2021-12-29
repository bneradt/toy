#!/bin/bash

script='lanternfish/lanternfish.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}
[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} ${example_input}`
[ ${val} -eq 5934 ] || fail "Unexpected number of fish: ${val}, expected 5934."

val=`${script} --num_days 256 ${example_input}`
[ ${val} -eq 26984457539 ] || fail "Unexpected number of fish: ${val}, expected 26984457539."

val=`${script} input.txt`
[ ${val} -eq 355386 ] || fail "Unexpected number of fish: ${val}, expected 355386."

val=`${script} --num_days 256 input.txt`
[ ${val} -eq 1613415325809 ] || fail "Unexpected number of fish: ${val}, expected 1613415325809."

echo "All tests pass"
exit 0
