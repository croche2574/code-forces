import sys

line_count = 0
num_doors = 0
num_seconds = 0

for line in sys.stdin:
    array = [int(i) for i in line.split()]
    if line_count == 0:
        pass
    elif line_count % 2 == 1:
        #print(array)
        [num_doors, num_seconds] = array
    else:
        #print('doors: %d, sec: %d' % (num_doors, num_seconds))
        #print(array)
        first = array.index(1)
        last = len(array) - 1 - array[::-1].index(1)
        #print('first: %d, last: %d' % (first, last))
        delta = abs(last - first)
        if delta < num_seconds:
            print("yes")
        else:
            print("no")
    
    line_count += 1