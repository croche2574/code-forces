import sys

line_count = 0

for line in sys.stdin:
    length = int(line)
    if line_count == 0:
        pass      
    else:
        perm = list(range(2, length+1))
        perm.append(1)
        print(' '.join(map(str, perm)))
    
    line_count += 1
