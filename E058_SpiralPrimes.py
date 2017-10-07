'''
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both
diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes along
both diagonals first falls below 10%?
'''


import PrimesToX as PTX

if __name__ == "__main__":
    primes_to_alot = PTX.primes_to_x(1000000)
    my_sum = 1
    top_right = 3
    primes = 0
    composites = 0
    for n in range(1, 4):
        for m in range(0, 4):
            if top_right + 2*n*m in primes_to_alot:
                primes += 1
            else:
                composites +=1
            print(n, top_right + 2*n*m)
        if primes/(primes+composites) <= .1:
            print(n)
        top_right += (n)*8 + 2


        # my_sum = 1
        # bottom_left = 3
        # for n in range(3, 1002,2):
        #     #print(n, bottom_left,  my_sum)
        #     my_sum += 4*bottom_left+6*(n-1)
        #     bottom_left = bottom_left + (n-1)*4 + 2
        # print(n, my_sum)

    # print(n, my_sum)on
