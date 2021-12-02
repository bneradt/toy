#!/usr/bin/env bash

script="./process_depth/process_depth.py"
input="input.txt"
fail()
{
    echo $1
    exit 1
}
[ -f "${script}" ] || fail "Could not find: ${script}"
[ -r "${script}" ] || fail "Not readable: ${script}"
[ -r "${input}" ] || fail "Could not read input file: ${input}"

[ `python3 ${script} ${input}` -eq 1713 ] || fail "Expected 1713 with a window of 1"
[ `python3 ${script} -w3 ${input}` -eq 1734 ] || fail "Expected 1734 with a window of 3"

echo "All tests pass."
exit 0
