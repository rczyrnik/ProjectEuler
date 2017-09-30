'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def make_dic():
    product = 1
    my_dic = {0:1}
    for x in range(1, 10):
        product *= x
        my_dic[x] = product
    return my_dic

def sum_digits(num):
    return sum([dic[int(d)] for d in str(num)]) == num


if __name__ == "__main__":
    dic = make_dic()

    # for n in range(10):
    #     print(n, dic[9]*n)
    #go up to 7 digits, 2540160

    numbers = []
    for n in range(3, 2540160):
        if sum_digits(n):
            numbers.append(n)
    print(sum(numbers), numbers)
