#!/bin/bash

fail()
{
    echo $1
    exit 1
}

python3 -m unittest || fail "Unit tests failed."

# First, test the old, wrong way to follow the directions.
val=`./process_course/process_course.py -w "test/test_input/example_input.txt"`
[ $val -eq 150 ] || fail "Expected 150 from sample input, got: $val"

# Now, test the new, correct way.
val=`./process_course/process_course.py "test/test_input/example_input.txt"`
[ $val -eq 900 ] || fail "Expected 900 from sample input, got: $val"

# Verify with the contest's input.
val=`./process_course/process_course.py -w "input.txt"`
[ $val -eq 1499229 ] || fail "Expected 1499229 from sample input, got: $val"

val=`./process_course/process_course.py "input.txt"`
[ $val -eq 1340836560 ] || fail "Expected 1340836560 from sample input, got: $val"

echo "All tests passed."
exit 0
