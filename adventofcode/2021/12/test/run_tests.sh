#!/bin/bash

script='best_path/best_path.py'
example_input1='test/example_input1.txt'
example_input2='test/example_input2.txt'
example_input3='test/example_input3.txt'

fail()
{
    echo $1
    exit 1
}
[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} ${example_input1}`
[ ${val} -eq 10 ] || fail "Unexpected syntax error score: ${val}, expected 10."

val=`${script} ${example_input2}`
[ ${val} -eq 19 ] || fail "Unexpected syntax error score: ${val}, expected 19."

val=`${script} ${example_input3}`
[ ${val} -eq 226 ] || fail "Unexpected syntax error score: ${val}, expected 226."

val=`${script} input.txt`
[ ${val} -eq 3887 ] || fail "Unexpected syntax error score: ${val}, expected 3887."

echo "All tests pass"
exit 0
