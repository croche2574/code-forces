import sys

line_count = 0
positions = []

for line in sys.stdin:
    array = [int(i) for i in line.split()]
    if line_count == 0:
        pass
    elif line_count % 2 == 1:
        positions = array
    else:
        [n, s] = positions
        if max(array) < s:
            s_max = s
        else:
            s_max = max(array)

        sequence = list(range(1, s_max + 1))
        #print(sequence)
        n = len(sequence)
        if n == 1:
            print(0)
        elif s > max(array):
            print(s-min(array))
        elif s < int(n/2) and int(n/2) % 2 == 0:
            #print('u')
            print(2*(s - 1) + (n - s))
        elif s <= int(n/2) and int(n/2) % 2 == 1:
            #print('u_odd')
            print(2*(s - 1) + (n - s))
        elif int(n/2) % 2 == 0:    
            #print('l')
            print(2*(n-s) + s - 2)
        else:
            #print('l_odd')
            print(2*(n-s) + s -1)

    line_count += 1