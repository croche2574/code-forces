import sys

line_count = 0
length = 0

for line in sys.stdin:
    array = [int(i) for i in line.split()]
    if line_count == 0:
        pass
    elif line_count % 2 == 1:
        length = array[0]
    else:
        count = 1
        while len(array) > 1:
            for i in range(length):
                front = set(array[:i])
                back = set(array[i:])
                #print(front)
                #print(back)
                if not front.issubset(back):
                    array = array[:i-1]
                    #print(array)
                    count += 1
                    if len(array) == 1:
                        count += 1
                    break
        print (count-1)
    line_count += 1