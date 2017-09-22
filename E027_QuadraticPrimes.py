'''
Euler discovered the remarkable quadratic formula:

n2+n+41n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer
values 0≤n≤390≤n≤39. However, when n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41
is divisible by 41, and certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601n2−79n+1601 was discovered,
which produces 80 primes for the consecutive values 0≤n≤790≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+bn2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

where |n||n| is the modulus/absolute value of nn
e.g. |11|=11|11|=11 and |−4|=4|−4|=4
Find the product of the coefficients, aa and bb, for the quadratic expression
that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.
'''

def find_max_prime(a, b):
    for n in range(0, 10000):
        if n**2 + a*n + b not in primes:
            return n
    return n

if __name__ == "__main__":
    with open("PrimesToTenThousand.txt") as f:
        data = f.read()
    primes = {int(x) for x in data.split()}


    with open("PrimesToThousand.txt") as f:
        data = f.read()

    primes1000 = {int(x) for x in data.split(',')}

    b_range = {-x for x in primes1000}

    b_range.update(primes1000)

    max_of_maxes = 0
    max_a = 0
    max_b = 0

    for a in range(-1000, 1000):
        for b in b_range:
            temp_max = find_max_prime(a, b)
            # print(a, b, temp_max)
            if temp_max > max_of_maxes:
                max_of_maxes = temp_max
                max_a = a
                max_b = b
    print(max_a, max_b, max_a*max_b)
