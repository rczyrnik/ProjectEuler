'''
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with
denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
'''
import sys


def find_length(denom):
    numer = 1000
    result = ''
    go = True
    while go:
        result += str(int(numer/denom))
        remain = numer%denom

        if len(result) > 4 and result[0] == result[-3] and result[1] == result[-2] and result[2] == result[-1]:
            go = False

        # if len(result) > 90:
        #     go = False
        numer = remain*10
    print(denom)
    print(result)
    return len(result)

if __name__ == "__main__":
    num = int(sys.argv[1])

    with open("E026_Primes.txt") as f:
        data = f.read()
    primes = [int(x) for x in data.split(", ")]

    max_len = 0
    max_num = 0
    for x in primes:
        length = find_length(x)
        if length > max_len:
            max_len = length
            max_num = x
    print(max_num)
