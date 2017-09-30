'''
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
'''

def find_goldbach(num):
    for x in squares[0:num]:
        if num - 2*x in primes[0:num]:
            return True
    return False

if __name__ == "__main__":
    with open("PrimesToTenThousand.txt") as f:
        data = f.read()
    primes = [int(x) for x in data.split()]

    squares = [x**2 for x in range(1, 100)]



    for n in range(3, 400000, 2):
        if n not in primes:
            if not find_goldbach(n):
                print(n)
