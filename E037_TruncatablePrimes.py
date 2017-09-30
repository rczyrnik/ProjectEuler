'''
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are
both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def left_to_right(num):
    length = len(num)
    for x in range(1, length):
        if num[x:] not in primes:
            return False
    return True

def right_to_left(num):
    length = len(num)
    for x in range(1, length):
        if num[0:-x] not in primes:
            return False
    return True


if __name__ == "__main__":
    with open("PrimesToOneMillion.txt") as f:
        data = f.read()
    primes = [x.strip('\n') for x in data.split(',')]

    primes1379 = []
    bad_nums = '024568'
    good_nums = '379'
    for x in primes:
        if not any(num in x[1:] for num in bad_nums):
            primes1379.append(x)
    my_sum = 0
    for p in primes1379:
        if left_to_right(p) and right_to_left(p):
            print(p)
            if int(p) >10: my_sum+=int(p)
    print(my_sum)

    # print('3137' in primes)
    # print(primes379)
