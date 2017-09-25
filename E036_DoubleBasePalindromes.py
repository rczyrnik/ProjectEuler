'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

# forward binary: bin(8)[2:]
# reverse binary: bin(8)[-1:1:-1]
# forward decimal: str(8)
# reverse decimal: str(8)[::-1]

# must be odd number so bin ends in 1

sum = 0
for x in range(1, 1000000, 2):
    if bin(x)[2:] == bin(x)[-1:1:-1] and str(x) == str(x)[::-1]:
        print( str(x), bin(x)[2:] )
        sum += x
print(sum)
