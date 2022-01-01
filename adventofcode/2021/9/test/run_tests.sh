#!/bin/bash

script='heightmap/parse_heightmap.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}

[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} ${example_input}`
[ ${val} -eq 15 ] || fail "Unexpected position number: ${val}, expected 15."

val=`${script} input.txt`
[ ${val} -eq 444 ] || fail "Unexpected position number: ${val}, expected 444."

echo "All tests pass"
exit 0
