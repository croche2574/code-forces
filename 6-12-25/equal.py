import sys

line_count = 0

for line in sys.stdin:
    array = [int(i) for i in line.split()]
    if line_count == 0:
        pass        
    else:
        n = array[0]
        k = array[1]
        zeroes = n - k
        perfect = [1 for i in range(k)]
        for x in range(zeroes):
            perfect.append(0)
        print(''.join(map(str, perfect)))

    line_count += 1