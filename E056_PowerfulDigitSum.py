'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

def digit_sum(num):
    my_sum = 0
    for digit in str(num):
        my_sum += int(digit)
    return my_sum

if __name__ == "__main__":
    mds = 0
    for a in range(1, 100):
        for b in range(1, 100):
            temp = digit_sum(a**b)
            if temp > mds: mds = temp
    print(mds)
