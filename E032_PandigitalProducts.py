'''

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

import itertools

if __name__ == "__main__":
    length = 9
    my_string = "123456789"
    my_permutations = [x for x in itertools.permutations(my_string, length)]
    ans = {}
    for p in range(len(my_permutations)):
        ex = [int(x) for x in my_permutations[p]]
        if (ex[0]) * (1000*ex[1]+100*ex[2]+10*ex[3]+ex[4]) == 1000*ex[5]+100*ex[6]+10*ex[7]+ex[8]:
            ans[1000*ex[5]+100*ex[6]+10*ex[7]+ex[8]] = "1, 4, 4"
        if (10*ex[0]+ex[1]) * (100*ex[2]+10*ex[3]+ex[4]) == 1000*ex[5]+100*ex[6]+10*ex[7]+ex[8]:
            ans[1000*ex[5]+100*ex[6]+10*ex[7]+ex[8]] = "2, 3, 4"
    print(sum(list(ans.keys())))
