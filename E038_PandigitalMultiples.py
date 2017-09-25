'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

# '''

IGNORE EVERYTHING (did by hand)

# # assume 2 digs
# def random_fn_name(x):
#     first = x/100000
#     second = x%100000
#     # print(first, second, third)
#     if first*2 == second:
#         return True
#     return False
#
# # assume 3 digit #
# # def random_fn_name(x):
# #     first = x//1000000
# #     second = x//1000%1000
# #     third = x%1000
# #     # print(first, second, third)
# #     if first/1 == second/2 == third/3:
# #         return True
# #     return False
#
#
# if __name__ == "__main__":
#         # x = 192384576
#     for x in range(987654321, 918273645, -1):
#         if random_fn_name(x):
#             print(x)
