'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

def last_three(base, exp):
    product = 1
    for x in range(1, exp+1):
        product *= base
        product = product % 1000
    return product

def last_ten(base, exp):
    product = 1
    for x in range(1, exp+1):
        product *= base
        product = product % 10**10
    return product

if __name__ == "__main__":

    my_sum = 0
    for n in range(1, 1001):
        my_sum += last_ten(n, n)
        my_sum = my_sum % 10**10
    print(my_sum)
