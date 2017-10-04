'''
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

MY NOTES:
has to include 1 (and smallest starts with 1. otherwise 6*2 = 12
different numbers? we don't know. assume repeats okay
'''
import itertools

def check_permutes(num_as_string):
    permutations = itertools.permutations(num_as_string, len(num_as_string))
    return {int(''.join(x)) for x in permutations}

def check_multiples(num):
    for m in range(2, 7):
        if sorted(str(num)) != sorted(str(num*m)):
            return False
    return True

if __name__ == "__main__":
    # check_permutes('1234')

    # print(check_multiples(14, {14, 11}))

    # length = 6
    # range_min = 10**(length-1)
    # for x in range(range_min, 2 * range_min):
    #     if check_multiples(x):
    #         print(x)

    p = 142857
    for n in range(1, 7):
        print("{} x {} = {}".format(n, p, n*p))
