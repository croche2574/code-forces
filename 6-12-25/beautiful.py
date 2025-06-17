import sys
from bisect import bisect_left

line_count = 0
k = 0

thresholds = []
last = 0

for x in range(5000):
    ones_sum = sum([1 for bit in bin(x)[2:] if bit == '1'])
    if ones_sum < last:
        thresholds.append(x-1)
    last = ones_sum

for line in sys.stdin:
    array = [int(i) for i in line.split()]
    if line_count == 0:
        pass
    elif line_count % 2 == 1:
        k = array[1]
    else:
        if all(number % 2 == 1 for number in array):
            targets = [thresholds[bisect_left(thresholds, y)] for y in array]
            print(targets)

    line_count += 1