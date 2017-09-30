'''
Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
'''

#
# def n_by_n_sum(n):
#     if n = 1: return 1
#     my_sum = 0
#     while n < 6:


my_sum = 1
bottom_left = 3
for n in range(3, 1002,2):
    #print(n, bottom_left,  my_sum)
    my_sum += 4*bottom_left+6*(n-1)
    bottom_left = bottom_left + (n-1)*4 + 2
print(n, my_sum)
