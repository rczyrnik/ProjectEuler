'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
'''
from collections import defaultdict

if __name__ == "__main__":
    with open("PrimesFourDigits.txt") as f:
        data = f.read()
    # primes = {int(x) for x in data.split()}
    # print(primes)


    my_dic = defaultdict(list)
    for x in data.split():
        sort = ''.join(sorted(x))
        my_dic[sort].append(x)
    # print(my_dic)
    which = 1
    for key, value in my_dic.items():
        if len(value)>which+1 and str(int(value[which]) + 3330) in value and str(int(value[which]) + 6660) in value:
            # and int(value[2])-int(value[1]) == int(value[1])-int(value[0]):
            print(str(int(value[which])) + str(int(value[which]) + 3330) + str(int(value[which]) + 6660))
