'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

import sys

def check_pwrs(pwr, num):
    right = 0
    for char in list(str(num)):
        right += my_dic[char]
    left = num
    return left == right

if __name__ == "__main__":
    pwr = int(sys.argv[1])

    my_dic = {}
    for x in range(10):
        my_dic[str(x)] = x**pwr
    print(my_dic)


    ans = []
    for x in range(10, 10000000):
        if check_pwrs(my_dic, x): ans.append(x)

    print(ans)
    print(sum(ans))
