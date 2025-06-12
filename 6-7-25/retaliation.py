import sys

line_count = 0
n = 0

def op_1(array):
    for i in range(len(array)):
        op = array[i] - (i+1)
        if op >= 0:
            array[i] = op
        else:
            return False
    return array

def op_2(array):
    for i in range(len(array)):
        op = array[i] - (n - (i+1) + 1)
        if op >= 0:
            array[i] = op
        else:
            return False
    return array

def check_sum(sums1, sums2, n):
    pairs = []
    for sum_ in sums1:
        if n - sum_ in sums2:
            pairs.append((sum_, n - sum_))
    return pairs

for line in sys.stdin:
    array = [int(i) for i in line.split()]
    #if 165 <= line_count <= 168:
    #        print(array)
    if line_count == 0:
        pass
    elif line_count % 2 == 1:
        n = array[0]
    else:
        #print(line_count)
        min_element = min(array) # find the min
        #print(array)
        if min_element == 1:
            #print('min: 1')
            op1 = op_1(array.copy()) # do op1 once
            op2 = op_2(array.copy()) # do op2 once
            #print(op1)
            #print(op2)
            if (op1 and list(set(op1))[0] == 0 and len(set(op1)) == 1) or (op2 and list(set(op2))[0] == 0 and len(set(op2)) == 1): # check all values 0
                print('yes')
            else:
                print('no')
        else:
            found = False
            num_1 = [index for index, value in enumerate(array) if value == min(array)] # find all indices where the min is (op1 value)
            for n1 in num_1:
                n1 += 1 # adjust for i starting at 1 
                num_2 = n - n1 + 1 # calc result of op2 for min

                #print('min: %d, num1: %d, num2: %d' % (min_element, n1, num_2))
                sums1 = ([i for i in range(n1, min_element +1, n1)]) # array of sums possible from num_1 
                sums2 = ([i for i in range(num_2, min_element +1, num_2)]) # array of sums from num_2
                sums1.append(0) # add 0 for case where op not used
                sums2.append(0) # add 0 for case where op not used
                #print(sums1)
                #print(sums2)
                pairs = check_sum(sums1, sums2, min_element) # check whether any number from sums1 + a number from sums2 == min
                # print(pairs)
                for pair in pairs: # test the operations for the pairs (Slow part)
                    w = array.copy() # working array
                    # print(pair[0] / n1)
                    for x in range(int(pair[0] / n1)): # op1
                        op = op_1(w.copy())
                        if op:
                            w = op
                            #print(w)
                    
                    for x in range(int(pair[1] / num_2)): # op2
                        op = op_2(w.copy())
                        if op:
                            w = op
                            #print(w)
                    
                    if len(set(w)) == 1 and list(set(w))[0] == 0: # check for all values == 0
                        print('yes')
                        break
                else:
                    continue
                break
            else:
                print('no')
    line_count += 1