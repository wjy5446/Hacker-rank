#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr = arr[::-1]

out = ""

for i in arr:
    out += str(i)
    out += " "

print(out)
