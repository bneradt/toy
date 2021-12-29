#!/bin/bash

script='save_fuel/save_fuel.py'
example_input='test/example_input.txt'

fail()
{
    echo $1
    exit 1
}
[ -r "${script}" ] || fail "Could not find: ${script}"
python3 -m unittest || fail "Unit tests failed."

val=`${script} ${example_input}`
[ ${val} -eq 37 ] || fail "Unexpected position number: ${val}, expected 37."

val=`${script} --use_compounding_costs ${example_input}`
[ ${val} -eq 168 ] || fail "Unexpected position number: ${val}, expected 168."

val=`${script} input.txt`
[ ${val} -eq 342641 ] || fail "Unexpected position number: ${val}, expected 342641."

val=`${script} --use_compounding_costs input.txt`
[ ${val} -eq 93006301 ] || fail "Unexpected position number: ${val}, expected 93006301."

echo "All tests pass"
exit 0
