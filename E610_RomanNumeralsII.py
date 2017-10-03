'''
A random generator produces a sequence of symbols drawn from the set
{I, V, X, L, C, D, M, #}.
Each item in the sequence is determined by selecting one of these symbols at random,
independently of the other items in the sequence.
At each step, the seven letters are equally likely to be selected,
with probability 14% each, but the # symbol only has a 2% chance of selection.

We write down the sequence of letters from left to right as they are generated,
and we stop at the first occurrence of the # symbol (without writing it).
However, we stipulate that what we have written down must always (when non-empty)
be a valid Roman numeral representation in minimal form. If appending the next
letter would contravene this then we simply skip it and try again with the next
symbol generated.

Please take careful note of About... Roman Numerals for the definitive rules
for this problem on what constitutes a "valid Roman numeral representation"
and "minimal form". For example, the (only) sequence that represents 49 is XLIX.
The subtractive combination IL is invalid because of rule (ii), while XXXXIX is
valid but not minimal. The rules do not place any restriction on the number of
occurrences of M, so all integers have a valid representation.
These are the same rules as were used in Problem 89,
and members are invited to solve that problem first.

Find the expected value of the number represented by what we have written down
when we stop. (If nothing is written down then count that as zero.)
Give your answer rounded to 8 places after the decimal point.
'''
import re
import sys

def num_to_neum(number):
    ones =     {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 0:''}
    tens =     {1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC', 0:''}
    hundreds = {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM', 0:''}

    one = ''
    ten = ''
    hundred = ''
    thousand = ''
    if number >= 0:   one     = ones[      number        %10 ]
    if number >= 10:  ten     = tens[      (number//10)  %10 ]
    if number >= 100: hundred = hundreds[  (number//100) %10 ]
    if number >= 1000: thousand = "M" * (number // 1000)

    return thousand + hundred + ten + one

if __name__ == "__main__":


    expected1 = 0
    for n in range(1, 10000):
        roman = num_to_neum(n)

        prob = .14**len(roman) * .02
        print(n, roman, len(roman), expected1)
        expected1 += n*prob
    print(expected1)
    #
    # expected2 = 0
    # for n in range(1, 100000):
    #     roman = num_to_neum(n)
    #     prob = .14**len(roman) * .02
    #     expected2 += n*prob


    # print(expected1-expected2)
    # print(expected1)
    # print(expected2)













#
# GENERAL ROMAN NUMERAL STUFF
#
#
#     # my_string = sys.argv[1]
#
#
#     pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
#         #   ^ is the start of the string
#         #   M is the character to match
#         #   M can occur 0 to 3 times
#         #   $ is the end of the string
#         #   (A|B) matches A or B but not both
#         #   ? shows an optional character
#         #   M* for any number of m's
#     if re.search(pattern, my_string):
#         print("yay")
#
#     pattern = '''
#         ^                   # beginning of string
#         M{0,3}              # thousands - 0 to 3 Ms
#         (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
#                             #            or 500-800 (D, followed by 0 to 3 Cs)
#         (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
#                             #        or 50-80 (L, followed by 0 to 3 Xs)
#         (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
#                             #        or 5-8 (V, followed by 0 to 3 Is)
#         $                   # end of string
#         '''
#         # from Dive Into Python 3
#
#     if re.search(pattern, my_string, re.VERBOSE):
#         print("yay")
