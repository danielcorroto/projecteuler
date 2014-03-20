'''
Created on Mar 19, 2014

@author: Daniel Corroto

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from numberUtil import getProperDivisors

def isAbundant(n):
    if (n < 1):
        return False;
    s = reduce(lambda x, y: x + y, getProperDivisors(n))
    return s > n

abundants = [isAbundant(n) for n in xrange(28124)]

count = 0
for i in xrange(28124):
    twoAbundants = False
    for j in xrange(i / 2 + 1):
        if (abundants[j] and abundants[i - j]):
            twoAbundants = True
    if (not twoAbundants):
        count += i

print count



