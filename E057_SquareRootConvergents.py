'''
It is possible to show that the square root of two can be expressed as
an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator exceeds the
number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?

'''

from fractions import Fraction
import math
import sys

sys.setrecursionlimit(1009)

def frac_sum(position):
    if position == len(two_list)-1:
        return Fraction(1, 2)
    else:
        return Fraction(1, 2+frac_sum(position+1))


if __name__ == "__main__":

    a = Fraction(1,1)
    b = Fraction(1,2)
    count = 0
    # print(1, a+b)
    for n in range(2, 1001):
        b = 1 / (2+b)

        f = a+b
        # print(int(math.log(f.numerator,10)),int(math.log(f.denominator, 10)))

        if int(math.log(f.numerator,10)) != int(math.log(f.denominator, 10)):
            count += 1
            print(n, a+b)

    print(count)
