#!/bin/bash

script='syntax_checker/syntax_checker.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}
[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} ${example_input}`
[ ${val} -eq 26397 ] || fail "Unexpected syntax error score: ${val}, expected 26397."

val=`${script} --autocomplete ${example_input}`
[ ${val} -eq 288957 ] || fail "Unexpected autocomplete score: ${val}, expected 288957."

val=`${script} input.txt`
[ ${val} -eq 358737 ] || fail "Unexpected syntax error score: ${val}, expected 358737."

val=`${script} -a input.txt`
[ ${val} -eq 4329504793 ] || fail "Unexpected autocomplete score: ${val}, expected 4329504793."

echo "All tests pass"
exit 0
