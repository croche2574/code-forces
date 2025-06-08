import sys

line_count = 0
n = 0

def op_1(array):
    for i in array:
        op = array[i] - (i+1)
        if op > array[i]:
            return False
        array[i] -= op
    return array

def op_2(array):
    for i in array:
        op = n - (i+1) + 1
        if op > array[i]:
            return False
        array[i] -= op
    return array

for line in sys.stdin:
    array = [int(i) for i in line.split()]
    if line_count == 0:
        pass
    elif line_count % 2 == 1:
        n = array[0]
    else:
        
    line_count += 1