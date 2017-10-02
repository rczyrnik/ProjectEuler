'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''


def primes_to_x(x):
    p =[]
    with open("PrimesToTenMillion.txt") as f:
        data = f.read()
        for n in data.split():
            if int(n) > x:
                return p
            p.append(int(n))
    return False

def check_for_prime(my_dic):
    for key, value in my_dic.items():
        if value in primes:
            return value
    return False

if __name__ == "__main__":

    primes = primes_to_x(1000000)

    d = {}
    for p in primes:
        d[p] = p


    for c in range(1, 2000):                     # adding c primes
        for n in range(0, 100):                 # cycle through first 100 primes
            d[primes[n]] += primes[n+c]         # add cth prime after nth prime

        if not check_for_prime(d):
            print(c+1)
            print()


    #
    # for c in range(0, 6):
    #
    # d = {}
    # for n in range(0, len(primes)-c):
    #     d[primes[n]] = primes[n]
    #     s = 0
    #     for x in range(1, c):
    #         d[primes[n]] += primes[n+x]
    #     if d[primes[n]] in primes:
    #         print(primes[n], d[primes[n]])

    # d = {}
    #
    # for n in range(0, len(primes1)):
    #
    # for p in primes1:
    #     d[p] =
