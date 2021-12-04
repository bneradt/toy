#!/bin/bash

script='./process_diagnostic/process_diagnostic.py' 

fail()
{
    echo $1
    exit 1
}

python3 -m unittest || fail "Unit tests failed."

val=`${script} 'test/test_input/example_input_a.txt'`
[ ${val} -eq 198 ] || fail "Unexpected part a power consuption. Expected 198, got ${val}."

val=`${script} -l 'test/test_input/example_input_a.txt'`
[ ${val} -eq 230 ] || fail "Unexpected part a power consuption. Expected 230, got ${val}."

# Verify the contest input.
val=`${script} 'input.txt'`
[ ${val} -eq 3633500 ] || fail "Unexpected part a power consuption. Expected 3633500, got ${val}."

val=`${script} -l 'input.txt'`
[ ${val} -eq 4550283 ] || fail "Unexpected part a power consuption. Expected 4550283, got ${val}."


echo "All tests passed."
exit 0
