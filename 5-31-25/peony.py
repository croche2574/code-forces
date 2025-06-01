import sys
import statistics
import math
import random
import itertools

def get_pair(array, l_i):
    i = (l_i + 1) % len(array)
    for j in range(len(array)):
        if array[i] != array[j]:
            return [i, j]
        
def get_pair_2(array, l_i):
    while True:
        i, j = random.sample(range(len(array)), 2)
        if (array[i] != array[j]) and (i != l_i) and (array[i] != array[l_i]):
            return i, j

def get_pair_3(array, l_i):
    array.sort(reverse=True)
    print(array)
    i = array[0]
    for x in range(1, len(array)):
        if array[x] != i:
            return 0, x

def get_pair_4(array, l_i):
    array.sort(reverse=True)
    print(array)
    return 0, len(array)-1

def get_pair_5(array, l_i):
    array.sort()
    i = len(array)-1
    print(array)
    for j in range(len(array)):
        if math.gcd(array[j], array[i]) != 1 and array[j] != array[i]:
            return i, j
    
    return i, 0

def get_ones(array):
    for i in range(len(array)):
        for j in range(1, len(array)):
            if math.gcd(array[i], array[j]) == 1 and array[i] != array[j]: # return gcd of 1
                return i, j
    
    for i in range(len(array)):
        for j in range(1, len(array)):
            if math.gcd(array[i], array[j]) % 2 != 0 and array[i] != math.gcd(array[i], array[j]): # return the odd gcd without repeating non 1s
                return i, j
    
    return [] # no 1s possible

def get_ones_v2(array):
    pair = []
    run_count = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            run_count += 1
            if math.gcd(array[i], array[j]) == 1 and array[i] != array[j]: # return gcd of 1
                pair = [i, j]
                break
            elif math.gcd(array[i], array[j]) % 2 != 0 and array[i] != math.gcd(array[i], array[j]): # return the odd gcd without repeating non 1s
                if len(pair) == 0: 
                    pair = [i, j]
        else:
            continue
        break
    print('runs: %d' % (run_count))
    return pair
        
def get_pair_v6(array, check_ones):
    array.sort()
    i = len(array)-1
    #print(array)
    if array[0] == 1:
        return i, 0

    elif check_ones:
        ones = get_ones_v2(array)
        #print(ones)
        if len(ones) > 0:
            #print('0: %d, 1: %d' % (ones[0][0], ones[0][1]))
            return ones[1], ones[0]

    for j in range(len(array)): # reduce the array
        if math.gcd(array[j], array[i]) != 1 and array[j] != array[i]:
            return i, j
    
    return i, 0

line_count = 0
for line in sys.stdin:
    if line_count == 0:
        pass
    elif line_count % 2 == 1:
        if int(line) == 1:
            print(0)
    else:
        array = [int(i) for i in line.split()]
        array.sort()
               
        if array[0] != 1:
            check_ones = len(set([item % array[0] for item in array])) > 1 # Check if all values not same gcd
        else:
            check_ones = False

        if len(array) > 1:
            done = len(set(array)) <= 1
            #l_i = 0
            inc = 0
            while not done:
                array.sort()
                #print(array)
                [i, j] = get_pair_v6(array, check_ones)
                gcd = math.gcd(array[i], array[j])
                array[i] = gcd

                #print('i: %d, j: %d, gcd: %d' % (i, j, gcd))
                done = len(set(array)) <= 1
                #print(array)
                inc += 1
            print(inc)
    line_count += 1
