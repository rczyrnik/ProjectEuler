'''
A number chain is created by continuously adding the square of the digits
in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

def chain(ans):

    while ans != 1 and ans != 89:
        if ans in my_dic:
            ans = my_dic[ans]
        else:
            ans = square_digits(ans)
        temp_set.add(ans)
        # print(ans)
    for x in temp_set:
        my_dic[x] = ans
    return ans

def square_digits(num):
    my_sum = 0
    for char in list(str(num)):
        my_sum += squares[char]
    return my_sum

if __name__ == "__main__":
    squares = {}
    for x in range(0, 10):
        squares[str(x)] = x**2
    result = 0
    my_dic = {}
    for n in range(1, 10000000):
        temp_set = set()
        if chain(n) == 89:
            result += 1
    print(result)
