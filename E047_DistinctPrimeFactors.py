'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
'''
from collections import defaultdict

def find_factors(num, factors):
    for x in range(2, 10000):
        if num%x == 0:
            factors[x] += 1
            return find_factors(num//x, factors)

def return_factors(num):
    factors = defaultdict(int)
    find_factors(num, factors)
    return set(factors.items())



if __name__ == "__main__":
    magic_num = 4

    my_dic = {2: return_factors(2), 3: return_factors(3), 4: return_factors(4)}

    for n in range(5, 1000000):
        my_dic[n] = return_factors(n)

        a = my_dic[n-3]
        b = my_dic[n-2]
        c = my_dic[n-1]
        d = my_dic[n]
        if len(a)==len(b)==len(c)==len(d)==magic_num and not a&b and not a&c and not a&d and not b&c and not b&d and not c&d:
            print(n-3)
