'''
Created on Mar 20, 2014

@author: Daniel Corroto

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
from numberUtil import mcd

def fractionGenerator(x=100):
    for i in xrange(11, x):
        if (i % 10 != 0 and i % 11 != 0):
            yield i

def isEqualsFractions(x, y, m, n):
    mcd1 = mcd(x, y)
    mcd2 = mcd(m, n)
    return x // mcd1 == m // mcd2 and y // mcd1 == n // mcd2

num = 1
den = 1
for num1 in fractionGenerator():
    for den2 in xrange(1, 10):
        num2 = num1 % 10
        den1 = num1 // 10 * 10 + den2
        if num1 < den1 and isEqualsFractions(num1, den1, num2, den2):
            num *= num2
            den *= den2
        den1 = num1 // 10 + den2 * 10
        if num1 < den1 and isEqualsFractions(num1, den1, num2, den2):
            num *= num2
            den *= den2

        num2 = num1 // 10
        den1 = num1 % 10 * 10 + den2
        if num1 < den1 and isEqualsFractions(num1, den1, num2, den2):
            num *= num2
            den *= den2
        den1 = num1 % 10 + den2 * 10
        if num1 < den1 and isEqualsFractions(num1, den1, num2, den2):
            num *= num2
            den *= den2

print den / mcd(num, den)
