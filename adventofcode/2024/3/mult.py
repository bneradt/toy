#!/usr/bin/env python3

import re
import sys

mult_vals_regex = re.compile(r'mul\((\d\d?\d?),(\d\d?\d?)\)')
enabled_regex = re.compiled(r'()')

def get_mult(line:str) -> int:
    '''Scan for all mult commands and return the product.
    :param line: The line to scan.
    :return: The product of the instructions.
    :example:
    >>> get_mult('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')
    161
    '''
    product_sum = 0
    for first, second in mult_vals_regex.findall(line):
        product_sum += int(first) * int(second)
    return product_sum


product_sum = 0
combined = ''
for line in open(sys.argv[1], "r"):
    combined = line.strip()
product_sum += get_mult(line)
print(product_sum)
