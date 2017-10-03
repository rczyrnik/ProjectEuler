'''
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among
the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.

MY THOUGHTS
won't change the last digit
could change any number of digits

'''
# from PrimesToX import primes_to_x
import PrimesToX as PTX
import itertools

def generate_numbers(length):
    first_digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '*'}
    middle_digits = '0123456789*'
    last_digits = {'1', '3', '7', '9'}
    numbers = []
    for f in first_digits:
        for m in [''.join(x) for x in itertools.product(  middle_digits, repeat = length-2)]:
            for l in last_digits:
                number = f+m+l
                if '*' in number:
                    numbers.append(f+m+l)
    return numbers

def replace_stars(star_string):
    for n in range(0, 10):
        print(star_string.replace('*', str(n)))


if __name__ == "__main__":
    primes = PTX.primes_to_x(1000000)
    # print(primes)

    # for string in generate_numbers(6):
    #     hits = 0
    #     if string[0] == "*":
    #         for n in range(1, 10):
    #             if int(string.replace('*', str(n))) in primes:
    #                 hits += 1
    #     else:
    #         for n in range(0, 10):
    #             if int(string.replace('*', str(n))) in primes:
    #                 hits += 1
    #     if hits >= 8:
    #         print(string, hits)

    string = '*2*3*3'
    for n in range(0, 10):
        new_num = int(string.replace('*', str(n)))
        if new_num in primes:
            print(new_num)
