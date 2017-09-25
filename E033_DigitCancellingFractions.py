'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''
from fractions import Fraction

def fake_reduce(num1, num2):
    if num1 == num2:
        return False
    elif num1%10 == num2//10 and num1//10 == num2%10:
        return False
    elif num1%10 == num2//10:
        return (num1//10, num2%10)
    elif num1//10 == num2%10:
        return (num1%10, num2//10)
    else:
        return False



if __name__ == "__main__":
    big_num = 1
    big_denom = 2
    for num in range(10, 100):
        for denom in range(num, 100):
            fake = fake_reduce(num, denom)
            if fake and fake[1] != 0:
                fraction1 = num/denom
                fraction2 = fake[0]/fake[1]
                if fraction1 == fraction2:
                    print(num, denom, fraction1, fraction2)
                    big_num *= num
                    big_denom *= denom
    print(Fraction(big_num, big_denom))
