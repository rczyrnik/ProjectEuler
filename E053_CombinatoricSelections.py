'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100,
are greater than one-million?
'''


def C(n,r):
    return f_dic[n] / (f_dic[r]*f_dic[n-r])

def num_ge_mill(n):
    for r in range(0, n+1):
        if C(n,r) >= 1000000:
            return n+1-2*r
    return 0

if __name__=="__main__":
    # print(factorial(6))

    f_dic = {0:1}
    product = 1
    for n in range(1, 101):
        product *= n
        f_dic[n] = product
    # print(f_dic)

    n = 22
    my_sum = 0
    for n in range(23, 101):
        my_sum += num_ge_mill(n)
    print(my_sum)
    # for r in range(0, n+1):
    #     print(n, r, C(n, r))
