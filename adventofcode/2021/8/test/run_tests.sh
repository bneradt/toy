#!/bin/bash

script='display_reader/display_reader.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}

[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} -c ${example_input}`
[ ${val} -eq 26 ] || fail "Unexpected position number: ${val}, expected 26."

val=`${script} ${example_input}`
[ ${val} -eq 61229 ] || fail "Unexpected position number: ${val}, expected 61229."

val=`${script} -c input.txt`
[ ${val} -eq 284 ] || fail "Unexpected position number: ${val}, expected 284."

val=`${script} input.txt`
[ ${val} -eq 973499 ] || fail "Unexpected position number: ${val}, expected 973499."

echo "All tests pass"
exit 0
