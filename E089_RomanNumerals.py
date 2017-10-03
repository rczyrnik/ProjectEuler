'''
For a number written in Roman numerals to be considered valid there are basic
rules which must be followed. Even though the rules allow some numbers to be
expressed in more than one way there is always a "best" way of writing a
particular number.

For example, it would appear that there are at least six ways of writing the
number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last
example is considered to be the most efficient, as it uses the least number
of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
contains one thousand numbers written in valid, but not necessarily minimal,
Roman numerals; see About... Roman Numerals for the definitive rules for this
problem.

Find the number of characters saved by writing each of these in their minimal
form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.
'''

def minimize(numeral):
    # numeral.replace('IV', 'IIII')
    # numeral.replace('IX', 'VIIII')
    # numeral.replace('XL', 'XXXX')
    # numeral.replace('XC', 'LXXXX')
    # numeral.replace('CD', 'CCCC')
    # numeral.replace('CM', 'DCCCC')
    numeral = numeral.replace('VIIII','IX')
    numeral = numeral.replace('IIII','IV')
    numeral = numeral.replace('LXXXX','XC')
    numeral = numeral.replace('XXXX','XL')
    numeral = numeral.replace('DCCCC','CM')
    numeral = numeral.replace('CCCC','CD')

    return numeral



if __name__ == "__main__":
    with open("E089.txt") as f:
        data = f.readlines()
    numbers = [x.strip('\n') for x in data]

    saved = 0
    for n in numbers:
        saved += len(n) - len(minimize(n))
    print(saved)
