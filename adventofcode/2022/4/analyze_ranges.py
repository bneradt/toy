#!/usr/bin/env python3

from datetime import datetime
import sys

subset_count = 0
overlap_count = 0

time_start = datetime.now()
for line in open(sys.argv[1]):
    first_dash = line.find('-')
    first_comma = line.find(',')
    first_start = int(line[:first_dash])
    first_end = int(line[first_dash+1:first_comma])

    second_dash = line.find('-', first_comma)
    second_comma = line.find(',', first_comma+1)
    second_start = int(line[first_comma+1:second_dash])
    second_end = int(line[second_dash+1:second_comma])

    if first_start <= second_start and first_end >= second_end:
        subset_count += 1
    elif second_start <= first_start and second_end >= first_end:
        subset_count += 1
    if second_start <= first_end and second_end >= first_start:
        overlap_count += 1

time_end = datetime.now()

print(f'Subset count: {subset_count}')
print(f'Overlap count: {overlap_count}')
print(f'Time: {time_end - time_start}')
