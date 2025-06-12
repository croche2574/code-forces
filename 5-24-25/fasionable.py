import sys

inc = 0
num_tests = 0
length = 0
array = []
fashionable = False

for line in sys.stdin:
    if inc == 0:
        num_tests = line
    elif inc % 2 == 1:
        length = line
    else:
        array = list(map(int, line.split()))
        print(array)
        
        fashionable = (min(array) + max(array)) % 2 == 0
        # print(fashionable)
        steps = 0
        while not fashionable:
            even_count = len(list(filter(lambda num: num % 2 == 0, array)))
            odd_count = len(list(filter(lambda num: num % 2 != 0, array)))
            mn = min(array)
            mx = max(array)
            min_even = mn % 2 == 0
            max_even = mx % 2 == 0

            if odd_count > even_count:  # remove the even
                if min_even:
                    array.remove(mn)
                else:
                    array.remove(mx)

            elif even_count > odd_count or odd_count == even_count:  # remove the odd
                if min_even:
                    array.remove(mx)
                else:
                    array.remove(mn)

            # print(array)
            fashionable = (min(array) + max(array)) % 2 == 0
            # print(fashionable)
            steps += 1

        #print(steps)

    inc += 1
    fashionable = False
