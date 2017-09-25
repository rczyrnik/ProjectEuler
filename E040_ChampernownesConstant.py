'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''


long_string = "0"
x = 1
while len(long_string) < 10000001:
    long_string += str(x)
    x += 1
print(long_string[1],
        long_string[10],
        long_string[100],
        long_string[1000],
        long_string[10000],
        long_string[100000],
        long_string[1000000]
        )
