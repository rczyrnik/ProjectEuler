'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

def is_pandigital(my_num, my_str):
    for x in my_str:
        if x not in my_num: return False
    return True

if __name__ == "__main__":
    numbers = [ ['1'],
                ['1','2'],
                ['1','2','3'],
                ['1','2','3','4'],
                ['1','2','3','4','5'],
                ['1','2','3','4','5','6'],
                ['1','2','3','4','5','6','7'],
                ['1','2','3','4','5','6','7','8'],
                ['1','2','3','4','5','6','7','8','9'] ]

    with open("PrimesToTenMillion.txt") as f:
        data = f.read()
        # primes = {int(x) for x in data.split()}
    # with open("PrimesToOneMillion.txt") as f:
    #     data = f.read()
    # primes = [x.strip('\n') for x in data.split(',')]

    # with open("PrimesToTenThousand.txt") as f:
    #     data = f.read()
    # primes = [int(x) for x in data.split()]

        for x in data.split():
            if is_pandigital(x, numbers[len(x)-1]):
                print(x)
