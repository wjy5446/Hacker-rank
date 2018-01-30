#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

sum_list = []

for x in range(1, 5):
    for y in range(1, 5):
        n_sum = 0

        n_sum += (sum(arr[y - 1][x-1:x+2]) + sum(arr[y + 1][x-1:x+2]) + arr[y][x])

        sum_list.append(n_sum)

max_sum = max(sum_list)

print(max_sum)
