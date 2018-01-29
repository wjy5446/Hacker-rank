# Task
# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.
#
# Input Format
#
# A single integer, .
#
# Output Format
#
# Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

#!/bin/python3

import sys

max_num_one = 0
cur_num_one = 0

n = int(input().strip())

while n > 0:
    if n % 2 == 1:
        cur_num_one += 1
    else:
        cur_num_one = 0

    if(max_num_one < cur_num_one):
            max_num_one = cur_num_one

    n = n // 2

print(max_num_one)
