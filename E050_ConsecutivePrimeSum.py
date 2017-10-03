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

if __name__ == "__main__":

    max_prime = 1000000

    primes = primes_to_x(max_prime)
    # print(len(primes))
    prime_set = {x for x in primes}

    # # starting at 2
    # prime_sum = 5
    # for n in range(2, len(primes)-2, 2):
    #     prime_sum += primes[n]+primes[n+1]
    #     # print("previous sum + {} + {} = {}".format(primes[n], primes[n+1], prime_sum))
    #     if prime_sum in primes:
    #         print(n, prime_sum, " yay")

    # starting at nth prime after 2
    n = 9
    prime_sum = primes[n]
    for n in range(n+1, len(primes)-2, 2):
        prime_sum += primes[n]+primes[n+1]
        # print("previous sum + {} + {} = {}".format(primes[n], primes[n+1], prime_sum))
        if prime_sum in prime_set:
            print(n, prime_sum, " yay")
    print(prime_sum)


    '''
    n = 0   534 958577
    n = 1   524 920291
    n = 2   539 978037
    n = 3   544 997651
    '''
